# -*- coding:utf-8 -*-
# @Time  : 2019/8/28
# @Author: yanghuiyu
# @UITest：意见反馈页面

from comm.webDriver import webDriver
from comm.Log import Logger
import time, unittest

driver = webDriver().setUpClass()
logger = Logger().get_logger()
class TestFeedbackpage(webDriver, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

