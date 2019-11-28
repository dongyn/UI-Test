# -*- coding:utf-8 -*-
#@Time  : 2019/8/28 11:11
#@Author: pengjuan

# -*- coding:utf-8 -*-
#@Time  : 2019/8/23 17:52
#@Author: pengjuan

from comm.webDriver import webDriver
import pageElement.firstEnterPage as first_enter
from comm.Log import Logger
import comm.common as common
import time, unittest

driver = webDriver()
logger = Logger().get_logger()
class TestFirstEnterPage(webDriver, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_first_enter_page(self):
        """
        用户下载后，首次打开APP
        :return:
        """
        logger('======test_first_enter_page=====')
        # 用户权限按钮
        first_enter.swipe_guide(self.driver, 2)
        time.sleep(1)
        # 去勾选360.apk
        first_enter.click_checkbox(self.driver)
        time.sleep(3)
        first_enter.click_experience(self, driver)
        # 检测是否有升级，有的话点击暂不更新
        if firstEnterPage.is_update(self.driver):
            first_enter.click_update()
            time.sleep(2)
        else:
            self.assertTrue("推荐", first_enter.click_checkbox(), msg="未进入首页")













