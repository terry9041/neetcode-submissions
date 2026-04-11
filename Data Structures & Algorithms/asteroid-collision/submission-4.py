class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for i in range(1, len(asteroids)):
            stack.append(asteroids[i])
            while len(stack) > 1:
                a1 = stack[-1]
                a2 = stack[-2]
                if (a2 > 0 and a1 > 0) or (a2 < 0 and a1 < 0) or (a2 < 0 and a1 > 0):
                    break
                stack.pop()
                stack.pop()
                if abs(a1) == abs(a2):
                    continue
                else:
                    stack.append(a1 if abs(a1) > abs(a2) else a2)
        return stack
