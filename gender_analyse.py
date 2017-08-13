# coding: utf-8

import re
import os

import twitter
import gender_guesser.detector as gender

api = twitter.Api(
    consumer_key=os.getenv('CONSUMER_KEY'),
    consumer_secret=os.getenv('CONSUMER_SECRET'),
    access_token_key=os.getenv('TOKEN'),
    access_token_secret=os.getenv('TOKEN_SECRET'),
)

users = api.GetFriends()
names = [u.name for u in users]

# Strips emoji from the names:
emoji_pattern = re.compile("["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           r"⭐🦄🤖☭⚠\(\)Ⓥ☁️✨]+", flags=re.UNICODE)

# Extract the first word as best we can from each name:
fn = [emoji_pattern.sub(' ', name).strip().split(' ', 1)[0].title() for name in names]

d = gender.Detector()

# Build a list of (name, gender) tuples:
genders = [(n, d.get_gender(n)) for n in fn]

# Summarize the gender data:
from collections import Counter
stats = Counter([g[1] for g in genders])
print(stats)

# Rough percentage of female of "known" total:
print (stats['female'] / (stats['male'] + stats['female']) * 100, "% women vs. women + men")


# In[ ]:
