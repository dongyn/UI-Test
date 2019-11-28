#coding=utf-8
#author='Shichao-Dong'


import time,os
import logging
import logging.handlers
#使用相对路径+绝对路径
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
log_path = PATH("../logs")

class Logger():

    def __init__(self):

        filename = 'cibn'+''.join(time.strftime('%Y%m%d'))+''.join('.log') #设置log名
        self.logname =os.path.join(log_path,filename)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #设置日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - [%(levelname)s] - %(message)s')
        self.handler = logging.handlers.RotatingFileHandler(self.logname, maxBytes=1024 * 1024, backupCount=5,encoding='utf-8')  # 实例化handler

    def output(self,level,message):
        '''
        :param level: 日志等级
        :param message: 日志需要打印的信息
        :return:
        '''
        #send logging output to a disk file

        self.handler.setLevel(logging.DEBUG)
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        self.logger.setLevel(logging.DEBUG)

        #send logging output to streams
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level =='debug':
            self.logger.debug(message)
        elif level =='warn':
            self.logger.warn(message)
        elif level =='error':
            self.logger.error(message)

        #防止重复打印
        self.logger.removeHandler(self.handler)
        self.logger.removeHandler(ch)

        self.handler.close()

    def info(self,message):
        self.output('info',message)

    def debug(self,message):
        self.output('debug',message)

    def warn(self,message):
        self.output('warn',message)

    def error(self,message):
        self.output('error',message)

