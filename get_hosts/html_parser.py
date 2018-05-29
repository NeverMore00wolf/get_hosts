from bs4 import BeautifulSoup
import re
import operator
class HtmlParser(object):


    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        link_all = soup.find_all('a')
        for link in link_all:
            #url_obj = re.match('<a.*?href="(.+)".*?>(.*?)</a>', str(link))
 #           print(url_obj.group(1))
#            print(url_obj.group(2))
            # new_urls.add(url.group(1))
            if str(link.get('href'))[:4]=='http':
                url = link.get('href')
            else:
                continue
            new_urls.add(url)
        return new_urls




    def _get_new_data(self, page_url, soup):
        result = []
        sort_result = {}
        link_all = soup.find_all('a')
        for link in link_all:

            if str(link.get('href'))[:4]=='http':
                url = link.get('href')
            else:
                continue
            #('<a.*?href="(.+)"?.*>(.*?)</a>')
            #rule2 = re.findall('http\://[a-zA-Z0-9\.\?/&\=\:]+', str(link))
            #rule1 = re,findall('>(.*?)</a>', str(link))
            #print(rule2)
            #print(rule2[0])
            name = re.search('>([^<img.*>].*?)</a>$', str(link))
            if name is not None:
                if name.group(1) is not None:
                     name = name.group(1)
                else:
                    name = ''
            else:
                name = ''
            #if rule2 == None:
            #     continue
            # if rule2.group(1) == None:
            #     continue
            # true_url = re.match('http\://[a-zA-Z0-9\.\?/&\=\:]+', str(url))
            #
            # if(true_url == None):
            #     continue
            url_name = str(url) + str(name)
            #print(url_name)
            #result[url_name] = link_all.count(url_name)
            #result = sorted(result.items(), key=lambda item: item[1])
            #result = sorted(result.values(), key=lambda x: x[1], reverse=True)
            #sorted(result.items( ), lambda x, y: operator.eq(x[1], y[1]), reverse=True)
            url_name = url_name.strip('\n')
            result.append(url_name)

        for i in result:
           sort_result[i] = result.count(i)
        #sort_result = sorted(sort_result.items(), key=lambda x: x[1], reverse=True)

        return sort_result


    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont.decode('utf-8', 'ignore'), 'lxml')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data

