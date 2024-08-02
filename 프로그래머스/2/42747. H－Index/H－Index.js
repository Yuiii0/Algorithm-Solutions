function solution(citations) {
    let i=0;
    
    citations.sort((a,b)=>b-a);
    
    while(citations[i]>=i+1){
        i++;
    }
    return i
    
}