#coding:utf8
import html_downloader
import html_output
import html_parser
import url_manager
import capture_packet
import analysis_packet
import time
import threading
import ctypes
import inspect





class SpiderMain(object):
    def __init__(self, root_url):

        self.url = root_url


        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_output.HtmlOutputer()


    def craw(self):
        count = 1
        print(self.url)
        self.urls.add_new_url(self.url)
        # try:
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print('craw %d : %s' % (count, new_url))
            #html_cont = self.downloader.download(new_url)
            if self.downloader.download(new_url) is None:
                continue
            else:
                html_cont = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parse(new_url, html_cont)
            self.urls.add_new_urls(new_urls)
            self.outputer.collect_data(new_data)

            if count == 2:
                break
            count = count + 1
            time.sleep(5)
        # except:
        #     print('craw faild!!!!!!')

        self.outputer.out_html()

class del_packets(object):
    def __init__(self):
        self.capture = capture_packet.capture()

    def collect_packet(self):
        self.capture()


class analysis():
    def __init__(self):
        self.del_capture = analysis_packet.del_packet()
    def del_capture(self):
        self.del_packet()

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
    def run(self):
        print(self.name + "thread begin #########")

        if self.name == "spider":
            print(self.args)
            SpiderMain(self.args).craw()

        elif self.name == "capture":
            del_packets()
        print(self.name + "thread finish ##############")


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)



if __name__ == "__main__":
    root_url = "http://tv.cctv.com"
    thing1 = MyThread(SpiderMain, root_url, "spider")
    thing2 = MyThread(del_packets, None, "capture")
    thing1.start()
    thing2.start()
    thing1.join()
    # thing2.join()
    print(thing1.isAlive( ))
    print(thing2.isAlive( ))
    if thing1.isAlive() == False:
        stop_thread(thing2)

    # obj_spider = SpiderMain()
    # obj_spider.start()
    #obj_spider = threading.Thread(target=SpiderMain(1, "Thread-spider"), )
    #threads.append(obj_spider)
    #obj_packet = del_packets(2, "Thread-del")
    #obj_packet.start()
    #obj_packet = threading.Thread(target=del_packets(2, "Thread-del").collect_packet())
    #threads.append(obj_packet)

    #obj_packet.collect_packet().start()
    #obj_spider.craw(root_url).start()
    # for thing in threads:
    #     thing.setDaemon(True)
    #
    #     thing.start()



    #obj_packet.join()
    #obj_spider.join()
    # start analysis packet
    #analysis().del_capture()



    