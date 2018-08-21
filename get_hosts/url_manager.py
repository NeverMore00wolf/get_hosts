import re

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    def add_new_url(self, url):

        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)


    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            xz_url = re.match('http://.*?.com/.*?', str(url))
            if str(xz_url) is not None:
                self.add_new_url(url)
            else:
                continue

    #判断是否有新的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    #获取一个url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
