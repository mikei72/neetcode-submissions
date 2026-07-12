class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweetMap = defaultdict(deque)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweetMap[userId].append((self.count, tweetId))
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []

        self.follows[userId].add(userId)
        for f in self.follows[userId]:
            if f in self.tweetMap:
                index = len(self.tweetMap[f]) - 1
                count, tweetId = self.tweetMap[f][index]
                heapq.heappush(heap, [count, tweetId, f, index - 1])

        while heap and len(res) < 10:
            count, tweetId, f, index = heapq.heappop(heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[f][index]
                heapq.heappush(heap, [count, tweetId, f, index - 1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
