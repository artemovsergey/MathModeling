const N = 1000;        //Количество случайных точек
const m = 12;        //Количество ячеек гистограммы
let lambda = 2;         //Параметр распределения Пуассона
let lambda_est;     //Оценка параметра распределения Пуассона
let Ki = [];        //[N];//Счетчик количества перемножений случайных чисел
let h = [];         //[m + 1];//Массив гистограммы
let Pk = [];        //[m + 1];//Массив вероятностей попадания в k-ю ячейку гистограммы

for (let k = 0; k <= m; k++) {
	h[k] = 0;					 //Обнуление гистограммы
}

Pk[0] = Math.exp(-lambda);            //Расчет вероятности попадания в нулевую ячейку

lambda_est = 0;


for (let i = 0; i < N; i++)      //Основной цикл генерации N случайных чисел
{
	Ki[i] = -1;
    let S = 1;                //Произведение случайных чисел
    
	do {
		let r = Math.random();
		S = S * r;
		Ki[i] = Ki[i] + 1;
	} while (S > Pk[0]);

	if (Ki[i] < m) {
		h[Ki[i]] = h[Ki[i]] + 1;
	} else {	
		h[m] = h[m] + 1;         //Все значения, большие m - 1, помещаются в m-юячейку
    }
    
	lambda_est = lambda_est + Ki[i];
}

lambda_est = lambda_est / ( N * 1.0 );

Pk[0] = Math.exp(-lambda_est);

let SumPk = Pk[0] ;           //Сумма всех вероятностей до (m-1)-й ячейки

for (let k = 0; k <= m - 2; k++)
{
	Pk[k + 1] = Pk[k] * lambda_est / (k + 1);
	SumPk = SumPk + Pk[k + 1];
}

Pk[m] = 1 - SumPk;

let Hi = 0;                   //Расчет критерия хи-квадрат
for (let k = 0; k < m; k++)
{
	let temp = h[k] - N*Pk[k];
	Hi = Hi + temp*temp/(N*Pk[k]);
}


console.log('');
console.log('lambda = ', lambda);
console.log('lambda_est = ', lambda_est);
console.log('');

console.log('Гистограмма');
for (let k = 0; k <= m; k++) {
    console.log(k + 1, ' - ', h[k]);
};
console.log('');

console.log('хи-квадрат = ', Hi);
console.log('хи-квадрат cr = ', m + 3 * Math.sqrt( 2 * m ) );
console.log('');