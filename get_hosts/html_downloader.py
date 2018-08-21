from urllib import request
import requests
import ssl
import sys

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        maxtrynum = 10

        head = {
            #"Host": "list.iqiyi.com",
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
            #"Referer": "http://list.iqiyi.com/www",
            #"Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8",
        }
        for tries in range(maxtrynum):
            try:
                ssl._create_default_https_context = ssl._create_unverified_context
                get_url_req = request.Request(url=url, headers=head)
                response = request.urlopen(get_url_req)
                html = response.read()
                #de_html = html.decode('utf-8')

                if response.getcode() != 200:
                    return None
                return html
            except:
                if tries < (maxtrynum - 1):
                    continue
                else:
                    print("has tried %d times to access url %s, all filed!" % (maxtrynum, url))




