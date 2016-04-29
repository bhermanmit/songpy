"""
Project is used to download youtube video into an m4a file and set ID3 tags.
"""
import sys
import urllib2
import re


def main():
    """Main entry point for project."""
    response = urllib2.urlopen('http://youtube.com/')
    html = response.read()
    

    print html
    pass

if __name__ == '__main__':
    sys.exit(main())
