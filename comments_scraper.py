import argparse
from soupper import soup_comments
from consts import comments_txt
from Comment import Comment, print_comments
from selenium_scraper import scrape_li_comments


def execute_scrape(url, days_ago, debug=False):
    """ If debug is True - Soup constant HTML from consts.py.
        Else - Use selenium to extract HTML from URL. """
    if debug:
        comments_html = comments_txt
    else:
        comments_html = scrape_li_comments(url)

    """ All post's comments generator """
    all_comments = (Comment(*souped_cmt) for souped_cmt in soup_comments(comments_html))
    """ Only post's new comments generator """
    new_comments = (c for c in all_comments if c.is_newer_from_days_ago(days_ago) and c.has_mail)

    """ Print new comments """
    print_comments(new_comments)


if __name__ == "__main__":

    """ Argument parser for URL path and requested comments age """
    parser = argparse.ArgumentParser()
    parser.add_argument('post_url', type=str, help='LI post URL to scrape comments from.')
    parser.add_argument('days_ago', type=int, help='The comment is newer than X days ago.')
    parser.add_argument('--debug', dest='debug', nargs='?',
                        default=False, const=True,
                        help='Instead of using scraping with selenium, using const html source')

    args = parser.parse_args()
    url = args.post_url
    days_ago = int(args.days_ago)
    debug = args.debug
    execute_scrape(url, days_ago, debug)
