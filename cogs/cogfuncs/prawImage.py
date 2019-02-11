import praw, random

async def prawImgFind(prawDepInj,subreddit="all",sortby="top",srange="100",retries="3"):
    usableExt=["jpg","peg","png","gif"]
    usableSort=["hot","new","controversial","top","rising"]
    if sortby not in usableSort:
        return("no_sort")

    reddit=praw.Reddit(client_id=prawDepInj.clientId, client_secret=prawDepInj.clientSecret, user_agent=prawDepInj.userAgent)
    try:
        reddit.subreddits.search_by_name(subreddit, exact=True)
    except:
        return("no_sub")    

    subGet = reddit.subreddit(subreddit)
    if sortby=="best":
        posts = [post for post in subGet.best(limit=int(srange))]
    elif sortby=="new":
        posts = [post for post in subGet.new(limit=int(srange))]
    elif sortby=="controversial":
        posts = [post for post in subGet.controversial(limit=int(srange))]
    elif sortby=="top":
        posts = [post for post in subGet.top(limit=int(srange))]
    elif sortby=="rising":
        posts = [post for post in subGet.rising(limit=int(srange))]

    randTop = min(len(posts),int(srange))-1

    for i in range(0,int(retries)):
        randomPost = posts[random.randint(0,randTop)].url
        print(randomPost)
        if randomPost[-3:] in usableExt:
            return(randomPost)
        i+=1
    return("no_image")