function solution(array) {
    let answer = 0;
    let max = 0; 
    let duple = false;
    
    let dict = array.reduce((acc,val)=>{
        acc[val] = (acc[val] || 0) +1;
        return acc;
    },{})
    
    
    for(let i in dict){
        if(max < dict[i]){
            answer = i*1;
            max = dict[i];
            duple = false;
        }else if(max === dict[i]){
            duple = true;
        }
    }
    
    return duple ? -1 : answer;
}