const alpha1=1
const betta1=0
const gamma1=1
const alpha2=1
const betta2=0
const gamma2=0.5

function solver(a, b, c, d, e, f) {
    let y = (a * f - c * d) / (a * e - b * d)
    let x = (c * e - b * f) / (a * e - b * d)
    return  [x,y]
}

export function system(table0, table1, table2,n){
    let matrix= new Array(new Array(2), new Array(2))
    let vector = new Array(2)

    matrix[0][0] = alpha1*table1[0][1] + betta1*table1[0][2]
    matrix[0][1] = alpha1*table2[0][1] + betta1*table2[0][2]
    vector[0] = gamma1-alpha1*table0[0][1]-betta1*table0[0][2]

    matrix[1][0] = alpha2*table1[n][1] + betta2*table1[n][2]
    matrix[1][1] = alpha2*table2[n][1] + betta2*table2[n][2]
    vector[1] = gamma2-alpha2*table0[n][1]-betta2*table0[n][2]

    let result = solver(matrix[0][0],matrix[0][1],vector[0],matrix[1][0],matrix[1][1],vector[1])
//    console.log("==========================", "\n", result)
    let resultArray = new Array(n+1)

    for(let i=0;i<n+1;i++){
        resultArray[i] = new Array(4)
    }

    for(let i=0;i<n+1;i++){
        resultArray[i][0]=table0[i][0]
        resultArray[i][1]=table0[i][1] + result[0]*table1[i][1] + result[1]*table2[i][1]
        resultArray[i][2]=table0[i][3]
        resultArray[i][3]=Math.abs(resultArray[i][2]-resultArray[i][1])
    }

    console.log('', 'Xi','\t\t','method','   \t  ','the exact',' \t\t','error')
    for(let i=0;i<n+1;i++){
        console.log(resultArray[i][0].toFixed(2),'\t',resultArray[i][1].toFixed(10),'\t',
            resultArray[i][2].toFixed(10),'\t',resultArray[i][3].toFixed(10))
    }
}