export function system1f(x,y,z){
    return z
}

export function system1g(x,y,z){
    return 2/Math.pow(1+x,3)+y+z*(1+x)
}

export function system2f(x,y,z){
    return z
}

export function system2g(x,y,z){
    return y+z*(1+x)
}

export function system3f(x,y,z){
    return z
}

export function system3g(x,y,z){
    return y+z*(1+x)
}

export function exact(x,y,z){
    return 1/(1+x)
}

//////////////////////////////////////////////

export function p(x){
    return -1-x
}

export function q(x){
    return -1
}

export function f(x){
    return 2/Math.pow(1+x,3)
}