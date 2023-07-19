function solution(quiz) {
    var answer = [];
    quiz.map(q => {
        const [calc, result] = q.split(" = ");
        const sign = calc.includes('+') ? 1 : -1
        const [x, y] = calc.split(sign === 1 ? ' + ' : ' - ');
        
        if(sign === 1){
            if(x*1 + y*1 === result*1){
                answer.push('O');
            } else {
                answer.push('X')
            };
            
        } else{
            if(x*1 + y*-1 === result*1){
                answer.push('O');
            } else {answer.push('X')
        }
        }
    })
    return answer;
}