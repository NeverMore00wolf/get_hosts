from urllib import request


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return
        maxTryNum = 10

        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
            'Referer': 'http://www.iqiyi.com/dianying/'
        }
        for tries in range(maxTryNum):
            try:
                get_url_req = request.Request(url=url, headers=head)
                response = request.urlopen(get_url_req)
                if response.getcode() != 200:
                    return None
                return response.read()
            except:
                if tries < (maxTryNum - 1):
                    continue
                else:
                    print("has tried %d times to access url %s, all filed!" ,maxTryNum, url)
