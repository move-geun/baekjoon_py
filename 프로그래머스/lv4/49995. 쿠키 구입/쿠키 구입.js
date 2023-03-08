function solution(cookie) {
    var answer = 0;
    let box = cookie.length;

    // 이분탐색 지점설정
    for (let i=0; i<box-1; i++){
        let old = i;
        let young = i+1;
        let oldsum = cookie[old];
        let youngsum = cookie[young];

        // 값 비교
        while(true){
            if (oldsum == youngsum && answer < oldsum){
                answer = oldsum;
            } else if (oldsum <= youngsum && old !== 0){
                oldsum += cookie[--old];
            } else if (youngsum <= oldsum && young !== box-1){
                youngsum += cookie[++young];
            } else{
                break;
            }
        }
    }

    return answer;
}