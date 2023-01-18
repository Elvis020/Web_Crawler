import logging
import re
import threading
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool
from pprint import pprint

from bs4 import BeautifulSoup

from Crawler.Utils.utilities import extract_all_web_links, decode_webpage, add_to_visited_links, get_related_pages, \
    get_non_related_pages, create_folder_for_file


class Crawler:
    def __init__(self):
        self.weblinks = dict()

    def __update_non_related_weblinks(self, links):
        """ For links not related to the domain, their values in the dictionary is [] """
        for link in links:
            self.weblinks[link] = []

    def __add_weblink(self, link, update):
        """ Adding links related to the domain to the weblinks dictionary """
        self.weblinks[link] = update

    def __gather_all_links_under_domain(self, input_url):
        """ Gathering all the weblinks """
        print('Gathering all links...')
        response = decode_webpage(input_url).read().decode("utf-8")
        soup = BeautifulSoup(response, 'html.parser')

        thread1 = ThreadPool(1).apply_async(get_related_pages, (soup.find_all('a', href=True),))
        thread2 = ThreadPool(1).apply_async(get_non_related_pages, (soup.find_all('a', href=True),))
        related_links = thread1.get()
        non_related_links = thread2.get()

        with ThreadPoolExecutor(2) as executor:
            executor.submit(self.__update_non_related_weblinks, non_related_links)

        with ThreadPoolExecutor(1) as executor:
            executor.submit(get_related_pages, (soup.find_all('a', href=True),))

        # For debugging purposes
        logging.log(msg=f'Active threads:{threading.activeCount()}', level=logging.WARN)
        logging.log(msg=f'Number of web_links:{len(self.weblinks) + 1}', level=logging.WARN)

        all_related_pages = map(lambda link: input_url + link if re.match('/+', link) else link, related_links)
        return set(filter(lambda x: x[:-1] != input_url, all_related_pages))

    def get_all_links(self, url) -> None:
        """ Uses depth-first-search(DFS) algorithm to gather the links  """
        visited_links = deque()
        visited_links.append(url)
        while visited_links:
            current_link = visited_links.pop()
            if current_link not in self.weblinks and self.__gather_all_links_under_domain(current_link):
                self.__add_weblink(current_link, self.__gather_all_links_under_domain(current_link))

                t4 = ThreadPool(6).apply_async(add_to_visited_links, (self.__gather_all_links_under_domain(current_link), visited_links,))
                t4.get()
            else:
                self.__add_weblink(current_link, [])
        get_all_links = extract_all_web_links(self.weblinks)
        return create_folder_for_file(get_all_links)
