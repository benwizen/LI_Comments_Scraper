# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re


def soup_comments(comments):
    soup = BeautifulSoup(comments, 'html.parser')
    souped_comments = soup.find_all("article", class_="comments-comments-list__comment-item")

    for comment in souped_comments:
        try:
            writer = comment.find("span", class_="hoverable-link-text").text
            position = comment.find("span", class_=re.compile("^feed-shared-post-meta__headline")).text.strip()
            content = comment.find("p", class_=re.compile("^comments-comment-item__main-content")).text
            when = comment.find("time").text
            yield (writer, position, content, when)
        except AttributeError:
            print(comment)
            raise


if __name__ == "__main__":
    pass
