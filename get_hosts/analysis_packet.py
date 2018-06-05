import os, re

    # 导入scapy和scapy_http模块

try:
    import scapy.all as scapy
except ImportError:
    import scapy

try:
    import scapy_http.http
except ImportError:
    from scapy.layers import http

def del_packet():
    # !/usr/bin/env python
    # -*- coding: UTF-8 -*-
    '''
    host&user-agent&referer的统计输出
    @author:qny&wangtingting
    @date:2018-05-10
    '''



    # 读取报文，报文名称为http,路径与本脚本路径相同
    packets = scapy.rdpcap('http.pcap')

    # 报文中host&user-agent&referer的输出文本
    f = open("out.txt", "w")

    for p in packets:
        # print('=' * 78)


        # 获取host
        try:
            host = "Host:" + str(p.payload.getfieldval('Host'), encoding='utf-8')
            # print(host)
        except:
            host = "Host:"
            # print(host)
        f.write(host + '\n')

        # 获取User-Agent
        try:
            useragent = "User-Agent:" + str(p.payload.getfieldval('User-Agent'), encoding='utf-8')
            # print(useragent)
        except:
            useragent = "User-Agent:"
            # print(useragent)
        f.write(useragent + '\n')

        # 获取Referer
        try:
            referer = "Referer:" + str(p.payload.getfieldval('Referer'), encoding='utf-8')
            # print(referer)
        except:
            referer = "Referer:"
            # print(referer)
        f.write(referer + '\n')

        f.write('\n')

    f.close()

    def write_to_file(string):
        # 统计的输出文件，路径与本脚本路径相同
        fp = open('out_new.txt', 'a+')
        fp.write(string + '\n')
        fp.close()

    def tongji(file):
        host = []
        user_agent = []
        user_agent_fenkai = []
        referer = []
        pattern1 = re.compile(r'Host:.')
        pattern2 = re.compile(r'User-Agent:.')
        pattern3 = re.compile(r'Referer:.')
        f = open(file, 'r')
        for line in f.readlines( ):
            if pattern1.findall(line):
                host_new = line.split(':', 1)[1].replace('\n', '')
                host.append(host_new)
            if pattern2.findall(line):
                user_agent_new = line.split(':', 1)[1].replace('\n', '')
                user_agent.append(user_agent_new)
            if pattern3.findall(line):
                referer_new = line.split(':', 1)[1].replace('\n', '')
                referer.append(referer_new)

        for agent in user_agent:
            xulie = agent.split( )
            count = 0
            changdu = len(xulie)
            while count < changdu:
                if xulie[count].startswith('(') is not True:
                    user_agent_fenkai.append(xulie[count])
                    count = count + 1
                elif xulie[count].startswith('('):
                    new = ''
                    startnum = count
                    while count < changdu:
                        if xulie[count].endswith(')'):
                            endnum = count
                            count = count + 1
                            break
                        else:
                            count = count + 1
                    while startnum <= endnum:
                        new += xulie[startnum]
                        startnum += 1
                    user_agent_fenkai.append(new)

        # print ('host and number:')
        write_to_file('host and number:')
        paixu(host)
        write_to_file('\n')
        # print 'user-agent and number:'
        write_to_file('user-agent and number:')
        paixu(user_agent_fenkai)
        write_to_file('\n')
        # print 'referer and number:'
        write_to_file('referer and number:')
        paixu(referer)
        write_to_file('\n')

    def paixu(list):
        zidian = {}
        list_quchong = set(list)
        for item in list_quchong:
            zidian.update({item: list.count(item)})
        dict_new = sorted(zidian.items( ), key=lambda d: d[1], reverse=True)
        for i in dict_new:
            abc = '{0:^10},{1:^15}'.format(i[0], i[1])
            # print '{0:^10},{1:^15}'.format(i[0], i[1])
            write_to_file(abc)
        # print(' ' * 50)









