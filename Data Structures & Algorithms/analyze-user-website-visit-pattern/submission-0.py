class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        zipped = sorted(zip(timestamp, username, website))
        users = {}
        for time, user, page in zipped:
            if user in users:
                users[user].append(page)
            else:
                users[user] = [page]
        pattern_count = {}
        for user in users:
            n = len(users[user])
            if n < 3:
                continue
            user_pattern = set()
            for i in range(n):
                for j in range(i+1, n):
                    for k in range(j+1,n):
                        pattern = (users[user][i], users[user][j], users[user][k])
                        user_pattern.add(pattern)
            for pattern in user_pattern:
                pattern_count[pattern] = pattern_count.get(pattern, 0) + 1
            
        max_score = 0
        res = None

        for pattern in sorted(pattern_count.keys()):
            if pattern_count[pattern] > max_score:
                res = pattern
                max_score = pattern_count[pattern]
        
        return list(res)

        
        


        