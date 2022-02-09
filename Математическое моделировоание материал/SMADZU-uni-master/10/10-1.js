const fs = require("fs");

let N = 300 / 3;                                    // Размер обучающей выборки

let a = 5;                                          // Середина квадрата
let bx = [ 2, 8, 4 ];                               // соответствует среднему значению (математическому ожиданию)
let by = [ 2, 2, 8 ];                               // соответствует среднему значению (математическому ожиданию)
let sigma = 0.75;						            // соответствует разбросу относительно среднего (стандартному отклонению)

fs.writeFileSync("10-1.txt", "in out res\r\n");     // Запись в файл строки со структурой обучающих примеров
fs.writeFileSync("10-1-TEST.txt", "in out\r\n");     // Запись в файл строки со структурой обучающих примеров

for (let k = 0; k < 3; k++) {
    let x_min = 10;
    let x_max = 0;
    let y_min = 10;
    let y_max = 0;
    for (let i = 0; i < N; i++)                     // Цикл генерации точек и записи в файл обучающих примеров
    {
        let x = 0;
        let y = 0;
        for (let j = 1; j <= 12; j++)               //	Вычисление суммы 12 случайных чисел
        {
            x = x + Math.random();
            y = y + Math.random();
        }
        x = (x - 6) * sigma + bx[k];
        y = (y - 6) * sigma + by[k];

        if (x > x_max) x_max = x;
        if (x < x_min) x_min = x;
        if (y > y_max) y_max = y;
        if (y < y_min) y_min = y;
        
        fs.appendFileSync("10-1.txt", `${x} ${y} ${k + 1}\r\n`);
                                                    // Запись в файл строки с обучающим примером
    }
    
    console.log("x_min", x_min);
    console.log("x_max", x_max);
    console.log("y_min", y_min);
    console.log("y_max", y_max);
    console.log("");
}

for (let i = 0; i < 10; i++)                     // Цикл генерации точек и записи в файл обучающих примеров
{
    let x = 0;
    let y = 0;
    for (let j = 1; j <= 12; j++)               //	Вычисление суммы 12 случайных чисел
    {
        x = x + Math.random();
        y = y + Math.random();
    }
    x = (x - 6) * sigma + a;
    y = (y - 6) * sigma + a;
    fs.appendFileSync("10-1-TEST.txt", `${x} ${y}\r\n`);
}


