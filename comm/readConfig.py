#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/5/27 16:57
#@Author: dongyani 
#@File  : readConfig.py

import os,configparser

path = os.path.split(os.path.realpath(__file__))[0]
config_path = os.path.join(path, 'config.ini')#这句话是在path路径下再加一级，最后变成C:\Users\songlihui\PycharmProjects\dkxinterfaceTest\config.ini
config = configparser.ConfigParser()#调用外部的读取配置文件的方法
config.read(config_path, encoding='utf-8')

class ReadConfig():
    def get_config(self,name):
        value = config.get('config',name)
        return value

    def get_cmd(self,name):
        value = config.get('cmd',name)
        return value

    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value

    def get_app(self, name):
        value = config.get('APP', name)
        return value

    def get_test(self, name):
        value = config.get('TEST', name)
        return value

    # 获取数据库配置的相应键值
    def getDb(self, key):
        value = config.get("db", key)
        return value

    # 获取日志配置的相应键值
    def getLog(self,key):
        value = config.get("log", key)
        return value

    # 获取浏览器配置的相应键值
    def getDriver(self):
        value = int(config.get("browser", "browserType"))
        return value

    # 获取测试url
    def getUrl(self):
        value = int(config.get("url", "Environmental"))
        if value == 0:
            value = config.get("url", "testUrl")
        else:
            value = config.get("url", "formalUrl")
        return value

    # 运行结果是否保留的参数
    def getResult(self):
        value = int(config.get("result", "isClear"))
        return value

# if __name__ == '__main__':#测试一下，我们读取配置文件的方法是否可用
#     print('EMAIL中的开关on_off值为：', ReadConfig().get_email('on_off'))