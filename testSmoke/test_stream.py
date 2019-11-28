# -*- coding:utf-8 -*-
#@Time  : 2019/9/16 15:21
#@Author: yanghuiyu
#@Function:stream

import unittest, time
import comm.common as common
from comm.webDriver import webDriver
from pageElement.homePage import homepage
from comm.readConfig import ReadConfig
from pageElement.base_element_operate import base

telephone = ReadConfig().get_app("telephone")

class Stream(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #打开应用，进入首页
        cls.driver = webDriver().get_driver()
        base(cls.driver).start_login_app()
        base(cls.driver).bottom_navigation("首页")
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()
        pass

    # 4
    def test_01_play_home_stream(self):
        """播放直播视频"""
        homepage(self.driver).stream_CCTV1()
        start_time = self.driver.find_element_by_id("dopool.player:id/portrait_current_duration").text
        self.assertEqual("分", start_time[-1:], "启播时间显示**时**分即播放正常")
        self.driver.find_element_by_id("dopool.player:id/backImage").click()  # 返回
        self.driver.find_element_by_id("dopool.player:id/common_page_finish").click()    #返回首页

    # 5
    def test_02_Reminisce(self):
        """播放直播视频，回看"""
        homepage(self.driver).stream_CCTV1()
        common.swipeDown(self.driver)
        common.swipeDown(self.driver)
        remimisce_text = self.driver.find_element_by_id("dopool.player:id/state_text").text
        self.assertEqual("回看",remimisce_text,"找到回看")
        self.driver.find_element_by_id("dopool.player:id/state_text").click()   #点击回看按钮
        start_time = self.driver.find_element_by_id("dopool.player:id/portrait_current_duration").text
        self.assertEqual("分", start_time[-1:], "启播时间显示**时**分即播放正常")
        self.driver.find_element_by_id("dopool.player:id/backImage").click()     #返回
        self.driver.find_element_by_id("dopool.player:id/common_page_finish").click()    #返回首页
        base(self.driver).bottom_navigation("首页")

    # 5
    def test_03_full_screen(self):
        """播放视频，全屏"""
        homepage(self.driver).stream_CCTV1()
        self.driver.find_element_by_id("dopool.player:id/iv_full_screen").click()
        common.delayed_get_element(self.driver, 10, ("id", "dopool.player:id/iv_full_screen"))
        # 点击屏幕中心
        time_text = self.driver.find_element_by_id("dopool.player:id/tv_time").text
        self.assertEqual("分", time_text[-1:], "启播时间显示**时**分即正常播放")
        self.driver.find_element_by_id("dopool.player:id/backImage").click()    #退出全屏
        self.driver.find_element_by_id("dopool.player:id/backImage").click()    #退出播放
        self.driver.find_element_by_id("dopool.player:id/common_page_finish").click()  # 返回首页
        base(self.driver).bottom_navigation("首页")

    # 6
    def test_04_change_station_vertical_screen(self):
        """竖屏换台"""
        homepage(self.driver).stream_CCTV1()
        common.delayed_get_element(self.driver, 15, ("xpath", "//*[@text='换台']")).click()
        self.driver.find_element_by_xpath("//*[@text='CIBN']").click()
        self.driver.find_element_by_xpath("//*[@resource-id='dopool.player:id/recyclerView']/android.view.View[1]").click()
        start_time = common.delayed_get_element(self.driver, 15, ("id", "dopool.player:id/portrait_current_duration")).text
        self.assertEqual("分", start_time[-1:], "启播时间显示**时**分即播放正常")
        self.driver.find_element_by_id("dopool.player:id/backImage").click()  # 返回
        self.driver.find_element_by_id("dopool.player:id/common_page_finish").click()  # 返回首页
        base(self.driver).bottom_navigation("首页")

    # 6
    def test_05_change_station_horizontal_screen(self):
        """横屏换台"""
        homepage(self.driver).stream_CCTV1()
        common.delayed_get_element(self.driver, 5, ("xpath", "//*[@text='换台']")).click()
        common.delayed_get_element(self.driver, 3, ("xpath", "//*[@text='央视']")).click()
        common.delayed_get_element(self.driver, 3, ("xpath", "//*[@text='CCTV3']")).click()
        time.sleep(7)
        start_time = self.driver.find_element_by_id("dopool.player:id/portrait_current_duration").text
        self.assertEqual("分", start_time[-1:], "启播时间显示**时**分即播放正常")

    # 17
    def test_06_reservation(self):
        """预约"""
        homepage(self.driver).stream_CCTV1()
        reservation_xpath = "//android.support.v7.widget.RecyclerView[@resource-id='dopool.player:id/epgListRV']/" \
                            "android.view.ViewGroup[6]/android.widget.TextView[3]"
        common.delayed_get_element(self.driver, 5, ("xpath", reservation_xpath)).click()
        time.sleep(3)
        self.assertTrue(common.isElementExist("xpath", self.driver, "//*[@text='已预约']"), "点击预约后按钮应变成已预约")
        item_xpath = "//*[@resource-id='dopool.player:id/epgListRV']/android.view.ViewGroup[6]/android.widget.TextView[2]"
        item_name = self.driver.find_element_by_xpath(item_xpath).text
        base(self.driver).click_play_float_button("backImage", [(79, 150)])
        common.delayed_get_element(self.driver, 3, ("id", "dopool.player:id/common_page_finish")).click()
        base(self.driver).bottom_navigation("我的")
        common.delayed_get_element(self.driver, 5, ("xpath", "//*[@text='我的预约']")).click()
        reservation_item = common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/tv_epg_name")).text
        self.assertEqual(item_name, reservation_item, "我的预约中显示已预约的节目和在竖屏播放节目单中预约的节目不一致")

    # 自动化新增
    def test_07_switching_clarity(self):
        """切换清晰度"""
        homepage(self.driver).stream_CCTV1(True)
        base(self.driver).click_play_float_button("third_tv", [(2099, 1008)])
        tv_definition = self.driver.find_elements_by_id("dopool.player:id/tv_definition")
        definition = tv_definition[1].text if self.driver.find_element_by_id(f"//*[@text='{tv_definition[0].text}']").get_attribute("selected") \
            else tv_definition[0].text
        self.driver.find_element_by_xpath(f"//*[@@text='{definition}']").click()
        base(self.driver).click_play_float_button("third_tv", [(2099, 1008)])
        self.assertTrue(self.driver.find_element_by_xpath(f"//*[@@text='{definition}']").get_attribute("selected"),"切换清晰度失败")
        common.click_screen_point(self.driver, 1 / 2, 1 / 8, 20)

    # 18
    def test_08_forum(self):
        """聊一聊"""
        homepage(self.driver).stream_CCTV1(live_title = "CCTV2")
        common.delayed_get_element(self.driver, 5, ("xpath", "//*[@text='聊一聊']")).click()
        send_button_text = common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/send_text")).text
        self.assertEqual("发送", send_button_text, "CCTV2竖屏播放页面切换到聊一聊页面失败")

    # 自动化新增
    def test_09_lock_screen(self):
        """锁屏"""
        homepage(self.driver).stream_CCTV1(is_full_screen = True)
        base(self.driver).click_play_float_button("iv_screen_lock", [(177, 468)])
        base(self.driver).click_play_float_button("third_tv", [(2153, 1008)])
        self.assertFalse(common.isElementExist("id", self.driver, "dopool.player:id/tv_definition"), "锁屏以后无法点击清晰度按钮")

    # 自动化新增
    def test_10_switch_screen_ratio(self):
        """切换屏幕比例"""
        homepage(self.driver).stream_CCTV1(is_full_screen=True)
        time.sleep(1)
        base(self.driver).click_play_float_button("iv_collapsing", [(2166, 175)])
        definition = "tv_definition_4_3" if self.driver.find_element_by_id("dopool.player:id/tv_definition_16_9").get_attribute("selected") \
            else "tv_definition_16_9"
        homepage(self.driver).switch_attributes(f"dopool.player:id/{definition}", "iv_collapsing", [(2166, 177)])
        self.assertTrue(self.driver.find_element_by_id(f"dopool.player:id/{definition}").get_attribute("selected"), "切换屏幕比例失败")
        common.click_screen_point(self.driver, 1 / 2, 1 / 2, 20)

    # 自动化新增
    def test_11_one_click_live(self):
        """一键直播"""
        #1.查看直播中的节目名称 2.回看 3.一键直播 4.查看是否在播放直播中的节目
        homepage(self.driver).stream_CCTV1()
        living_title = common.delayed_get_element(self.driver, 3, ("id", "dopool.player:id/live_title")).text
        common.swipeDown(self.driver, 1/2)
        self.driver.find_element_by_xpath("//*[@resource-id='dopool.player:id/epgListRV']/android.view.ViewGroup[1]/android.widget.TextView[3]").click()
        common.delayed_get_element(self.driver, 10, ("id", "dopool.player:id/iv_full_screen"))
        base(self.driver).click_play_float_button("civ_to_live", [(87, 388)])
        common.delayed_get_element(self.driver, 10, ("id", "dopool.player:id/iv_full_screen"))
        actual_living_title = common.delayed_get_element(self.driver, 3, ("id", "dopool.player:id/live_title")).text
        self.assertEqual(living_title, actual_living_title, f"一键直播播放的节目应该是{living_title}")

    # 自动化新增
    def test_12_watch_history(self):
        """直播的观看历史"""
        homepage(self.driver).clear_watch_history("直播")
        live_title = "CCTV1"
        homepage(self.driver).stream_CCTV1(live_title)
        common.delayed_get_element(self.driver, 3, ("id", "dopool.player:id/backImage")).click()
        common.delayed_get_element(self.driver, 3, ("id", "dopool.player:id/common_page_finish")).click()
        base(self.driver).bottom_navigation("我的")
        self.assertTrue(common.isElementExist("xpath", self.driver, f"//*[@text='{live_title}']"), f"观看历史中应显示{live_title}")

    # 7，14
    def test_13_exit_play(self):
        """退出播放"""
        base(self.driver).sign_out()
        homepage(self.driver).stream_CCTV1()
        common.delayed_get_element(self.driver, 17, ("id", "dopool.player:id/backImage")).click()
        page_name = common.delayed_get_element(self.driver, 3, ("id", "dopool.player:id/common_page_title")).text
        self.assertEqual("央视", page_name, "从直播页面返回的上级页面应该是央视页")

if __name__ == "__main__":
    Stream().test_13_exit_play()






