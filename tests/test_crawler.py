import os
import pytest

from pathlib import Path

from crawler.ShallowCrawler import ShallowCrawler


class TestCrawler:
    @pytest.fixture
    def crawler(self):
        return ShallowCrawler(), 'https://turntabl.io'

    def test_gather_all_links_under_domain(self, crawler):
        crawler, domain = crawler
        related_links, _ = crawler.map_weblinks(domain)
        assert 7 == len(related_links)
        assert ('https://turntabl.io/our-services.html' in related_links) == True
        assert ('https://turntabl.io/terms-of-service.html' in related_links) == True
        assert ('https://turntabl.io/index.html' in related_links) == True

    def test_get_all_links(self, crawler):
        crawler, domain = crawler
        related, unrelated = crawler.map_weblinks(domain)
        assert len(related.union(unrelated)) > 7

    def test_gather_links_into_file(self, crawler):
        crawler, domain = crawler
        base_path = os.path.dirname(__file__)
        crawler.gather_links_into_file(domain)
        path_of_file = os.path.abspath(os.path.join(base_path, '..', 'results'))
        expected = Path(path_of_file)

        assert True == expected.exists()
        assert True == expected.is_file()
