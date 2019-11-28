#coding=utf-8
#author='Shichao-Dong'

import time, os
from appium import webdriver
from comm.Log import Logger
from selenium.common.exceptions import WebDriverException
from comm.StartAppiumServer import Sp
from comm.readConfig import ReadConfig

conf = ReadConfig()
log = Logger()

app_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "../..")), 'UI-Test', 'comm', 'apps', 'cibn.apk')
platformName = conf.get_config('platformName')
appPackage = conf.get_config('appPackage')
appActivity = conf.get_config('appActivity')
appium_port = conf.get_config('appium_port')

class webDriver:
    def __init__(self):
        self.get_device = conf.get_cmd('viewDevices')
        self.get_Version = conf.get_cmd('platformVersion')
        self.startServer = conf.get_cmd('startServer')

    def get_deviceName(self):
        values = os.popen(self.get_device).readlines()
        print(values)
        dev = values[1].split()[0]
        if len(values)-2 == 1:
            print(dev)
            log.info('可用设备为：'+ dev)
            return dev
        else:
            log.warn('暂未获取到可用设备')
            print('No device found')

    def get_platformVersion(self):
        values = os.popen(self.get_Version).readlines()
        # log.info('系统版本号为：'+ str(values))
        if values != '':
            Version=values[0].split('=')[1]
            print(Version)
            log.info('可用设备版本号为：'+Version)
            return Version.strip()
        else:
            log.warn('暂未获取到可用设备')
            print('No device found')

    def get_driver(cls):
        desired_caps = {
            'platformName': platformName,
            'deviceName': webDriver().get_deviceName(),
            # 'platformVersion': webDriver().get_platformVersion(),
            'platformVersion': '9',
            'appPackage': appPackage,
            'appActivity': appActivity,
            'automationName': 'uiautomator2',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True,
            'newCommandTimeout': 6000,
            'app': app_path
        }
        try:
            # Sp().stop_appium()
            # Sp().start_appium()  #自动化全跑的话再运行
            driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub'%appium_port, desired_caps)
            time.sleep(4)
            print("driver加载成功")
            return driver
        except WebDriverException:
            print("driver加载失败")

    # @classmethod
    # def setUpClass(cls):
    #     global driver, countA
    #     # appium启动服务只运行一次
    #     if countA == 1:
    #         # 启动appium服务
    #         Sp().start_appium()  # 自动化全跑的话再运行
    #     countA = countA + 1
    #     cls.get_driver()

    # @classmethod
    # def tearDownClass(cls):
    #     # 关闭浏览器驱动
    #     cls.driver.quit()
    #     # 卸载app
    #     cls.driver.removeApp(appPackage);
    #     # 关闭appium服务
    #     Sp().stop_appium()

# if __name__ == "__main__":
#     webDriver().get_driver()
#     cur_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), ".."))) + "\\testSmoke"
#     print(cur_path)
