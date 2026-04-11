from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # 1. sort raw data by time and user
        # format: [(time,username,website)]
        data = sorted(zip(timestamp,username,website))

        # 2. process data into user visit history dict
        # format: username: [website]
        users = defaultdict(list)
        for _, username, website in data:
            users[username].append(website)

        # 3. count frequency of patterns
        # format: pattern (tuple of 3 strings): freq (int)
        pattern_count = defaultdict(int)
        for user, history in users.items():
            n = len(history)
            if n < 3:
                continue
            user_patterns = set()
            for i in range(n):
                for j in range(i+1,n):
                    for k in range(j+1,n):
                        user_patterns.add((history[i],history[j],history[k]))
            for pattern in user_patterns:
                pattern_count[pattern] += 1
        
        # 4. find the most freq pattern
        return list(min(pattern_count.keys(), key = lambda x : (-pattern_count[x], x)))
