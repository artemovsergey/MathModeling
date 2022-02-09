const fs = require("fs");
fs.writeFileSync("9.txt", "X Y Z D E\r\n");     // Запись в файл строки со структурой обучающих примеров

const N = 1000;								// Количество случайных точек
let V = 0;									// Значение вычисляемой площади (определенного интеграла)
let D = 0;
let E = 0;
let a = 0, b = 1;                               //Границы интервала

for (let i = 0; i < N; i++)           		// Цикл генерации точек
{
	let x = Math.random();
	let y = Math.random();
	let z = Math.random();

   	x = x*(b - a) + a;
   	y = y*(b - a) + a;
   	z = z*(b - a) + a;
	
	if ( x * x + y * y < 1 && x > 0 && y > 0) {
		let d = Math.sqrt(1 - x*x - y*y);
		let e = 1;
		if (z >= d) {
			e = 0;
		}
		fs.appendFileSync("9.txt", `${x} ${y} ${z} ${d} ${e}\r\n`);
		D = D + d;
		E = E + e;
	} else {
		fs.appendFileSync("9.txt", `${x} ${y} ${z} ${0} ${0}\r\n`);
	}
	
	if (x*x + y*y + z*z < 1) {
		V = V + 1;         					// Проверка условия попадания под поверхность сферы
	}
}
let V_c = E/N;
let custom_Pi_est = 6*V_c;
let custom_epsilon = 2.6*Math.sqrt(V_c*(1 - V_c)/N);	//Расчет погрешности

V = V/N;
let Pi_est = 6*V;
let epsilon = 2.6*Math.sqrt(V*(1 - V)/N);	//Расчет погрешности


console.log("");
console.log("custom_Pi_est = ", custom_Pi_est);
console.log("custom_epsilon = ", custom_epsilon);
console.log("");
console.log("Pi_est", Pi_est);
console.log("epsilon", epsilon);
console.log("");

// console.log(JSON.stringify({ A, B, C, D, E}));
