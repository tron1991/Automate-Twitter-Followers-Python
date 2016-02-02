# Automate Twitter Followers 

**Automate your Twitter feed** using Python to grow Twitter Following.

## Preview
![screencast](http://g.recordit.co/qxNIF2plXI.gif)

## How to Install Scripts

1) Download the existing code from this repo.

2) Make a Twitter Account to gain access to Twitter for Developers([https://dev.twitter.com](https://dev.twitter.com))

3) In the Twitter Developer Account, create an app and generate 4 tokens. You will need Consumer Key, Consumer Secret, Access Token, Access Token Secret.

4) When you have the 4 keys, place them inside the twitter_info.py along with your Twitter handle.

5) Now you can change specifc keywords to follow sample_twitter_codes.py like below. 

6) To follow a keyword, change this

```ruby
from twitter_follow_bot import auto_follow
auto_follow("newyork", count=40)

```

7) To follow a person's following, change this
```ruby
from twitter_follow_bot import auto_follow_followers_for_user
auto_follow_followers_for_user("iOSDevHelper", count=40)

```

##How to Use the Script

To use the script, simply go to the folder where you placed all your python files and tokens in terminal. When you are in the directory run the script in your terminal.  

```ruby
python sample_twitter_codes.py
```
Based on your settings in this file, you can follow, unfollow followers to your twitter account.

##Python

**Automate Twitter Followers** is implemented in **Python**.


## Creator

Nicholas Ivanecky ([@ivantr0n](http://twitter.com/ivantr0n)), To visit all my works visit ([www.ivantron.com](http://www.ivantron.com))
