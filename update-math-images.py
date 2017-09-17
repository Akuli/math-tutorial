#!/usr/bin/env python3
# update the gifs in images/math and the markdown files that use them
#
# this downloads images from latex2png.com and it doesn't work 100% of
# the time, run the script again if the downloading fails
import glob
import hashlib
import os
import re
import shutil
import sys
import urllib.request     # because i can


MATH_REGEX = re.compile(r'!\[math:(.+?)\]\[\]')
LINK_LIST_REGEX = re.compile(
    r'^\[math:.+\]: images/math/[0-9a-f]{32}.gif$', re.MULTILINE)


# the images need to be downloaded because the latex2png server seems to
# be so slow that images linked from it don't work on github
def download_image(math):
    md5 = hashlib.md5(math.encode('utf-8')).hexdigest()
    path = os.path.join('images', 'math', md5 + '.gif')
    if os.path.exists(path):
        return path

    url = 'https://latex.codecogs.com/gif.latex?' + math.replace(' ', '&space;')
    print("Downloading", url, "to", path, "...")

    response = urllib.request.urlopen(url)
    with open(path, 'wb') as file:
        shutil.copyfileobj(response, file)

    return path


def update_link_list(content, used_filenames):
    content = LINK_LIST_REGEX.sub('', content).rstrip() + '\n'

    maths = MATH_REGEX.findall(content)
    if not maths:
        return content

    lines = []
    for math in maths:
        filename = download_image(math)
        used_filenames.add(filename)
        lines.append('[math:%s]: %s' % (math, filename.replace(os.sep, '/')))

    return content + '\n' + '\n'.join(lines) + '\n'


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    image_paths = set()
    for filename in glob.glob('*.md'):
        with open(filename, 'r') as file:
            old_content = file.read()

        new_content = update_link_list(old_content, image_paths)
        if new_content == old_content:
            print("Already OK:", filename)
        else:
            print("Updating", filename, "...")
            with open(filename, 'w') as file:
                file.write(new_content)

    # delete md5 named images that aren't needed anymore
    for filename in os.listdir(os.path.join('images', 'math')):
        path = os.path.join('images', 'math', filename)
        if path not in image_paths:
            print("Deleting", path)
            os.remove(path)


if __name__ == '__main__':
    main()
