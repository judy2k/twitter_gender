# Gender Analyse

This is a *very* quick script I threw together, originally as a Jupyter Notebook.
The approach was based on that
[described](https://dzone.com/articles/how-to-analyze-your-twitter-followers-by-gender)
by A. Jesse Jiryu Davis. I've switched out the `sexmachine` library for
`gender-guesser` because that runs on Python 3.

Please feel free to use this script on your own account. I'm sharing it in the
hope that it will help others address their own Twitter bubbles. It's not good
to only hear opinions from people who think like you!

## Installation

You'll need Python 3 - I used Python 3.6.
Clone this repo, create a virtualenv, and run `pip install -r requirements.txt`

## Running It

You need to create a [Twitter App](https://apps.twitter.com/). Get your
consumer key & secret, and your access token & secret. Set the following
environment variables with these values:

* CONSUMER_KEY
* CONSUMER_SECRET
* TOKEN
* TOKEN_SECRET

Now run the script:

```bash
python gender_analyse.py
```

The script will print out some rough stats. If you want to do more with the
data, you should hack the script!

## Spelling

'Analyse' is the British spelling of 'Analyze' - it's not a typo!

:heart:
