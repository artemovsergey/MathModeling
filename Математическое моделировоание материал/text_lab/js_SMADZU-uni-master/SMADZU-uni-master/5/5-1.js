const N = 1000;      				//Количество случайных точек
const m = 12;    					//Количество ячеек гистограммы
let a = 2, sigma = 3;				//Параметры нормального распределения
let a_est = 0, sigma_est = 0;		//Оценки параметров нормального распределения
let h = []; 			// [m + 2]; // Массив гистограммы
let x = []; 			// [N];    	// Массив полученных случайных чисел

for (let k = 0; k < m + 1; k++) {
	h[k] = 0;  			//Обнуление гистограммы
}

for (let i = 0; i < N; i++)	{			//Основной цикл генерации N случайных чисел
	let y = Math.random();

	do {
		let r = Math.random();			//Генерация точек внутри прямоугольника
		x[i] = 6*sigma*(r - 0.5) + a;
   		y = Math.random();
  	}
	while ( y > Math.exp(-(x[i]-a)*(x[i]-a)/(2*sigma*sigma)));//Условие попадания под кривую

	a_est = a_est + x[i];
}
a_est = a_est / N;

for (let i = 0; i < N; i++) {       					// Циклрасчета sigma_est
	sigma_est += ( x[i] - a_est ) * (x[i] - a_est);
}
sigma_est = Math.sqrt( sigma_est / N );
let dx = 6 * sigma_est / m;                  			//Ширина ячейки гистограммы


for (let i = 0; i < N; i++) {                         	//Цикл заполнения гистограммы
	if (x[i] < a_est - 3 * sigma_est) {					//Если полученное число меньше левой границы
		h[0] = h[0] + 1;								//прямоугольника, оно попадает в нулевую ячейку…
	} else {
		if (x[i] >a_est + 3*sigma_est) { 				//…а если оно больше правой границы,
			h[m + 1] = h[m + 1] + 1;					//оно попадает в (m+1)-ю ячейку
		} else {
			let k = Math.floor((x[i] - a_est + 3*sigma_est)/dx) + 1; //Адрес ячейки, в 										//которую попало число x
			h[k] = h[k] + 1;
		}
	}
}









let Pk = []; //[m + 2];                 //Массив вероятностей попадания в k-ю ячейку 						//гистограммы
let tk = []; //[m + 1];                  //Массив координат границ ячеек гистограммы

for (let k = 0; k <= m + 1; k++)
{
	tk[k] = a_est - 3*sigma_est + (k - 1)*dx;
}

let SumPk = 0;              //Сумма вероятностей попадания в m ячеек 						//гистограммы
for (let k = 1; k <= m; k++) {
	let x_m = 0.5*(tk[k] + tk[k + 1]);         //Средняя точка, в которой 									//вычисляется функция
	Pk[k] = dx * Math.exp(-(x_m - a_est)*(x_m - a_est)/
            (2*sigma_est *sigma_est))/(Math.sqrt(2*3.141593)*sigma_est);
	SumPk = SumPk + Pk[k];
}
Pk[0] = Pk[m + 1] = 0.5 * (1 - SumPk);

let Hi = 0;                                            //Расчет критерия хи-квадрат
for (let k = 0; k < m + 1; k++) {
	let temp = h[k] - N * Pk[k];
	Hi = Hi + temp * temp / (N * Pk[k]);
}




console.log('');
console.log('sigma = ', sigma);
console.log('Оценка sigma = ', sigma_est);
console.log('');
console.log('a = ', a);
console.log('Оценка a = ', a_est);

console.log('Гистограмма');
for (let k = 0; k < m + 1; k++) {
    console.log(k + 1, ' - ', h[k]);
};
console.log('');

console.log('хи-квадрат = ', Hi);
console.log('хи-квадрат cr = ', m + 3 * Math.sqrt( 2 * m ) );
console.log('');
