function solution(clothes) {
    var answer = 1;
    const cloth = clothes.reduce((arr,val)=>{
        arr[val[1]] = (arr[val[1]] || 1) + 1;
        return arr;
    },{})
    
    for(let i in cloth){
        answer *= cloth[i];
    }
    return answer - 1;
}