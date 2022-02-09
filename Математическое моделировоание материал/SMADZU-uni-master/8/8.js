const fs = require("fs");
fs.writeFileSync("8.txt", "x y\r\n");     	// Запись в файл строки со структурой обучающих примеров

const N = 50;   							// Количество случайных точек
let A0 = 0.5, B0 = 11, A, B; 					// Параметры смоделированной и подогнанной прямых линий
let x = [], y = []; 						// [N] Массивы координат точек
let sigma_noise = 0.2;						// Параметр уровня нормального шума
let w = []; 								// [N]; Массив робастных весов
let d = []; 								// [N]; Массив расстояний от точек до подгоняемой прямой

for (let i = 0; i < N; i++)            		// Цикл генерации точек измерений
{
	let error = 0;                   		// Моделирование ошибки измерения на основании ЦПТ
	for (let j = 0; j < 12; j++) {
		error = error + Math.random();
	}
	error = (error - 6)*sigma_noise;

	x[i] = i;
	y[i] = A0*x[i] + B0 + error;

	if (i === N / 2) {
		y[i] -= 50;
	}

	if (i === N - 1) {
		y[i] += 50;
	}
	fs.appendFileSync("8.txt", `${x[i]} ${y[i]}\r\n`);
}

let r = 6 * (Math.random() - 0.5);
A = A0 + r;                             	// Начальное приближение параметра A
r = 4 * (Math.random() - 0.5);
B = B0 + r;                             	// Начальное приближение параметра B

for (let i = 0; i < N; i++) {
	w[i] = 1;								// Начальные веса равны единице
}

let sw = N;                             	// Начальная сумма всех весов
const C = 5;                        		// Константа весовой функции Тьюки
let S = 100000;
let k = 0;
while (S > 0.0001)       					// Цикл итерационного перерасчета параметров прямой
{
	k++;
	if (k > 100) break;             		// Если количество итераций очень большое, цикл прекращается
	let a = A, b = B;         				// Временные переменные для хранения параметров прямой

	let swd, sx, sy, sxy, sxx;
	swd = sx = sy = sxy = sxx = 0;

	for (let i = 0; i < N; i++) {
		d[i] = y[i] - a*x[i] - b;      		// Расчет расстояний от точек до подгоняемой линии
		swd += w[i]*d[i]*d[i];
	}

	let Sigma = C*Math.sqrt(swd/sw);  		// Расчет параметра весовой функции Тьюки

	for (let i = 0; i < N; i++) {       	// Цикл пересчета весов для точек
		if (Math.abs(d[i]) > Sigma) {
			w[i] = 0;
		} else {
			let temp = d[i]/Sigma;
			temp = 1 - temp*temp;
			w[i] = temp*temp;
		}
	}
	sw = 0;

	for (let i = 0; i < N; i++) {
		sw  += w[i];
		sx  += w[i]*x[i];
		sxx += w[i]*x[i]*x[i];
		sy  += w[i]*y[i];
		sxy += w[i]*x[i]*y[i];
	}

	let q = sw*sxx - sx*sx;					// Знаменатель

	if (q == 0) {                       	// Если знаменатель равен нулю…
		console.log("Error: q = 0. Line is vertical!");
		break;
	} else {
		A = (sw*sxy - sx*sy)/q;
		B = (sy*sxx - sx*sxy)/q;
	}

	S = (A - a)*(A - a) + (B - b)*(B - b);	//Расчет условия сходимости параметров
}

console.log("");
console.log("a = ", A0);
console.log("b = ", B0);
console.log("A = ", A);
console.log("B = ", B);
console.log("k = ", k);
console.log("");
