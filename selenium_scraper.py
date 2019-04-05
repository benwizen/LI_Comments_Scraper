from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException
from time import sleep
import getpass
import sys


def scrape_li_comments(url):
    """ Selenium to load all the comments of the post. """
    try:
        """ Selenium configuration """
        options = webdriver.ChromeOptions()
        username = getpass.getuser()
        options.add_argument(r"user-data-dir=C:\Users\{0}\AppData\Local\Google\Chrome\User Data".format(username))
        driver = webdriver.Chrome(options=options)
        driver.get(url)

    except InvalidArgumentException:
        print("All chrome windows must be closed!")
        sys.exit(1)

    """ Loop to load all comments - until button does'nt exist (NoSuchElementException) """
    while True:
        try:
            driver.find_element_by_id('show_prev').click()
            sleep(1)
        except NoSuchElementException:
            break

    comments = driver.find_elements_by_class_name("comments-comments-list__comment-item")
    print(f"======================================")
    print(f"The post has {len(comments)} comments.")
    print(f"======================================\n")

    comments_container = driver.find_element_by_class_name("comments-comments-list")
    comments_html = comments_container.get_attribute('innerHTML')
    return comments_html
