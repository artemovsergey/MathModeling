const fs = require("fs");
fs.writeFileSync("15.dat", "");

let lambda = 8;    					//Интенсивность поступления требований
let t_serv = 6;						//Среднее время обслуживания одной заявки
const n = 4;       					//Количество каналов обслуживания 
const m = 2;     					//Количество мест в очереди
let p = []; 						//Массив вероятностей [n + m + 1];
let alpha = lambda*t_serv; 			//Коэффициент загрузки

try {
	let temp1 = 0;					//Первая временная переменная, необходимая для расчета p[0]
	for (let k = 1; k <= n; k++)
		temp1 = temp1 + Math.exp(k*Math.log(alpha)) / Factorial(k);
	
	let temp2 = 0;               					//Вторая временная переменная, необходимая для расчета p[0]
	for (let s = 1; s <= m; s++)
		temp2 = temp2 + Math.exp(s*Math.log(alpha / n));
	
	p[0] = 1 / (1 + temp1 + temp2*Math.exp(n*Math.log(alpha)) / Factorial(n)); //Вероятность простоя СМО
	
	for (let k = 1; k <= n; k++)
		p[k] = p[0] * Math.exp(k*Math.log(alpha)) / Factorial(k);
	
	for (let s = 1; s <= m; s++)
		p[n + s] = p[0] * Math.exp(n*Math.log(alpha))*Math.exp(s*Math.log(alpha / n)) / Factorial(n);
	
		
	let N_buzy = 0;                               	//Среднее число каналов, занятых обслуживанием
	for (let k = 1; k <= n; k++)
		N_buzy = N_buzy + k*p[k];
	for (let s = 1; s <= m; s++)
		N_buzy = N_buzy + n*p[n + s];
	
	let N_vac = n - N_buzy;                			//Среднее число свободных каналов
	
	let N_req = 0;                                	//Среднее число заявок в очереди
	for (let s = 1; s <= m; s++)
		N_req = N_req + s*p[n + s];
	
	let T_line = N_req*t_serv;             			//Среднее время ожидания заявки в очереди
	let T_sys = T_line + t_serv;          			//Среднее время обслуживания заявки в СМО
	
	let Q = 1 - p[n + m];                      		//Относительная пропускная способность СМО
	let A = lambda*Q;                         		//Абсолютная пропускная способность СМО



	let countToFixed = 9;
	let P_den = p[0] * ( Math.pow(lambda * t_serv, n+m) / (Math.pow(n, m) * Factorial(n)));
	
	console.log("");
	saveInfo("Интенсивность поступления требований (lambda)", lambda);
	saveInfo("Среднее время обслуживания одной заявки (t_serv)", t_serv);
	saveInfo("Количество каналов обслуживания  (n)", n);
	saveInfo("Количество мест в очереди (m)", m);
	console.log("");
	saveInfo("Среднее число свободных каналов (N_buzy)", N_buzy.toFixed(countToFixed));
	saveInfo("Среднее число свободных каналов (N_vac)", N_vac.toFixed(countToFixed));
	saveInfo("Среднее число заявок в очереди (N_req)", N_req.toFixed(countToFixed));
	saveInfo("Среднее время ожидания заявки в очереди (T_line)", T_line.toFixed(countToFixed));
	saveInfo("Среднее время обслуживания заявки в СМО (T_sys)", T_sys.toFixed(countToFixed));
	saveInfo("Относительная пропускная способность СМО (Q)", Q.toFixed(countToFixed));
	saveInfo("Абсолютная пропускная способность СМО (A)", A.toFixed(countToFixed));
	console.log("");
	saveInfo("Вероятность отказа (P_den)", P_den.toFixed(countToFixed));
	saveInfo("Вероятность простоя СМО: ");
	for(let k = 0; k < n + m + 1; k++) {
		saveInfo(`P[${k}]`, p[k].toFixed(countToFixed));
	}
	console.log("");
	console.log("ограничение (<100) =", 10*n+n*m*2);






} catch (err) {
	console.log(err);
}

function saveInfo(text, number = null) {
	if (number) {
		console.log(`${text} = `, number);
		fs.appendFileSync("15.dat", `${text} = ${number}\r\n`);
	} else {
		console.log(`${text}`);
		fs.appendFileSync("15.dat", `${text}\r\n`);
	}
}


// Используемая здесь функция Factorial() имеет следующую реализацию:
function Factorial(number)    										//Рекуррентная функция расчета факториала числа number
{
	if (number < 0) 												//Ошибка. Факториал может быть только у неотрицательного числа 
		throw "Factorial: given number is negative!"; 				//Вывод сообщения на экран (Аварийное завершение программы)

	if (number < 2) return 1; 										//Факториалы нуля и единицы по определению равны единице
	else return number * Factorial(number - 1); 					//Рекуррентный вызов функции с уменьшенным на единицу аргументом
}
