const fs = require("fs");

//Объявление глобальных переменных
let n=9;                                  //Степень двойки для расчета N
let N1 = (Math.pow(2, n)) + 1;                             //Количество точек сигнала (Math.pow(2, n)) + 1
let Depth = 5;                            //Глубина вейвлет-разложения сигнала
let m_array = [];                         //Массив сигнала [N1]

for (let k = 0; k < N1; k++) {
  m_array[k] = 0;
}

var text = fs.readFileSync('12.dat','utf8')
fs.writeFileSync("13-r.dat", "");
let file_array = text.split('\r\n');

for (let k = 0; k < N1; k++) {
  m_array[k] = Number(file_array[k]);
}

let m_array_d = Decomposition([].concat(m_array), N1, Depth);

let m_array_f1 = Filtration([].concat(m_array_d), Depth, 0, 10);
let m_array_f2 = Filtration([].concat(m_array_f1), Depth, 1, 10);
let m_array_f3 = Filtration([].concat(m_array_f2), Depth, 2, 10);

let m_array_r = Reconstruction([].concat(m_array_f3), N1, Depth);

for (let k = 0; k < N1; k++) {
  if (m_array_r[k]) {
    fs.appendFileSync("13-r.dat", `${k} ${m_array_r[k]}\r\n`);
  }
}





function Decomposition(m_array, N1, Depth)                    //Функция прямого вейвлет-преобразования
{
  //p, q и r являются вспомогательными переменными 
  let p = Math.pow(2, n-1);                   //двойка в степени (n-1)
  let q = 2;
  let r = 1;

	for (let lev = 1; lev <= Depth; lev++)  //Цикл последовательного вейвлет-разложения
	{
		for (let k = 1; k <= p; k++)
		{
      let temp = (2*k - 1)*r;
      m_array[temp] = m_array[temp] - 0.5*(m_array[(k - 1)*q] + m_array[k*q]);
    }

    m_array[0] = m_array[0] + 0.5*m_array[r]; //Здесь использовано зеркальное отражение сигнала от границ

    m_array[N1 - 1] = m_array[N1 - 1] + 0.5*m_array[N1 - 1 - r];        
    for (let k = 1; k < p; k++)
    {		
        m_array[k*q] = m_array[k*q] + 0.25*(m_array[(2*k - 1)*r] + m_array[(2*k + 1)*r]);
    }

    p = p/2;
    r = q;
    q = q*2;
  }

  return m_array;
} 

function Reconstruction(m_array, N1, Depth)                   //Функция обратного вейвлет-преобразования
{
  //p, r и q являются вспомогательными переменными
  let p = Math.pow(2, n - Depth);                   //двойка в степени (n-Depth)
  let r = Math.pow(2, Depth - 1);                   //двойка в степени (Depth-1)
  let q = Math.pow(2, r);                           //двойка в степени r


  for (let lev = Depth; lev > 0; lev--)     //Цикл последовательной вейвлет-сборки
  {
    for (let k = 1; k < p; k++) {
      let tmp = m_array[k*q];
      m_array[k*q] = tmp - 0.25*(m_array[(2*k - 1)*r] + m_array[(2*k + 1)*r]);
    }

    m_array[0] = m_array[0] - 0.5*m_array[r];
    m_array[N1 - 1] = m_array[N1 - 1] - 0.5*m_array[N1 - 1 - r];

    for (let k = 1; k <= p; k++)
    {
      let temp = (2*k - 1)*r;
      m_array[temp] = m_array[temp] + 0.5*(m_array[(k - 1)*q] + m_array[k*q]);
    }

    p = p*2;
    q = r;
    r = r/2;
  }

  return m_array;
}

function Filtration(m_array, Depth, layer_numb, threshold)
{
  //Функция фильтрации одного уровня вейвлет-спектра с номером layer_numb
  //На данном уровне зануляются все вейвлет-коэффициенты,
  //модуль которых меньше значения threshold
	let k=0;
  if (layer_numb <= Depth)
  {
    let layer_size = Math.pow(2, n - layer_numb);           //двойка в степени (n-layer_numb)
    let t =  Math.pow(2, layer_numb - 1);                   //двойка в степени (layer_numb-1)

    for (k = 1; k < layer_size; k++)
    {
      if (Math.abs(m_array[(2*k + 1)*t]) <= threshold)      //fabs() вычисляет модуль числа (double)
        m_array[(2*k + 1)*t] = 0;
    }
  }
  else
  {
    let layer_size = Math.pow(2, n - Depth) + 1;            //двойка в степени (n-Depth)
    let t = Math.pow(2, Depth);                             //двойка в степени Depth

    if (Math.abs(m_array[k*t]) <= threshold)
      m_array[k*t] = 0;
  }

  return m_array;
}
