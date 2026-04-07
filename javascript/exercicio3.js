const fibonacci = (x) => {
    if (x==0 || x==1)
        return 1;
    let fm1 = 1, fm2 = 1, fm; // let é uma variável, igual const ou var. só serve pra definir
    for (let i=2; i<x; i++){ //  incrementando
        fm = fm1 + fm2;
        fm2 = fm1; // aqui o fm2 vira fm1
        fm1 = fm; // aqui o fm1 vira fm
    }
    return fm;
}
const fiboRec = (x) => {
    return (x==0 || x==1)? 1 : fiboRec(x-1) + fiboRec(x-2);
} 