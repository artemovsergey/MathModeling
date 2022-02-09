const N = 1000;         // Количество случайных точек
const m = 12;           // Количество ячеек гистограммы

let lambda = 2.5;       // Параметр экспоненциального распределения
let lambda_est;         // Оценка параметра экспоненциального распределения
let h = [];             // Массив гистограммы [m + 1];  
let Pk = [];            // Массив вероятностей попадания в k-ю ячейку гистограммы [m + 1];
let x = [];             // Массив полученных случайных чисел [N];

for (let k = 0; k <= m; k++) {
	h[k] = 0;           // Обнуление гистограммы
}

let dx = 5.0/m;         // Ширина ячейки гистограммы
lambda_est = 0;

for (let i = 1; i <= N; i++) {               // Основной цикл генерации N случайных чисел
    let r = Math.random();
    x[i] = -Math.log(r)/lambda;
	if (x[i] <= 5) {
		let k = Math.floor(x[i]/dx);        // Адрес ячейки, в которую попало число x
        h[k] = h[k] + 1;
	} else {
		h[m] = h[m] + 1;                    // Числа, большие 5, помещаются в m-ю ячейку
	}
	lambda_est = lambda_est + x[i];
}

lambda_est = N/lambda_est;

let x_sort = [];                            // [N]; Массив отсортированных случайных чисел
for (let i = 0; i <= N; i++) {
	x_sort[i] = x[i];
}

for (let k = 0; k <= N; k++) {                 //Сортировка
	for (let i = N; i >= k; i--) {
		if (x_sort[i] < x_sort[i - 1]) {
			let t = x_sort [i];
			x_sort[i] = x_sort[i - 1];
			x_sort[i - 1] = t;
		}
	}
}

let d_max = 0;                                  // Максимальное расстояние между теоретической и
                                                // эмпирической функциями распределения

for (let i = 0; i <= N; i++) {                            // Цикл определения d_max
	let Fi = 1 - Math.exp( -lambda_est * x_sort[i] );    // Теоретическая ф.р.
	let d = Math.abs(i/N - Fi);                // i/N – эмпирическая ф.р. (нижняя «ступенька»)
	if (d_max < d) {
		d_max = d;
	}
	d = Math.abs((i + 1)/N - Fi);             // (i+1)/N – эмпирическая ф.р. (нижняя «ступенька»)
	if (d_max < d) {
		d_max = d;
	}
}
let Dn = Math.sqrt(N - 1.0) * d_max;                //Критерий Колмогорова-Смирнова




console.log('');
console.log('lambda = ', lambda);
console.log('lambda_est = ', lambda_est);
console.log('');

console.log('Гистограмма');
for (let k = 0; k <= m; k++) {
    console.log(k + 1, ' - ', h[k]);
};
console.log('');

console.log('Критерий Колмогорова-Смирнова = ', Dn);
console.log('Dn cr = ', 1.36 );
console.log('');
