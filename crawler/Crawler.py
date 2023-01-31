from abc import ABC, abstractmethod


class Crawler(ABC):
    @abstractmethod
    def gather_all_weblinks(self, url):
        pass

    @abstractmethod
    def gather_links_into_file(self, url):
        pass
