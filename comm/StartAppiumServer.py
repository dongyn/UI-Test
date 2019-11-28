#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/9/3 16:57
#@Author: dongyani

from comm.Log import Logger
from comm.readConfig import ReadConfig
import time,os

conf = ReadConfig()
log = Logger()
appium_port = conf.get_config('appium_port')

class Sp():

    def stop_appium(self):
        '''关闭appium服务'''
        # if pc.upper() == 'WIN':
        p = os.popen(f'netstat -aon|findstr {appium_port}')
        p0 = p.read().strip()
        print(f"appium进程信息：{p0}")
        if p0 != '' and 'LISTENING' in p0:
            p1 = int(p0.split('LISTENING')[1].strip()[0:4])  # 获取进程号
            # print(p1)
            os.popen(f'taskkill /F /PID {p1}')  # 结束进程
            print('appium server进程已结束')
        # elif pc.upper() == 'MAC':
        #     p = os.popen(f'lsof -i tcp:{post_num}')
        #     p0 = p.read()
        #     if p0.strip() != '':
        #         p1 = int(p0.split('\n')[1].split()[1])  # 获取进程号
        #         os.popen(f'kill {p1}')  # 结束进程
        #         print('appium server已结束')

    def start_appium(self):
        p = os.popen(f'netstat -aon|findstr {appium_port}')
        p0 = p.read().strip()
        if p0 != '':
            print(f"appium进程已启动，进程信息：{p0}")
            self.stop_appium()
        else:
            t = f"start /b node D:\Appium\\node_modules\\appium\lib\server\main.js --address 127.0.0.1 --port {appium_port}"
            os.system(t)
            time.sleep(2)
            print("appium server进程启动成功")
            p = os.popen(f'netstat  -aon|findstr {appium_port}')
            p0 = p.read().strip()
            print(f"appium server进程信息：{p0}")

# if __name__ == '__main__':
    # Sp().start_appium()
    # Sp().stop_appium()
    # print(s)
