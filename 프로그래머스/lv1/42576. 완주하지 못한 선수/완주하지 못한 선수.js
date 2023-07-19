function solution(participant, completion) {
    var answer = '';
    
    let par_arr = participant.reduce((arr,val)=>{
       arr[val] = (arr[val] || 0) +1;
        return arr;
    },{})
    
    completion.map(c =>{
        par_arr[c] -= 1;
    })
    
    for(let i in par_arr){
        if(par_arr[i]){
            answer += i;
        }
    }
    
    
    return answer;
}