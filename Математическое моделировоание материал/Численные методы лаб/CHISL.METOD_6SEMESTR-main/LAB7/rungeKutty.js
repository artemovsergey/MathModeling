function fillTable(start, h, n, foo, fooExact, y0){
    let data = new Array(n)

    for(let i=0;i<n;i++){
        data[i]=new Array(8)
    }

    for(let i=0;i<n;i++){
        data[i][0] = start + i*h
        if(i === 0){
            data[i][1]=y0
            data[i][3]=0
            data[i][4]=0
            data[i][5]=0
            data[i][6]=0

        } else {
            let k1=foo(data[i-1][0],data[i-1][1])
            let k2=foo(data[i-1][0]+h/2,data[i-1][1]+h/2*k1)
            let k3=foo(data[i-1][0]+h/2,data[i-1][1]+h/2*k2)
            let k4=foo(data[i-1][0]+h,data[i-1][1]+h*k3)

            data[i][1]=data[i-1][1]+(1/6)*h*(k1+2*k2+2*k3+k4)
            data[i][3]=k1;
            data[i][4]=k2;
            data[i][5]=k3;
            data[i][6]=k4;
        }
        data[i][2] = fooExact(start + h * i)
        data[i][7]=Math.abs(data[i][1]-data[i][2])
    }
    return data
}

export function showTable(start, h, n, foo, fooExact, yo){
    const data = fillTable(start, h, n, foo, fooExact, yo)

    console.log('====================Method Runge-Kutty====================')
    console.log('Xi', '\t', 'Yi', '\t\t', 'Y exact', '\t', 'k1', '\t\t', 'k2', '\t\t', 'k3', '\t\t', 'k4', '\t\t', 'error')
    for(let i=0;i<n;i++){
        console.log(data[i][0].toFixed(2), '\t', data[i][1].toFixed(10), '\t', data[i][2].toFixed(10), '\t',
            data[i][3].toFixed(10), '\t', data[i][4].toFixed(10), '\t', data[i][5].toFixed(10), '\t',
            data[i][6].toFixed(10), '\t', data[i][7].toFixed(10))
    }
}

export function fillTableSystem(start, h, n, fooF, fooG, fooExact, y0, z0){
    let data = new Array(n)

    for(let i=0;i<n;i++){
        data[i]=new Array(13)
    }

    for(let i=0;i<n;i++){
        data[i][0] = start + i*h
        if(i === 0){
            data[i][1]=y0
            data[i][2]=z0

            data[i][4]=0
            data[i][5]=0
            data[i][6]=0
            data[i][7]=0

            data[i][8]=0
            data[i][9]=0
            data[i][10]=0
            data[i][11]=0

        } else {
            let k1=fooF(data[i-1][0],data[i-1][1],data[i-1][2])
            let l1=fooG(data[i-1][0],data[i-1][1],data[i-1][2])

            let k2=fooF(data[i-1][0]+h/2,data[i-1][1]+h/2*k1,
                data[i-1][2]+h/2*l1)
            let l2=fooG(data[i-1][0]+h/2,data[i-1][1]+h/2*k1,
                data[i-1][2]+h/2*l1)

            let k3=fooF(data[i-1][0]+h/2,data[i-1][1]+h/2*k2,
                data[i-1][2]+h/2*l2)
            let l3=fooG(data[i-1][0]+h/2,data[i-1][1]+h/2*k2,
                data[i-1][2]+h/2*l2)

            let k4=fooF(data[i-1][0]+h,data[i-1][1]+h*k3,
                data[i-1][2]+h*l3)
            let l4=fooG(data[i-1][0]+h,data[i-1][1]+h*k3,
                data[i-1][2]+h*l3)

            data[i][1]=data[i-1][1]+(1/6)*h*(k1+2*k2+2*k3+k4)
            data[i][2]=data[i-1][2]+(1/6)*h*(l1+2*l2+2*l3+l4)

            data[i][4]=k1;
            data[i][5]=k2;
            data[i][6]=k3;
            data[i][7]=k4;

            data[i][8]=l1;
            data[i][9]=l2;
            data[i][10]=l3;
            data[i][11]=l4;
        }
        data[i][3]=fooExact(start + h * i)
        data[i][12]=Math.abs(data[i][1]-data[i][3]);
    }
    return data
}

export function showTableSystem(start, h, n, fooF, fooG, fooExact, y0, z0){
    const data = fillTableSystem(start, h, n, fooF, fooG, fooExact, y0, z0)

    console.log('====================System method Runge-Kutty====================')
    console.log('Xi', '\t', 'Yi', '\t', 'Zi', '\t'/*, 'exact', '   ', 'k1', '   ', 'k2', '    ', 'k3', '     ', 'k4', '     ',
        'l1', '     ', 'l2', '     ', 'l3', '     ', 'l4', '   ', 'error'*/)
    for(let i=0;i<n;i++){
        console.log(data[i][0].toFixed(2), data[i][1].toFixed(6), data[i][2].toFixed(6)/*,
            data[i][3].toFixed(6), data[i][4].toFixed(6), data[i][5].toFixed(6),
            data[i][6].toFixed(6), data[i][7].toFixed(6), data[i][8].toFixed(6),
            data[i][9].toFixed(6), data[i][10].toFixed(6), data[i][11].toFixed(6),
            data[i][12].toFixed(6)*/)
    }
}