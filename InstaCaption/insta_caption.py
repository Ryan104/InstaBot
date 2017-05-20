#! python3
""" insta_caption.py - creates a caption with tags for instagram posts """

from caption_generator import get_bible_verse
from tag_generator import get_tags
import pyperclip

def insta_caption():
    """ return a random caption and tag set using the bible verse and outdoor tags modules """
    # TODO: paset caption to clipboard
    caption = '%s\n.\n.\n.\n%s' % (get_bible_verse(), get_tags())
    pyperclip.copy(caption)
    return caption
