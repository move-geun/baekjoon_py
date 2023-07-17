function solution(babbling) {
    var answer = 0;
    babblings = ['aya','ye','woo','ma']
    for (let i in babbling){
        let init = babbling[i]
        for(let j in babblings){
            if(init.includes(babblings[j])){
                init = init.replace(babblings[j], "X")
            }
        }
        init = init.replace(/X/gi,"")
        
        if(init.length === 0){
            answer += 1
        }
    } 
    return answer;
}