import heapq
class Twitter:

    def __init__(self):
        self.tweets = {} # userID : [(timestamp, tweetID)]
        self.following = {} # userID: {userID of the user followed in key}
        self.timestamp = 0 # acting as timestamp for tweets

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []
        
        # 1. Check if following exists AND has tweets
        if userId in self.following:
            for f_id in self.following[userId]:
                if f_id in self.tweets and self.tweets[f_id]: # Added empty check
                    tweet = self.tweets[f_id][-1]
                    # Flatten the tuple so it's (timestamp, tweetId, userId, index)
                    maxHeap.append((tweet[0], tweet[1], f_id, len(self.tweets[f_id]) - 1))
        
        # 2. Check if user themselves has tweets
        if userId in self.tweets and self.tweets[userId]: # Added empty check
            tweet = self.tweets[userId][-1]
            maxHeap.append((tweet[0], tweet[1], userId, len(self.tweets[userId]) - 1))
            
        heapq.heapify(maxHeap)
        
        while len(res) < 10 and maxHeap:
            # Now unpacking matches the flattened tuple
            time, tweetId, uId, idx = heapq.heappop(maxHeap)
            res.append(tweetId)
            if idx > 0:
                prev_tweet = self.tweets[uId][idx-1]
                heapq.heappush(maxHeap, (prev_tweet[0], prev_tweet[1], uId, idx-1))
        
        return res
        



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId: # Prevent self-following issues
            if followerId not in self.following:
                self.following[followerId] = set()
            self.following[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following or followeeId not in self.following[followerId]:
            return
        self.following[followerId].remove(followeeId)
        
