#coding:utf8
from collections import Counter

class HtmlOutputer(object):
    def __init__(self):
        self.datas = {}



    def collect_data(self, data):
        if data is None:
            return
        if self.datas is None:
            self.datas = data
        else:
            for k, v in data.items():
                if k in self.datas.items():
                    self.datas[k] += v
                else:
                    self.datas[k] = v
            # self.datas = dict(Counter(self.datas) + Counter(data))
        #print(self.datas)


    def out_html(self):
        #print(self.datas)
        sort_result = sorted(self.datas.items(), key=lambda x: x[1], reverse=True)
        print(sort_result)
        fout = open('output.html', 'w', encoding='utf-8')
        # fout.write('<html>')
        # fout.write('<body>')
        # fout.write('<table>')
        for x in sort_result:
            # fout.write('<tr>')
            fout.write(str(x))
            fout.write('\n')
            # fout.write('</tr>')
        # for v,k in sort_result.items():
        #    print('{v}:{k}'.format(v = v, k = k))
        # fout.write('</table>')
        # fout.write('</body>')
        # fout.write('</html>')
        fout.close()