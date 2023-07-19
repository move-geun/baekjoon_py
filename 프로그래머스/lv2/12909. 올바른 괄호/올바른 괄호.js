function solution(s){
    var answer = true;
    let tmp = [];
    
    for(let i=0; i<s.length; i++){
        if(s[i] === '\('){
            tmp.push(s[i]);
        }else{
            if(tmp.length>0) tmp.pop();
            else return false;
        }
    }
    if(tmp.length > 0) return false;
    return answer;
}