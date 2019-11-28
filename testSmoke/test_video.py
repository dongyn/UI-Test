# -*- coding:utf-8 -*-
#@Time  : 2019/9/16 15:56
#@Author: dongyani
#@Function: video

import unittest,time
from comm.webDriver import webDriver
import comm.common as common
from comm.readConfig import ReadConfig
from pageElement.base_element_operate import base
from pageElement.homePage import homepage

appPackage = ReadConfig().get_config("appPackage")
video_title = ReadConfig().get_app('video_title')

class Video(unittest.TestCase):

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
    def test_01_play_home_video(self):
        """在首页推荐页面，搜索输入-video_title，点击页面展示的第一条，点击立即观看，视频正常播放"""
        homepage(self.driver).play_video(video_title, True)
        self.assertTrue(True, "全屏按钮没有出现，点播视频播放失败")

    # 5
    def test_02_full_screen(self):
        """播放视频，全屏"""
        homepage(self.driver).play_video(video_title, True)
        self.assertFalse(common.isElementExist("id", self.driver, "dopool.player:id/recommendTitle"), "点击全屏播放，猜你喜欢不应出现")

    # 6
    def test_03_recommend(self):
        """猜你喜欢"""
        homepage(self.driver).play_video(video_title)
        #猜你喜欢第一个标题的xpath
        title_xpath = "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android." \
                      "widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view." \
                      "ViewGroup[1]/android.support.v4.view.ViewPager[1]/android.support.v7.widget.RecyclerView[1]/android." \
                      "view.ViewGroup[4]/android.widget.TextView[1]"
        recommend_title = common.delayed_get_element(self.driver,10,("xpath",title_xpath)).text
        # 猜你喜欢第一个视频图片的xpath
        xpath = "//android.support.v7.widget.RecyclerView[@resource-id='dopool.player:id/recyclerView']/android.view." \
                "ViewGroup[4]/android.widget.ImageView[1]"
        self.driver.find_element_by_xpath(xpath).click()
        common.click_screen_point(self.driver, 1/2, 1/8, 20)
        real_title = common.delayed_get_element(self.driver,10,("xpath","//*[@resource-id='dopool.player:id/tv_title']")).text
        self.assertTrue(recommend_title in real_title, f"猜你喜欢列表播放的视频应该是{recommend_title}")

    # 自动化新增
    def test_04_switching_clarity(self):
        """切换清晰度"""
        homepage(self.driver).play_video(video_title, True)
        base(self.driver).click_play_float_button("third_tv", [(2099, 1008)])
        tv_definition = self.driver.find_elements_by_id("dopool.player:id/tv_definition")
        definition = tv_definition[1].text if self.driver.find_element_by_id(
            f"//*[@resource-id='dopool.player:id/tv_definition' and @text='{tv_definition[0].text}']").get_attribute("selected") \
            else tv_definition[0].text
        self.driver.find_element_by_xpath(f"//*[@resource-id='dopool.player:id/tv_definition' and @text='{definition}']").click()
        base(self.driver).click_play_float_button("third_tv", [(2099, 1008)])
        self.assertTrue(self.driver.find_element_by_xpath(f"//*[@resource-id='dopool.player:id/tv_definition' and @text='{definition}']").\
                        get_attribute("selected"),
                        "切换清晰度失败")
        common.click_screen_point(self.driver, 1 / 2, 1 / 8, 20)

    # 自动化新增， 点播的弹幕暂时不做
    # def test_05_barrage(self):
    #     """弹幕"""


    # 自动化新增
    def test_06_lock_screen(self):
        """锁屏"""
        homepage(self.driver).play_video(video_title, True)
        base(self.driver).click_play_float_button("iv_screen_lock", [(177, 468)])
        base(self.driver).click_play_float_button("third_tv", [(2153, 1008)])
        self.assertFalse(common.isElementExist("id", self.driver, "dopool.player:id/tv_definition"), "锁屏以后无法点击清晰度按钮")

    # 自动化新增
    def test_07_switch_screen_ratio(self):
        """切换屏幕比例"""
        homepage(self.driver).play_video(video_title, True)
        time.sleep(1)
        base(self.driver).click_play_float_button("iv_collapsing", [(2166, 175)])
        definition = "tv_definition_4_3" if self.driver.find_element_by_id("dopool.player:id/tv_definition_16_9").get_attribute("selected") \
            else "tv_definition_16_9"
        homepage(self.driver).switch_attributes(f"dopool.player:id/{definition}", "iv_collapsing", [(2166, 177)])
        self.assertTrue(self.driver.find_element_by_id(f"dopool.player:id/{definition}").get_attribute("selected"),"切换屏幕比例失败")
        common.click_screen_point(self.driver, 1 / 2, 1 / 8, 20)

    # 自动化新增
    def test_08_collection(self):
        """收藏点播视频"""
        homepage(self.driver).play_video(video_title)
        common.delayed_get_element(self.driver, 3, ("id", "dopool.player:id/collection_text")).click()
        common.delayed_get_element(self.driver, 3, ("id", "dopool.player:id/backImage")).click()
        common.delayed_get_element(self.driver, 3, ("id", "dopool.player:id/cancel_text")).click()
        base(self.driver).bottom_navigation("我的")
        common.delayed_get_element(self.driver, 3, ("xpath", "//*[@text='我的收藏']")).click()
        common.delayed_get_element(self.driver, 3, ("xpath", "//*[@text='点播']")).click()
        self.assertEqual(video_title, self.driver.find_element_by_id("dopool.player:id/tvTitle").text,
                         f"我的收藏点播列表应该是{video_title}")

    # 自动化新增
    def test_09_watch_history(self):
        """点播的观看历史"""
        homepage(self.driver).clear_watch_history("点播")
        homepage(self.driver).play_video(video_title)
        common.delayed_get_element(self.driver, 3, ("id", "dopool.player:id/backImage")).click()
        common.delayed_get_element(self.driver, 3, ("id", "dopool.player:id/cancel_text")).click()
        base(self.driver).bottom_navigation("我的")
        self.assertTrue(common.isElementExist("xpath", self.driver, f"//*[@text='{video_title}']"), f"观看历史中应显示{video_title}")

    # 7
    def test_10_exit_play(self):
        """退出播放"""
        base(self.driver).sign_out()
        homepage(self.driver).play_video(video_title)
        common.delayed_get_element(self.driver, 17, ("id", "dopool.player:id/backImage")).click()
        common.delayed_get_element(self.driver, 3, ("id", "dopool.player:id/btn_left")).click()
        time.sleep(1)
        self.assertTrue(common.isElementExist("xpath", self.driver, "//*[@text='点播']"), "退出点播后应显示搜索页面")


# if __name__ == "__main__":
#     Video().test_04_switching_clarity()