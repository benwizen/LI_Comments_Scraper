from datetime import datetime, timedelta
import re


class Comment:
    def __init__(self, writer, position, content, when):
        self.writer = writer
        self.position = position
        self.content = content
        self.when = Comment.convert_to_date(when)
        self.has_mail = Comment.contains_mail(self.content)
        self.mails = Comment.extract_mails(content)

    @staticmethod
    def convert_to_timedelta_arg(cmt_time):
        days_per_unit = {"h": 'hours', "d": 'days', "w": 'weeks'}
        return {days_per_unit[cmt_time[-1]]: int(cmt_time[:-1])}

    @staticmethod
    def convert_to_date(when):
        time_format = "%d/%m/%y"
        now = datetime.now()
        return datetime.strftime(now - timedelta(**Comment.convert_to_timedelta_arg(when)), time_format)

    def is_newer_from_days_ago(self, days_ago):
        time_format = "%d/%m/%y"
        now = datetime.now()
        diff = now - datetime.strptime(self.when, time_format)
        return diff < timedelta(days_ago)

    @staticmethod
    def contains_mail(content):
        mail_pattern = re.compile(r"\w+@(\w+\.){1,2}\w{1,3}")
        if mail_pattern.search(content):
            return True
        return False

    @staticmethod
    def extract_mails(content):
        mail_pattern = re.compile(r"(\w+@(\w+\.){1,2}\w{1,3})")
        m = mail_pattern.findall(content)
        return [t[0] for t in m]

    def __str__(self):
        return f"Comment by: {self.writer}\n" \
            f"Writer position: {self.position}\n" \
            f"When: {self.when}\n" \
            f"Content: {self.content}\n" \
            f"Has_mail: {self.has_mail}\n" \
            f"Emails: {self.mails}"


def print_comments(new_comments):
    new_comments_count = 0
    for c in new_comments:
        new_comments_count += 1
        print("--------------------------------------")
        print(c)

    if new_comments:
        print("--------------------------------------")
        print()
        print("=======================================")
        print(f"Found {new_comments_count} new comments")
        print("=======================================")
    else:
        print("No results")


if __name__ == "__main__":
    pass
