function solution(people, limit) {
    var answer = 0;
    
    people.sort((a,b)=>a-b);
    
    while(people.length>0){
        let big=people.pop();
        if(big+people[0]<=limit){
            people.shift()
        }
        answer++
    }
    
    return answer;
}