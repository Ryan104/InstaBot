#! python3
""" img_download.py - search for images containing the tag with the argv and download images to a
folder """

import os
import sys
import requests
from bs4 import BeautifulSoup

# TODO: turn img_download into a function that can be imported to and passed argv or any tag
# TODO: manipulate img src url to get smaller images
# TODO: take number of images desired instead of number of pages
# TODO: change file naming convention to _XX instead of XX_XX ie only use running image number count
# TODO: use pixel image index in image name

SEARCH_TERM = " ".join(sys.argv[1:])
FOLDER_NAME = "_".join(sys.argv[1:])
BASE_URL = "https://www.pexels.com/search/"
PAGE_NUM_CALL = "/?page="
FULL_SIZE_DOWNLOAD = False

os.makedirs(('.\\Images\\' + FOLDER_NAME), exist_ok=True) # create directory where images will be stored

def get_html(url):
    """ fetch html string from given URL """
    res = requests.get(url)
    res.raise_for_status()
    return res.text

def parse_images(html):
    """ parse given html string and return list of image ulrs found on page """
    print("Parsing for images...")
    image_urls = []
    image_soup = BeautifulSoup(html, 'html.parser')
    for image_tag in image_soup.select('.photo-item > a > img'):
        image_urls.append(full_image_res(image_tag.get('src')))
    print("Found %s images!" % str(len(image_urls)))
    return image_urls

def full_image_res(image_url):
    """ remove the callbacks from the image URL so the fullsize image can be retrieved
     MAYBE... use the call backs to get a more desirable image size if needed ? """
    # TODO: handle error if image_url cannot find "?"
    if FULL_SIZE_DOWNLOAD:
        return image_url[:image_url.find("?")]
    else:
        return image_url

def download(images, page):
    """ download images from array of urls to the created directory """
    if not images:
        return False # Returns false if there were no images found, will stop looking
    for i in range(0, len(images)):
        print('Downloading image #%s to ".\\%s"' % (i, FOLDER_NAME))
        # get the images with requests
        res = requests.get(images[i])
        res.raise_for_status()
        # save the image to a file in the directory created
        image_path = '.\\Images\\' + FOLDER_NAME + '\\image_' + ('%02d_%02d.jpg' % (page, i))
        image_file = open(image_path, 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
    return True # Return true if images were found, will continue to next page

def img_download(max_pages):
    """ Attempt to download x number of pages with ~15 images per page """
    more_images = True
    page = 1
    print('Searching for "%s"...' % SEARCH_TERM)
    while more_images and page <= max_pages:
        print("--PAGE %s--" % page)
        more_images = download(
            parse_images(
                get_html(BASE_URL + SEARCH_TERM + PAGE_NUM_CALL + str(page))), page)
        page += 1
    print("Reached the end of %s!" % SEARCH_TERM)

img_download(4)
