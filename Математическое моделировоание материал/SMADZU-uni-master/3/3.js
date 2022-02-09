const N = 1000;                                 //Количество случайных точек
const m = 12;                                   //Количество ячеек гистограммы
let a = 1, b = 3;                               //Границы интервала
let a_est, b_est;                               //Оценки границинтервала
let h = [];                 //[m];              //Массив гистограммы
let x = [];                 //[N];              //Массив полученных случайных чисел
let x_sort = [];            //[N];              //Массив отсортированных по возрастанию случайных чисел

for (let k = 0; k < m; k++) {
	h[k] = 0;						            //Обнуление гистограммы
}

for (let i = 0; i < N; i++) {                   //Основной цикл генерации N случайных чисел
   let r = Math.random();
   x[i] = r*(b - a) + a;
}

for (let i = 0; i < N; i++) {
	x_sort[i] = x[i];                           //Копирование неотсортированного массива в 							отсортированный
}

for (let k = 0; k < N; k++) {
	for (let i = N; i >= k; i--) {
		if (x_sort[i] < x_sort[i - 1]) {
			let t = x_sort [i];               //Временная переменная
			x_sort[i] = x_sort [i - 1];
			x_sort[i - 1] = t;
		}
	}
}

a_est = x_sort[0];
b_est = x_sort[N - 1];

let dx = (b_est - a_est) / m;                   //Ширина ячейки гистограммы

for (let i = 0; i < N; i++) {                     //Цикл заполнения гистограммы
	let k = parseInt((x[i] - a_est) / dx);      // Адрес ячейки, в которую попало число x
    if (k === m) {
        h[k - 1] = h[k - 1] + 1;
    } else {
        h[k] = h[k] + 1;
    }
}

let Pk = 1.0 / m;                                 //Вероятность попадания в любую ячейку гистограммы

let Hi = 0;                                     //Расчет критерия хи-квадрат
for (let k = 0; k<m; k++) {
	let temp = h[k] - N * Pk;
	Hi = Hi + temp * temp / ( N * Pk);
}

console.log('');
console.log('A = ', a);
console.log('Оценка A = ', a_est);
console.log('B = ', b);
console.log('Оценка B = ', b_est);
console.log('');

console.log('Гистограмма');
for (let k = 0; k < m; k++) {
    console.log(k + 1, ' - ', h[k]);
};
console.log('');

console.log('хи-квадрат = ', Hi);
console.log('хи-квадрат cr = ', m + 3 * Math.sqrt( 2 * m ) );
console.log('');