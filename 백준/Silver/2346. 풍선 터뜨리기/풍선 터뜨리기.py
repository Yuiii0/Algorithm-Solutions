import sys
from collections import deque
input = sys.stdin.readline

# Read input
n = int(input())
notes = list(map(int, input().strip().split()))

# Initialize the deque with (balloon number, note) tuples
deck = deque((i + 1, note) for i, note in enumerate(notes))

result = []

# Start with the first balloon
cur = 0

while deck:
    balloon, move = deck.popleft()
    result.append(balloon)
    
    # No need to move if the deck is empty
    if not deck:
        break

    if move > 0:
        move -= 1  # Adjust move for right movements

    # Move to the next balloon
    deck.rotate(-move)

# Print the result
print(' '.join(map(str, result)))
