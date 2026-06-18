class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                popped_idx = stack.pop()
                output[popped_idx] = i - popped_idx

            stack.append(i)

        return output


"""
We loop through the array and track elements to the left that haven't been slimed yet:

- i = 0 (30): Cannot slime anything because it's first.
  Active left elements: [30 (idx 0)]

- i = 1 (38): Larger than 30. Thus, 30 is slimed and leaves
  Calculation: idx_38 - idx_30 -> 1 - 0 = 1. So result[idx_30] = 1.
  Active left elements: [38 (idx 1)]

- i = 2 (30): Not larger than 38. Move on.
  Active left elements: [38 (idx 1), 30 (idx 2)]

- i = 3 (36): Larger than the 30 adjacent to it. That 30 is slimed and leaves!
  Calculation: idx_36 - idx_30 -> 3 - 2 = 1. So result[idx_30] = 1.
  Next on the left is 38. 36 is not larger than 38. Move on.
  Active left elements: [38 (idx 1), 36 (idx 3)]

- i = 4 (35): Not larger than 36. Move on.
  Active left elements: [38 (idx 1), 36 (idx 3), 35 (idx 4)]

- i = 5 (40): Mega slime session! 40 is larger than everything remaining to its left:
  1) Slimes 35: idx_40 - idx_35 -> 5 - 4 = 1. So result[4] = 1.
  2) Slimes 36: idx_40 - idx_36 -> 5 - 3 = 2. So result[3] = 2.
  3) Slimes 38: idx_40 - idx_38 -> 5 - 1 = 4. So result[1] = 4.
  Active left elements: [40 (idx 5)]

- i = 6 (28): Not larger than 40. Move on.
  Active left elements: [40 (idx 5), 28 (idx 6)]

40 and 28 never found anything larger to slime them, so they stay 0
result = [1, 4, 1, 2, 1, 0, 0]
"""