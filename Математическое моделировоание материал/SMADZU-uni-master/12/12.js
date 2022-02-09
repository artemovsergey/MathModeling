
const fs = require("fs");
fs.writeFileSync("12.dat", ""); 	// Запись в файл строки со структурой обучающих примеров

const n = 9;						// > 8
const N = Math.pow(2, n) + 1;     		// Количество точек сигнала
let x = [], y = [];      			// Массивы координатточек сигнала [N]

let H1 = 1, H2 = 0.6;				// Значения амплитуд двух синусоид
let lambda1 = 3.5, lambda2 = 40;	// Значения частот двух синусоид
let e = 0.2;						// Уровень шума

let dx = 2*3.141593/(N - 1); 		// Величина шага изменения координаты x


for (let i = 0; i < Math.floor(N/3.0); i++)         //Моделирование первой части сигнала
{
	x[i] = i*dx;
	y[i] = H1*Math.sin(lambda1*x[i]) + e*(Math.random() - 0.5);
}

for (let i = Math.floor(N/3.0); i < Math.floor(2*N/3.0); i++)     //Моделирование второй части сигнала
{
	x[i] = i*dx;
	y[i] = H1*Math.sin(lambda1*x[i]) + H2*Math.sin(lambda2*x[i]) +
		e*(Math.random() -0.5);
}

for (let i = Math.floor(2*N/3.0); i < N; i++)                //Моделирование третьей части сигнала
{
	x[i] = i*dx;
	y[i] = H1*Math.sin(lambda1*x[i]) + e*(Math.random() - 0.5);
}

for (let i = 0; i < N; i++)
{
	fs.appendFileSync("12.dat", `${y[i]}\r\n`);
	// ofs<<y[i]<<std::endl;                   //Сохранение в файл y-координат сигнала
}

