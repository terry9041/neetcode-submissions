class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(reverse = True)
        
        stack = []

        for pair in pairs:
            if stack == []:
                stack.append(pair)
            elif ((target-pair[0])/pair[1]) > ((target-stack[-1][0])/stack[-1][1]):
                    stack.append(pair)
        
        return len(stack)