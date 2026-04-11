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
        if userId in self.following:
            for followingId in self.following[userId]:
                if followingId in self.tweets:
                    maxHeap.append(((self.tweets[followingId][-1]), followingId, len(self.tweets[followingId])-1))
        if userId in self.tweets:
            maxHeap.append(((self.tweets[userId][-1]), userId, len(self.tweets[userId])-1))
        heapq.heapify(maxHeap)
        while len(res) < 10 and maxHeap:
            (_, tweetId), userId, idx = heapq.heappop(maxHeap)
            res.append(tweetId)
            if idx > 0:
                heapq.heappush(maxHeap,((self.tweets[userId][idx-1]), userId, idx-1))
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
        
