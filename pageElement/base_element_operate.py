# -*- coding:utf-8 -*-
#@Time  : 2019/9/5 9:51
#@Author: dongyani
#@Function: 这个文件里面放的全部是基本的元素和元素相关的基本操作

import hashlib, time
import comm.common as common
from selenium.webdriver.support.ui import WebDriverWait
from comm.readConfig import ReadConfig
from datetime import datetime

telephone = ReadConfig().get_app("telephone")

class base():
    def __init__(self, driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 30)
        self.close_float_id = "dopool.player:id/iv_dismiss_popup"
        self.float_id = "dopool.player:id/image_get_coin"

    # 底部导航栏的图标按钮
    def bottom_navigation(self, button_name):
        xpath_mine = "//android.widget.LinearLayout[@resource-id='dopool.player:id/bottomNavigationView']/android." \
                     "widget.FrameLayout[5]/android.widget.FrameLayout[1]/android.widget.ImageView[1]"
        # button_index = {}
        if common.isElementExist("xpath", self.driver, xpath_mine):
            button_index = {"首页": 1,"直播": 2,"热点": 3,"会员": 4,"我的": 5}
        else:
            button_index = {"首页": 1, "直播": 2, "会员": 3, "我的": 4}
        xpath = f"//android.widget.LinearLayout[@resource-id='dopool.player:id/bottomNavigationView']/android.widget." \
            f"FrameLayout[{button_index[button_name]}]/android.widget.FrameLayout[1]/android.widget.ImageView[1]"
        common.delayed_get_element(self.driver, 10, ("xpath", xpath)).click()

    #界面只能存在一个字体按钮
    def text_tag(self):
        xpath = "//android.widget.TextView[@resource-id='dopool.player:id/tabText']"
        self.driver.find_element_by_xpath(xpath)

    # 切换首页页签
    def switch_home_tab(self, tab):
        # 定位到首页的顶部tabs列表按钮
        common.delayed_get_element(self.driver, 40, ("id", "dopool.player:id/img_all_channel"))
        common.delayed_get_element(self.driver, 10, ("xpath", f"//*[@text='{tab}']")).click()

    # 切换首页icon
    def switch_tab(self, icon):
        self.driver.find_element_by_xpath(f"//*[@text='{icon}']").click()

    def permission_allow(self):
        time.sleep(1)
        permission_id = "com.android.packageinstaller:id/permission_allow_button"
        if common.isElementExist("id", self.driver, "android:id/button1"): permission_id = "android:id/button1"
        while common.isElementExist("id", self.driver, permission_id): #更多精彩视频
            self.driver.find_element_by_id(permission_id).click()
            time.sleep(1)

    # 引导页面，左滑两次，立即体验
    def slide_guide_page(self):
        while not common.isElementExist("id", self.driver, "dopool.player:id/btn_start_experience"):
            common.swipeLeft(self.driver)

    # 去掉捆绑广告的勾选，点击立即进入
    def enter_app(self):
        time.sleep(3)
        if common.isElementExist("id", self.driver, "dopool.player:id/iv_checkbox"):
            common.delayed_get_element(self.driver, 1, ("id", "dopool.player:id/iv_checkbox")).click()
        if common.isElementExist("id", self.driver, "dopool.player:id/btn_start_experience"):
            common.delayed_get_element(self.driver, 1, ("id", "dopool.player:id/btn_start_experience")).click()

    # 关闭隐私弹框
    def close_privacy(self):
        common.delayed_get_element(self.driver, 15, ("id", "dopool.player:id/tv_Policy_agree")).click()

    # 如果有升级弹框的话，关掉升级弹框
    def close_upgrade(self):
        if common.isElementExist("id", self.driver, "dopool.player:id/tv_update_list"):
            self.driver.find_element_by_id("dopool.player:id/tv_update_cancle").click()

    # 如果有通知管理弹框的话，关掉通知管理弹框
    def close_notice_manage(self):
        if common.isElementExist("id", self.driver, "dopool.player:id/textView"):
            self.driver.find_element_by_id("dopool.player:id/tv_score_cancle").click()

    # 是否允许安装应用
    def permission_prompt(self):
        #允许手机电视安装新应用
        common.delayed_get_element(self.driver, 6, ("id", "com.android.packageinstaller:id/ok_button")).click()
        # 打开
        common.delayed_get_element(self.driver, 6, ("id", "com.android.packageinstaller:id/launch_button")).click()

    #如果有浮层的话，就关掉浮层，回到首页
    def close_float(self):
        """
        如果有浮层关闭按钮的话，点击关闭，就关掉浮层了
        如果没有，就要点击浮层，进入直播、点播或H5页面，
        直播和点播的退出：点系统返回，弹出退出窗再点退出按钮
        H5的退出：点系统返回即可
        """
        time.sleep(3)
        if common.isElementExist("id", self.driver, self.close_float_id):
            self.driver.find_element_by_xpath(self.close_float_id).click()
        elif common.isElementExist("id", self.driver, self.float_id):
            self.driver.find_element_by_xpath(self.float_id).click()
            self.driver.keyevent(4)# 点击系统返回键
            if common.isElementExist("id", self.driver, "dopool.player:id/img_history"):
                return
            else:
                ele_quit = common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/btn_left"))
                ele_quit.click()  # 退出直播或点播

    def close_childmode(self):
        # 点击知道了，即可关闭青少年模式
        if common.isElementExist("id", self.driver, "dopool.player:id/i_k"):
            self.driver.find_element_by_id("dopool.player:id/i_k").click()

    def encrypt_md5(self, timeStamp):
        timestr = str(int(int(timeStamp / 300) * 300))
        key = "edeac39d37f25c04020b9e6aa4802965500c26ea"
        sum_time = timestr + key + timestr
        md5_str = hashlib.md5(sum_time.encode()).hexdigest()[0:6]
        return md5_str

    #点击跳转到登录页面的按钮，在登录页面输入手机号码和验证码
    def login(self, xpath):
        common.delayed_get_element(self.driver, 5, ("xpath", xpath)).click()
        common.delayed_get_element(self.driver, 3, ("id", "dopool.player:id/phoneEdit")).send_keys(telephone)
        timeStamp = int(time.mktime(datetime.now().timetuple()))
        self.driver.find_element_by_id("dopool.player:id/smsCodeEdit").send_keys(self.encrypt_md5(timeStamp))
        while common.isElementExist("id", self.driver, "dopool.player:id/loginBtn"):
            self.driver.find_element_by_id("dopool.player:id/loginBtn").click()

    #退出登陆
    def sign_out(self):
        self.bottom_navigation("我的")
        common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/img_user_head")).click()
        common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/logoutBtn")).click()

    def start_app(self):
        # 打开应用，进入首页
        self.close_privacy()
        self.permission_allow()
        self.slide_guide_page()
        self.enter_app()
        self.close_upgrade()
        self.close_float()
        self.close_childmode()

    def start_login_app(self):
        self.start_app()
        self.bottom_navigation("我的")
        self.login("//*[@resource-id='dopool.player:id/img_user_head']")

    def click_play_float_button(self, float_button_id, float_button_bounds):
        if not common.isElementExist("id", self.driver, f"dopool.player:id/{float_button_id}"):
            common.click_screen_point(self.driver, 1 / 2, 1 / 8, 20)
            time.sleep(1)
            self.driver.tap(float_button_bounds, 20)  # 点击全屏上的清晰度按钮
        else:
            self.driver.find_element_by_id(float_button_id).click()

    def play_collect_appoint_stream(self):
        # 播放直播节目
        self.bottom_navigation("直播")
        common.delayed_get_element(self.driver,
                                   5,
                                   ("xpath", "//*[@resource-id='dopool.player:id/common_rcy']/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]")).click()
        common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/iv_collection")).click()
        common.delayed_get_element(self.driver,
                                   5,
                                   ("xpath","//*[@resource-id='dopool.player:id/epgListRV']/android.view.ViewGroup[4]/android.widget.TextView[3]")).click()
        common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/backImage")).click()


    def watch_vip_video(self):
        # 播放点播VIP视频
        video_xpath = "//*[@resource-id='dopool.player:id/common_rcy']/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]"
        common.delayed_get_element(self.driver, 5, ("xpath", video_xpath)).click()
        common.delayed_get_element(self.driver, 5, ("id", "dopool.player:id/pre_adView_skip")).click()
        base.click_play_float_button("portrait_seekBar", [(334, 414.5)])












