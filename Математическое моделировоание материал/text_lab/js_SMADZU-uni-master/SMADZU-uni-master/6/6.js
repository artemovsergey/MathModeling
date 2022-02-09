const N = 1000;      //Количество случайных точек
const m = 12;  //Количество ячеек гистограммы
let a = 2;//Параметр распределения Коши
let a_est;//Оценка параметра распределения Коши

let h = []; //[m + 2];//Массив гистограммы
let Pk = []; //[m + 2];//Массив вероятностей попадания в k-ю ячейку гистограммы
let x = []; //[N];      //Массив полученных случайных чисел
let x_sort = []; //[N];//Отсортированный массив случайных чисел

let gamma = 1;

for (let k = 0; k <= m + 1; k++) {
	h[k] = 0;      //Обнуление гистограммы
}

for (let i = 0; i < N; i++) {                      //Основной цикл генерации N случайных чисел
	let r = Math.random();
	x[i] = gamma*Math.tan(3.141593*(r - 0.5)) + a;
}

for (let i = 0; i < N; i++)
{
	x_sort[i] = x[i];               //Копирование неотсортированного массива в 							//отсортированный
}

for (let k = 0; k < N; k++)
{
	for (let i = N; i >= k; i--)
	{
		if (x_sort[i] < x_sort[i - 1])
		{
			let t = x_sort [i];            //Временная переменная
			x_sort [i] = x_sort [i - 1];
			x_sort [i - 1] = t;
		}
	}
}

a_est = x_sort[N/2];

let dx = 10.0/m;                                    //Ширина ячейки гистограммы

for (let i = 0; i < N; i++) 
{                             //Цикл заполнения гистограммы
	if (x[i] < a_est - 5)             //Если полученное число меньше левой границы
	{
		h[0] = h[0] + 1;               //области гистограммирования, оно попадает в 						//нулевую ячейку…
	}
	else 
	{
		if (x[i] > a_est + 5)    //…а если оно больше правой границы,
		{
			h[m + 1] = h[m + 1] + 1; //оно попадает в (m+1)-ю ячейку
		}
		else
		{
			let k = Math.floor((x[i] - a_est + 5)/dx) + 1;     //Адрес ячейки, в которую 										//попало число x
			if (k) {
				h[k] = h[k] + 1;
			}
		}
	}
}



let tk = []; //[m + 1];                               //Массив координат границ ячеек гистограммы

for (let k = 0; k <= m + 1; k++)
{
	tk[k] = a_est - 5 + (k - 1)*dx;
}

for (let k = 1; k <= m; k++)    //Расчет вероятностей попадания в k-ю ячейку 							//гистограммы
{
	Pk[k] = (Math.atan((tk[k + 1] - a_est)/gamma) - Math.atan((tk[k] - a_est)/gamma))/3.141593;
}	
Pk[0] = Pk[m + 1] = (Math.atan((tk[1] - a_est)/gamma))/3.141593 + 0.5;

let Hi = 0;                                          //Расчет критерия хи-квадрат
for (let k = 1; k <= m; k++)
{
	let temp = h[k] - N*Pk[k];
	Hi = Hi + temp*temp/(N*Pk[k]);
}


console.log('');
console.log('a = ', a);
console.log('Оценка a = ', a_est);

console.log('Гистограмма');
for (let k = 0; k <= m + 1; k++) {
	console.log(k + 1, ' - ', h[k]);
};
console.log('');

console.log('хи-квадрат = ', Hi);
console.log('хи-квадрат cr = ', m + 3 * Math.sqrt( 2 * m ) );
console.log('');
console.log(h.reduce((x, y) => x + y, 0));
console.log('');