function solution(ingredient) {
    var answer = 0;
    let arr=[]

    
      for (let i of ingredient) {
      arr.push(i);
    if (arr.slice(-4).join('') == '1231') {
      arr.splice(-4);
      answer++;
    }
  }

    return answer;
}