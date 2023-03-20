import sys
import urllib
from urllib import request, parse
from urllib.parse import urlparse, urljoin
from urllib.request import Request
from html.parser import HTMLParser
from collections import deque

# This wonderful script comes courtesy of Andrew Healey (full script available [here](https://github.com/healeycodes/Broken-Link-Crawler/blob/master/deadseeker.py))

search_attrs = set(['href', 'src'])
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'

class LinkParser(HTMLParser):
    def __init__(self, home, verbose):
        super().__init__()
        self.home = home
        self.verbose = verbose
        self.checked_links = set()
        self.pages_to_check = deque()
        self.pages_to_check.appendleft(home)
        self.scanner()

    def scanner(self):
        while self.pages_to_check:
            page = self.pages_to_check.pop()
            req = Request(page, headers={'User-Agent': agent})
            res = request.urlopen(req)

            if 'html' in res.headers['content-type']:
                with res as f:
                    body = f.read().decode('utf-8', errors='ignore')
                    self.feed(body)

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
        # ('href', 'https://google.com')
            if attr[0] in search_attrs and attr[1] not in self.checked_links:
                self.checked_links.add(attr[1])
                self.handle_link(attr[1])

    def handle_link(self, link):
        # check for a relative link (e.g. /about/, /blog/)
        if not bool(urlparse(link).netloc):

            # fix if we need to, we can't send a request to `/about/`
            link = urljoin(self.home, link)

        # attempt to send a request, seeking the HTTP status code
        try:
            req = Request(link, headers={'User-Agent': agent})
            status = request.urlopen(req).getcode()

        # we're expecting errors (dead resources) so let's handle them
        except urllib.error.HTTPError as e:
            print(f'HTTPError: {e.code} - {link}')  # (e.g. 404, 501, etc)
        except urllib.error.URLError as e:
            print(f'URLError: {e.reason} - {link}')  # (e.g. conn. refused)

        # otherwise, we got a 200 (OK) or similar code!
        else:

            # remove this in production or we won't spot our errors
            print(f'{status} - {link}')

        # build a queue of local pages so we crawl the entire website
        if self.home in link:
            self.pages_to_check.appendleft(link)

home_url = r'https://kspicer80.github.io/kspicer_ptrr/ptrr.html'
r = urllib.request.urlopen('https://kspicer80.github.io/kspicer_ptrr/ptrr.html')
print(r.status)

verbose = len(sys.argv) > 2 and sys.argv[2] == 'v'
LinkParser(home_url, verbose)

