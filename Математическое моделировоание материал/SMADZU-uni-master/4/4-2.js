const N = 1000;    	// Количество случайных точек
const m = 12;     	// Количество ячеек гистограммы

let sigma = 1; 			// Параметр распределения Рэлея
let sigma_est;		// Оценка параметра распределения Рэлея

let h = []; 		// [m + 1];    //Массив гистограммы
let x = []; 		// [N];    //Массив полученных случайных чисел


for (let k = 0; k <= m; k++) 
{
	h[k] = 0;   //Обнуление гистограммы
}

let dx = 10.0/m;                         			//Ширина ячейки гистограммы
let SumX2 = 0;                           			//Сумма квадратов случайных чисел

for (let i = 1; i <= N; i++) {                      	// Основной цикл генерации N случайных чисел
	let r = Math.random();
	x[i] = sigma * Math.sqrt(-2 * Math.log(r));
	SumX2 = SumX2 + x[i]*x[i];

	if (x[i] > 10) {
		h[m] = h[m] + 1;          					// Все числа, большие 10, попадают в m-ю ячейку
	} else {
		let k = Math.floor((x[i])/dx);                    	// Адрес ячейки гистограммы, в которую 							//попало число x
		h[k] = h[k] + 1;
	}
}

sigma_est = Math.sqrt(0.5*SumX2/N);

let tk = []; 										// [m + 1]; //Массив координат ячеек гистограммы
let Pk = [];

for (let k = 0; k <= m; k++)
{
	tk[k] = k*dx;
}

for (let k = 0; k < m; k++)
{
	Pk[k] = Math.exp(-0.5*tk[k]*tk[k]/sigma_est*sigma_est) -                    			
			Math.exp(-0.5*tk[k + 1]*tk[k + 1]/sigma_est*sigma_est);         //Расчет вероятностей  					//попадания в k-ю ячейку гистограммы
	// console.log("Pk[k]", Pk[k]);
}
Pk[m] = Math.exp(-0.5*tk[m]*tk[m]/sigma_est*sigma_est);                  

let Hi = 0;                                                                    //Расчет критерия хи-квадрат
for (let k = 0; k < m; k++)
{
	let temp = h[k] - N * Pk[k];
	Hi = Hi + temp * temp / ( N * Pk[k] );
}

console.log('');
console.log('sigma = ', sigma);
console.log('Оценка sigma = ', sigma_est);

console.log('Гистограмма');
for (let k = 0; k < m; k++) {
    console.log(k + 1, ' - ', h[k]);
};
console.log('');

console.log('хи-квадрат = ', Hi);
console.log('хи-квадрат cr = ', m + 3 * Math.sqrt( 2 * m ) );
console.log('');
