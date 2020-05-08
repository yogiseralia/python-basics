""" this is a module doc string"""
from urllib.request import urlopen
import sys


def fetch_words(url):
    """this is a function doc string -- fetch the list of words from a URL."""
    story_words = []
    story = urlopen(url)
    for line in story:
        line_words = line.decode("utf-8").split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(story_words):
    for word in story_words:
        print(word)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(url=sys.argv[1]) # argv[0] is the module filename.
