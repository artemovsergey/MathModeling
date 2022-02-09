import pack from 'ndarray-pack'
import det from 'ndarray-determinant'

function clone(a){
    return JSON.parse(JSON.stringify(a))
}

export function kramer(a,b,n) {
    let result = new Array(n)
    let M = pack(a)
    const determinant = det(M)

    for(let i=0;i<n;i++){
        let matr= clone(a)
        for (let j=0;j<n;j++) {
            matr[j][i] = b[j]
        }
        let N = pack(matr)
        result[i]=det(N)/determinant
    }
    return result
}