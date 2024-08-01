function solution(progresses, speeds) {
    var answer = [];
  
    //1. 작업일 배열 생성
    const work=progresses.map((v,i)=>Math.ceil((100-v)/speeds[i]));
    //2. 순회

    let deploy=work[0];
    let count=0;
    
    for(let i=0;i<work.length;i++){
        
        if(work[i]>deploy){
            answer.push(count);
            count=0;
            deploy=work[i];
        }
        count++;
    }
    answer.push(count); //마지막 요소 push
    return answer;

}