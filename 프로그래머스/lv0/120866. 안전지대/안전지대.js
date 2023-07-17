function solution(board) {
    let answer = board.length**2;
    const visited = Array.from(Array(board.length), () => Array(board.length).fill(0))
    const dist = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    for(let i =0; i<board.length; i++){
        for(let j=0; j<board.length;j++){
            if (board[i][j] === 1){
                if (visited[i][j] == 0){
                    visited[i][j] = 2
                    answer -= 1}
                for(const [a,b] of dist){
                    let ni = i + a;
                    let nj = j + b;
                    if( 0 <= ni && ni < board.length && 0 <= nj && nj < board.length  && visited[ni][nj] === 0){
                        visited[ni][nj] = 2;
                        answer -= 1
                    }
                }
            }
        }
    }
    
    
    return answer;
}