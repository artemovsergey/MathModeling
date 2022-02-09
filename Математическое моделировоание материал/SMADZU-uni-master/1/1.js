const N = 1000;                              //Количество случайных точек
const m = 12;                                //Количество испытаний
let p = 0.3;                                 //Вероятность удачного исхода
let p_est;                                   //Оценка вероятности удачного исхода
let Ki = []; //[N];                          //Массив количества испытаний, закончившихся удачно
let h = []; //[m + 1];                       //Массив гистограммы
let Pk = []; //[m + 1];                      //Массив вероятностей попадания в k-ю ячейку гистограммы

for (let k = 0; k <= m; k++) h[k] = 0;        //Обнуление гистограммы

p_est = 0;

for (let i = 0; i < N; i++)                    //Основной цикл генерации N случайных чисел
{
    Ki[i] = 0;
    for (let j = 0; j < m; j++)                //Цикл моделирования из m испытаний
    {
        let r = Math.random();
        if (r < p) {
            Ki[i] = Ki[i] + 1;
        }
    }
    h[Ki[i]] = h[Ki[i]] + 1;
    p_est =p_est + Ki[i] ;
}

p_est = p_est / ( m * N * 1.0) ;

let q_est = 1 - p_est;

Pk[0] = Math.exp( m * Math.log(q_est));                 //Вероятность того, что не было ни одного удачного исхода

for (let k = 0; k < m; k++) {                             //Рекуррентная формула
    Pk[k + 1] = Pk[k]*(m - k)*p_est/((k + 1)*q_est);    //расчета вероятностей
}

let Hi = 0;                                             //Расчет критерия хи-квадрат

for (let k = 0; k <= m; k++)
{
   let temp = h[k] - N*Pk[k];
   Hi = Hi + temp * temp / ( N * Pk[k]);
}

console.log('');
console.log('Параметр P = ', p);
console.log('Оценка P = ', p_est);
console.log('');

console.log('Гистограмма');
for (let k = 0; k <= m; k++) {
    console.log(k + 1, ' - ', h[k]);
};
console.log('');

console.log('хи-квадрат = ', Hi);
console.log('хи-квадрат cr = ', m + 1 + 3 * Math.sqrt( 2 * (m + 1) ) );
console.log('');