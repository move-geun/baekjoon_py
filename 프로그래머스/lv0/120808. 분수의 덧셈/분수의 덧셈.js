function solution(numer1, denom1, numer2, denom2) {
    var answer = [];
    let num = numer1*denom2 + numer2*denom1;
    let denom = denom1*denom2;
    let tmp = gcd(num, denom);
    
    return [num/tmp, denom/tmp];
}

function gcd(a,b){
    return a%b==0 ? b : gcd(b,a%b)
}