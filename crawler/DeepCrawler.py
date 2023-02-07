from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from crawler import *
from crawler.Crawler import Crawler


def extract_all_web_links(dictionary_of_links: dict, num_of_threads):
    """Gathers a dictionary of links into a set"""
    final_list_of_links = set()
    thread = ThreadPool(num_of_threads // 2).apply_async(combine_dictionary_keys_and_values,
                                                        (dictionary_of_links, final_list_of_links,))
    return set(thread.get())


class DeepCrawler(Crawler):
    def __init__(self, num_of_threads=5):
        super().__init__(num_of_threads=num_of_threads)

    def add_non_related_links_to_weblinks(self, links):
        """Add non-related links with values=[] to the weblinks dictionary"""
        for link in links:
            self.weblinks[link] = []

    def add_related_weblinks(self, link, update):
        """Add related links to the weblinks dictionary"""
        self.weblinks[link] = update

    def map_weblinks(self, input_url):
        """Gathering all the weblinks"""
        print('Gathering all links...')
        response = decode_webpage(input_url).read().decode("utf-8")
        soup = BeautifulSoup(response, 'html.parser')

        related_links, non_related_links = gather_links(soup, self.num_of_threads)

        with ThreadPoolExecutor(max_workers=self.num_of_threads // 2) as executor:
            executor.submit(self.add_non_related_links_to_weblinks, non_related_links)

        # For debugging purposes
        # logging.log(msg=f'Active threads:{threading.activeCount()}', level=logging.WARN)
        # logging.log(msg=f'Number of web_links:{len(self.weblinks) + 1}', level=logging.WARN)

        all_related_pages = map(lambda link: input_url + '/' + link, related_links)
        return set(filter(lambda x: x[:-1] != input_url, all_related_pages))

    def get_all_links(self, url):
        """Uses depth-first-search(DFS) algorithm to gather the links"""
        visited_links = [url]
        while visited_links:
            current_link = visited_links.pop()
            if current_link not in self.weblinks and self.map_weblinks(current_link):
                self.add_related_weblinks(current_link, self.map_weblinks(current_link))

                threadpool_for_gathering_links = ThreadPool(self.num_of_threads).apply_async(add_to_visited_links,
                                                                                 (self.map_weblinks(current_link), visited_links,))
                threadpool_for_gathering_links.get()
            elif current_link not in self.weblinks:
                self.add_related_weblinks(current_link, [])
        return extract_all_web_links(self.weblinks, self.num_of_threads)

    def gather_links_into_file(self, input_url):
        """Calls the function that creates a file for storing the results"""
        self.get_all_links(input_url)
        return create_file_for_storing_results(self.weblinks)