# -*- coding:utf-8 -*-
#@Time  : 2019/8/15 18:13
#@Author: pengjuan

import comm.common as common
import time
from selenium.webdriver.support.ui import WebDriverWait
from comm.readConfig import ReadConfig
from pageElement.base_element_operate import base

telephone = ReadConfig().get_app("telephone")


class homepage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.close_float_id = "dopool.player:id/iv_dismiss_popup"
        self.float_id = "dopool.player:id/image_get_coin"

    def stream_CCTV1(self, live_title = "CCTV1", is_full_screen = False):
        """在首页推荐页面，在icon组点央视，播放CCTV1,视频正常播放"""
        if not self.driver.find_element_by_id("dopool.player:id/tabText").text == "首页" :
            base(self.driver).bottom_navigation("首页")
        icon_xpath = f"//android.support.v7.widget.RecyclerView[@resource-id='dopool.player:id/common_rcy']/android." \
            f"widget.LinearLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[2]"
        common.delayed_get_element(self.driver, 60, ("xpath", icon_xpath)).click()
        common.delayed_get_element(self.driver, 60, ("xpath", f"//*[@text='{live_title}']")).click()
        if is_full_screen: common.delayed_get_element(self.driver, 10, ("id", "dopool.player:id/iv_full_screen")).click()

    def play_video(self, video_title, is_full_screen = False):
        time.sleep(7)
        if not self.driver.find_element_by_id("dopool.player:id/tabText").text == "首页" :
            base(self.driver).bottom_navigation("首页")
        common.delayed_get_element(self.driver, 10, ("id", "dopool.player:id/tv_tip")).click()
        common.delayed_get_element(self.driver, 10, ("id", "dopool.player:id/search_edit")).send_keys(video_title)
        video_title_xpath = "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout" \
                            "[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android." \
                            "widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.support.v7.widget.RecyclerView[1]/android." \
                            "widget.TextView[1]"
        common.delayed_get_element(self.driver, 3, ("xpath", video_title_xpath)).click()
        common.delayed_get_element(self.driver, 3, ("id", "dopool.player:id/tv_watch")).click()
        if is_full_screen: common.delayed_get_element(self.driver, 10, ("id", "dopool.player:id/iv_full_screen")).click()

    def switch_attributes(self, definition, attribute_id, bounds):
        self.driver.find_element_by_id(definition).click()
        base(self.driver).click_play_float_button(f"dopool.player:id/{attribute_id}", bounds)

    def clear_watch_history(self, page):
        base(self.driver).bottom_navigation("我的")
        common.delayed_get_element(self.driver, 3, ("xpath", "//*[@text='查看更多']")).click()
        common.delayed_get_element(self.driver, 3, ("xpath", f"//*[@text='{page}']")).click()
        self.driver.find_element_by_id("dopool.player:id/managerTextView").click()
        common.delayed_get_element(self.driver, 3, ("xpath", "//*[@text='全选']")).click()
        common.delayed_get_element(self.driver, 3, ("xpath", "//*[@text='删除']")).click()
        self.driver.find_element_by_id("dopool.player:id/backImage").click()