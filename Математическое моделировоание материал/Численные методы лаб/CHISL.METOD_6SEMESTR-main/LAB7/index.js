import {showTableSystem, fillTableSystem} from './rungeKutty.js'
import * as functions from './functions.js'
import {system} from './algorithm.js'
import {system2} from './algorithm2.js'

const a = 0
const b = 1
const h = 0.1

const n = (b-a)/h+1

let table0 = fillTableSystem(a,h,n,functions.system1f,functions.system1g,functions.exact,0,0)
let table1 = fillTableSystem(a,h,n,functions.system2f,functions.system2g,functions.exact,1,0)
let table2 = fillTableSystem(a,h,n,functions.system3f,functions.system3g,functions.exact,0,1)

showTableSystem(a,h,n,functions.system1f,functions.system1g,functions.exact,0,0)
showTableSystem(a,h,n,functions.system2f,functions.system2g,functions.exact,1,0)
showTableSystem(a,h,n,functions.system3f,functions.system3g,functions.exact,0,1)

system(table0, table1, table2, n-1)
//console.log('=======================================================')
//
//const a2 = 0
//const b2 = 0.5
//const h2 = 0.1
//const n2 = (b-a)/h+1
//
//let x = new Array(n2)
//
//for(let i=0;i<n2;i++){
//    x[i] = a2+i*h2
//}
//
//let result = system2(n,0,1,x,h)
//let exact = new Array(n)
//
//for(let i=0;i<n;i++){
//    exact[i] = functions.exact(x[i])
//}
//
//console.log('method','\t','the exact','\t','error')
//for(let i=0;i<n;i++){
//    console.log(result[i].toFixed(2),'\t\t',exact[i].toFixed(10),'\t',
//        Math.abs(exact[i]-result[i]).toFixed(10))
//}