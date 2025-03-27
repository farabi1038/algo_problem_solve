You are given an array of positive integers arr and an integer max_moves.

You are allowed to choose a single integer x ≥ 1. Each move subtracts x from any one element of the array.

You can apply multiple moves to any element.

You must use exactly max_moves total moves.

After all moves are applied, each element in the array must be ≤ 0.

Your goal is to find the maximum possible integer x such that:

Using exactly max_moves moves,

And subtracting x per move,

You can reduce all elements of the array to zero or below.

🧠 Rules:
Every move subtracts x from one element.

You may apply multiple moves to one element.

The number of moves must be exactly equal to max_moves

Every element must become ≤ 0 by the end.

You must find the maximum possible x that satisfies this.


import math

def max_x_exact_moves(arr, max_moves):
    low, high = 1, max(arr)
    answer = -1

    while low <= high:
        mid = (low + high) // 2
        moves_used = sum(math.ceil(a / mid) for a in arr)

        if moves_used == max_moves:
            answer = mid
            low = mid + 1  # try to find a bigger x
        elif moves_used < max_moves:
            high = mid - 1  # too few moves, x is too big
        else:
            low = mid + 1  # too many moves, x is too small

    return answer
