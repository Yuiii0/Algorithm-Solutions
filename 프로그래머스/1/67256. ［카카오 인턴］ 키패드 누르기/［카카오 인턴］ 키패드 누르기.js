const solution = (numbers, hand) => {
  let answer = '';

  let leftPosition = '*';
  let rightPosition = '#';

  const getDistance = (LRposition, target) => {
    const keypad = {
      1: [0, 0], 2: [0, 1], 3: [0, 2],
      4: [1, 0], 5: [1, 1], 6: [1, 2],
      7: [2, 0], 8: [2, 1], 9: [2, 2],
      '*': [3, 0], 0: [3, 1], '#': [3, 2],
    };
    const nowPosition = keypad[LRposition];
    const targetPosition = keypad[target];
    return Math.abs(targetPosition[0] - nowPosition[0]) + Math.abs(targetPosition[1] - nowPosition[1]);
  };

  for (let number of numbers) {
    // 왼쪽
    if (number === 1 || number === 4 || number === 7) {
      answer += 'L';
      leftPosition = number;
      continue
    }
    // 오른쪽
    else if (number === 3 || number === 6 || number === 9) {
      answer += 'R';
      rightPosition = number;
      continue
    }
    // 가운데(계산)
    else {
      // 거리 계산(함수)
      const leftDistance = getDistance(leftPosition, number);
      const rightDistance = getDistance(rightPosition, number);
      // 거리가 동일할 때
      if (leftDistance === rightDistance) {
        if (hand === "left") {
          answer += 'L';
          leftPosition = number;
            continue
        } else {
          answer += 'R';
          rightPosition = number;
            continue
        }
      }
      // 왼쪽이 더 가까울 때
      else if (leftDistance < rightDistance) {
        answer += 'L';
        leftPosition = number;
          continue
      }
      // 오른쪽 더 가까울 때
      else {
        answer += 'R';
        rightPosition = number;
          continue
      }
    }
  }
  return answer;
}
