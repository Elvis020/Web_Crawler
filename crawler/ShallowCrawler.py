from bs4 import BeautifulSoup
from crawler import *
from crawler.Crawler import Crawler


class ShallowCrawler(Crawler):
    def gather_all_weblinks(self, input_url):
        """Gathering all the weblinks"""
        print('Gathering all links...')
        response = decode_webpage(input_url).read().decode("utf-8")
        soup = BeautifulSoup(response, 'html.parser')
        related_links, non_related_links = gather_links(soup)

        # For debugging purposes
        # logging.log(msg=f'Active threads:{threading.activeCount()}', level=logging.WARN)
        # logging.log(msg=f'Number of web_links:{len(self.weblinks) + 1}', level=logging.WARN)

        related_links = set(map(lambda link: f"{input_url}/{link}", related_links))
        return related_links, non_related_links

    def gather_links_into_file(self, url):
        """Calls the function that creates a file for storing the results"""
        related, unrelated = self.gather_all_weblinks(url)
        all_links = related.union(unrelated)
        return create_file_for_storing_results(all_links)
