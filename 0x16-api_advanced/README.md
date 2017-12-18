<h1 class="gap">0x16. API advanced</h1>


<h4 class="task">
    0. How many subs?
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a function that queries the Reddit API (https://www.reddit.com/dev/api/) and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.</p><p>Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.</p><p>Requirements:</p><ul>
<li>Prototype: <code>def number_of_subscribers(subreddit)</code></li>
<li>If not a valid subreddit, return 0.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
</ul>


<h4 class="task">
    1. Top Ten
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a function that queries the Reddit API (https://www.reddit.com/dev/api/) and prints the titles of the first 10 hot posts listed for a given subreddit.</p><p>Requirements:</p><ul>
<li>Prototype: <code>def top_ten(subreddit)</code></li>
<li>If not a valid subreddit, print None.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
</ul>


<h4 class="task">
    2. Recurse it!
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a <em>recursive function</em> that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.</p><p>Hint: The Reddit API uses pagination for separating pages of responses.</p><p>Requirements:</p><ul>
<li>Prototype: <code>def recurse(subreddit, hot_list=[])</code></li>
<li>Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a starting value in the main.</li>
<li>If not a valid subreddit, return None.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
</ul><p>Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)</p>

