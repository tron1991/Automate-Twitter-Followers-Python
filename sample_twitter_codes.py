# -*- coding: utf-8 -*-


'''
Auto-Follow 40 followers of the username below
'''
from twitter_follow_bot import auto_follow
auto_follow("newyork", count=40)

from twitter_follow_bot import auto_follow
auto_follow("sanfrancisco", count=40)

'''
Auto-Follow the followers of the user below
'''

from twitter_follow_bot import auto_follow_followers_for_user
auto_follow_followers_for_user("iOSDevHelper", count=40)

'''
Unfollow any Non-Followers below
'''

'''
from twitter_follow_bot import auto_unfollow_nonfollowers
auto_unfollow_nonfollowers()
'''







