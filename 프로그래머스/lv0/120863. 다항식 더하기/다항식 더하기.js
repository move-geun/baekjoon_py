function solution(polynomial) {
    var answer = '';
    const arr = polynomial.split(" + ");
    let poly = 0;
    let num = 0;
    
    for(let i in arr){
        if(arr[i].includes("x")){
            if(arr[i] === 'x'){
                poly += 1
            }else poly += (arr[i].replace('x',''))*1;
        }else num += (arr[i])*1;
    }

    if(poly && num){
        if(poly===1){
            return "x + "+num;
        } return poly+"x + "+num;
    }else if(poly && num ===0){
        if(poly===1){
            return "x";
        } return poly+"x";
    }else if(poly === 0 && num){
        return String(num);
    }else return 0;
}