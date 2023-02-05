from crawler.CommandlineArgs import *
from crawler.DeepCrawler import DeepCrawler
from crawler.ShallowCrawler import ShallowCrawler
from crawler.Utils import *

# Getting the input arguments
args = get_args()
url = args.url
is_deep = args.deepcrawl
choose_crawler = {True: DeepCrawler, False: ShallowCrawler}
crawler = choose_crawler[is_deep]()


@timing
def run():
    """Entry point for Web Crawler"""
    if validate_url(url):
        return crawler.gather_links_into_file(url)
    print(f'Kindly check your url: {url}\n')
    return


if __name__ == '__main__':
    run()