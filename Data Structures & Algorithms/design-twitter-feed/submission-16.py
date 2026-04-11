import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        # Using negative integers for timestamp to simulate a Max-Heap with Python's Min-Heap
        self.timer = 0
        self.tweets = defaultdict(list)  # userId: [(timestamp, tweetId)]
        self.following = defaultdict(set) # userId: {followeeIds}

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Most recent tweets get smaller (more negative) timestamps
        self.tweets[userId].append((self.timer, tweetId))
        self.timer -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        min_heap = []
        
        # A user always sees their own tweets
        followees = self.following[userId] | {userId}
        
        for f_id in followees:
            if f_id in self.tweets and self.tweets[f_id]:
                # Start with the latest tweet from each followee
                idx = len(self.tweets[f_id]) - 1
                time, tweetId = self.tweets[f_id][idx]
                # Store: (timestamp, tweetId, followeeId, index_of_next_tweet)
                heapq.heappush(min_heap, (time, tweetId, f_id, idx - 1))
        
        while min_heap and len(res) < 10:
            time, tweetId, f_id, next_idx = heapq.heappop(min_heap)
            res.append(tweetId)
            
            # If this user has more tweets, push the next most recent one
            if next_idx >= 0:
                nxt_time, nxt_tweetId = self.tweets[f_id][next_idx]
                heapq.heappush(min_heap, (nxt_time, nxt_tweetId, f_id, next_idx - 1))
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # .discard() is cleaner than .remove() as it doesn't raise KeyError
        if followerId in self.following:
            self.following[followerId].discard(followeeId)