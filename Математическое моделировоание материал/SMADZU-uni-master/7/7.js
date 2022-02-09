const fs = require("fs");
fs.writeFileSync("7.txt", "x y\r\n");     // Запись в файл строки со структурой обучающих примеров

const N = 50;    						// Количество случайных точек
let x = [], y = []; 	 				// Массивы координат точек [N] 

let A0 = -1, B0 = 2, A = 0, B = 0;		// Параметры смоделированной и подогнанной прямых линий
let sigma_noise = 0.3; 					// Параметр уровня нормального шума


for (let i = 0; i < N; i++)            	// Цикл генерации точек измерений
{
	let error = 0;                   	// Моделирование ошибки измерения на основании ЦПТ
	for (let j = 0; j < 12; j++) {
		error = error + Math.random();
	}
	error = (error - 6) * sigma_noise;

	x[i] = i;
	y[i] = A0 * x[i] + B0 + error;
	fs.appendFileSync("7.txt", `${x[i]} ${y[i]}\r\n`);
}

let sx, sy, sxx, syy, sxy;
sx = sy = sxx = syy = sxy = 0;


for (let i = 0; i < N; i++) 			// Расчет сумм, необходимых для оценки параметров прямой
{
	sx  = sx  + x[i];
	sy  = sy  + y[i];
	sxx = sxx + x[i]*x[i];
	syy = syy + y[i]*y[i];
	sxy = sxy + x[i]*y[i];
}

let q = N * sxx - sx * sx;									// Знаменатель

if (q == 0) {                                               // Если знаменатель равен нулю…
	console.log("Error: q = 0. Line is vertical!");
} else {
	A = ( N * sxy - sx * sy) / q;
	B = ( sy * sxx - sx * sxy) / q;
	
	let Fmin = 0;
	for (let i = 0; i < N; i++) {
		Fmin = Fmin + (y[i] - A*x[i]- B) * (y[i] - A*x[i]- B);
	}
	
	let sigma = Math.sqrt(Fmin/(N - 2));					// Среднеквадратичная ошибка приближения
	let sigma_A = sigma*Math.sqrt(N/q);                 	// Погрешность расчета A
	let sigma_B = sigma*Math.sqrt(sxx/q);              		// Погрешность расчета B

	console.log("");
	console.log("Ao = ", A0);
	console.log("Bo = ", B0);
	console.log("A = ", A);
	console.log("B = ", B);
	console.log("Fmin = ", Fmin);
	console.log("Среднеквадратичная ошибка = ", sigma);
	console.log("Погрешность расчета A = ", sigma_A);
	console.log("Погрешность расчета B = ", sigma_B);
	console.log("");
}

