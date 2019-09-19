# 0x16-api_advanced

![N|Solid](https://4.bp.blogspot.com/-wVSij9rfStg/XG7iQvHUqpI/AAAAAAAAGwI/Eol6oonV49k6QgizI6nquU373QVBhxGigCLcBGAs/s1600/image1.png)

### Background Context

Questions involving APIs are common for interviews. Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’, sometimes they require you to use recursive functions and format/sort the results.

A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.

### Task

| Task name | Description |
| --- | --- |
| 0. How many subs?  | Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0. |
| 1. Top Ten | Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit. |
| 2. Recurse it! | Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None. |
| 3. Count it! | Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not). |