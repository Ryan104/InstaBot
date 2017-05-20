#! python3
""" tag_generator.py - assembles a list of tags for an intagram post """
from random import sample

# TODO: Use google cloud platform's vision API to get accurate image tags

# TODO: build hashtag library
TAGS = {
    'outdoors_standard': [
        '#camp', '#camping', '#backpacking', '#wildernessculture', '#wilderness', '#peace',
        '#love', '#findyourpark', '#nature', '#outdoors', '#outdoorlife', '#getoutstayout',
        '#getoutside', '#optoutside', '#rei1440project', '#nps100', '#woods', '#forest',
        '#traveling', '#travel', '#follow', '#landscapes', '#mountains', '#hike', '#hiking',
        '#nationalparks', '#nps', '#trail', '#hikingaddict', '#hikingtrail', '#gohiking',
        '#joy', '#life', '#sky', '#sunrise', '#sunset', '#beautiful', '#inspiration',
        '#happy', '#beauty', '#clouds'
    ],
    'outdoors_bonus': [

    ]
}

def get_tags():
    """ assemble list of 28 random tags """
    tag_str = " ".join(sample(TAGS['outdoors_standard'], 28))
    return tag_str
