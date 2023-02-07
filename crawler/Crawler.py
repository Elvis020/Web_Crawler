from abc import ABC, abstractmethod


class Crawler(ABC):
    def __init__(self, num_of_threads):
        self.num_of_threads = num_of_threads
        self.weblinks = dict()

    @abstractmethod
    def map_weblinks(self, url):
        pass

    @abstractmethod
    def gather_links_into_file(self, url):
        pass