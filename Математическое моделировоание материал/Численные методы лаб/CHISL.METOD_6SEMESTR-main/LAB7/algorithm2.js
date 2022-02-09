import {p,q,f} from './functions.js'
import {kramer} from './kramer.js'

let matrix
let array

const alpha1=1
const betta1=0
const gamma1=1
const alpha2=1
const betta2=0
const gamma2=0.5

function createSystem(x,n,h){
    matrix[0][0] = alpha1-betta1/h
    matrix[0][1] = betta1/h
    array[0] = gamma1
    matrix[n-1][n-2] = -betta2/h
    matrix[n-1][n-1] = alpha2+betta2/h
    array[n-1] = gamma2

    for(let i=1;i<n-1;i++) {
        matrix[i][i-1] = 1-h/2*p(x[i])
        matrix[i][i] = -2+Math.pow(h,2)*q(x[i])
        matrix[i][i+1] = 1+h/2*p(x[i])
        array[i] = Math.pow(h,2)*f(x[i])
    }
}

export function system2(n,y0,yn,x,h){
    matrix = new Array(n)
    array = new Array(n)

    for(let i=0;i<n;i++){
        matrix[i] = new Array(n)
    }

    for(let i=0;i<n;i++){
        for(let j=0;j<n;j++){
            matrix[i][j] = 0
        }
    }
    createSystem(x,n,h)
    const result = kramer(matrix,array,n)
    return result
}