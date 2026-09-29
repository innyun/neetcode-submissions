class Twitter:

    def __init__(self):
        self.count = 0
        self.posts = defaultdict(list)
        self.users = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.posts[userId], (self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        t = []
        if userId not in self.users[userId]:
            self.users[userId].append(userId)
        for user in self.users[userId]:
            for count, tweet in self.posts[user]:
                heapq.heappush(t, (count, tweet))
        while t and len(feed) < 10:
            feed.append(heapq.heappop(t)[1])
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.users[followerId]:
            self.users[followerId].append(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        
