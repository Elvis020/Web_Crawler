import argparse


# TODO: the user should be able to specify the number of threads
def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
        description='An app for recursively crawling the links of the domains of a url',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog='******* Developed by Elvis O. Amoako *******')
    parser.add_argument('-u',
                        '--url',
                        help='The domain url to be crawled',
                        metavar='str',
                        type=str,
                        default='https://turntabl.io')
    parser.add_argument('-d',
                        '--deepcrawl',
                        help='This indicates that the website has embedded links leading to external pages i.e links '
                             'lead to external web-pages and the crawling is done recursively, for one-paged '
                             'websites like(https://turntabl.io), this option should be False',
                        action=argparse.BooleanOptionalAction,
                        metavar='bool',
                        type=bool,
                        default=False)
    return parser.parse_args()