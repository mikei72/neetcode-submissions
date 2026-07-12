class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.appendleft((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        count = 0

        for t in self.tweets:
            if t[0] == userId or (userId in self.follows and t[0] in self.follows[userId]):
                count += 1
                res.append(t[1])
                if count == 10:
                    break
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
