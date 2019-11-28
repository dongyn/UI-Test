"""
该类主要是存放一些公共方法，比如：元素查找、截屏、操作Excel等等
"""
# 导入日志模块
# 读excel模块
import xlrd, time, os, shutil
from comm.Log import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

log = Logger()

'''
filePath:current path
qr：file name format
'''
filePath = os.path.split(os.path.dirname(__file__))[0]
'''
find element
flag:True or Flase
xpath:element xpath
0：text
1: id
2: name
'''

# class common():
#     def __init__(driver):
#         self.driver=driver
#         self.wait = WebDriverWait(driver, 30)

def delayed_get_element(driver, second=0, loc=("id", "dopool.player:id/xxx")):
    return WebDriverWait(driver, second).until(EC.presence_of_element_located(loc))

def isElementExist(flag, driver, xpath):
    isExist = True
    if flag == "xpath":
        # noinspection PyBroadException
        try:
            driver.find_element_by_xpath(xpath).is_displayed()
        except Exception as e:
            log.error(f"查找的元素不存在{xpath}{e}")
            isExist = False
        return isExist
    elif flag == "id":
        # noinspection PyBroadException
        try:
            driver.find_element_by_id(xpath).is_displayed()
        except Exception as e:
            log.error(f"查找的元素不存在{xpath}{e}")
            isExist = False
        return isExist
    elif flag == "name":
        try:
            driver.find_elements_by_name(xpath).is_displayed()
        except Exception as e:
            log.error(f"查找的元素不存在{xpath}{e}")
            isExist = False
        return isExist


'''
Screenshot function
'''


def Screenshot1(driver):
    rq = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
    # log文件的存放路径
    imPath = filePath + '/result/image/' + rq + '.png'
    driver.get_screenshot_as_file(imPath)


def Screenshot2(driver, imPath):
    driver.get_screenshot_as_file(imPath)


'''
Delete folder content
path: folder path
'''


def delFile(path):
    shutil.rmtree(path)
    os.makedirs(path)


'''
excel_name:excel file name
sheet_name:sheet name
return:sheet value
'''


def get_excel_value(sheet_name):
    cls = []
    excel_path = filePath + '/data/testCase.xls'
    workbook = xlrd.open_workbook(excel_path)
    sheet = workbook.sheet_by_name(sheet_name)
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != 'case_Name':
            cls.append(sheet.row_values(i))
    return cls


# Screen swipe
# get Screen size
def getScreenSize(driver):
    size = driver.get_window_size()
    # get width
    width = size['width']
    # get height
    height = size['height']
    return width, height

# swipe up Screen
def swipeUp(driver, n = 1/2):
    # 获取屏幕的高
    x = driver.get_window_size()['width']
    # 获取屏幕宽
    y = driver.get_window_size()['height']
    time.sleep(5)
    driver.swipe(1/2 * x, 1/2 * y, n * x, 1/7 * y)


# swipe down Screen
def swipeDown(driver, n = 1/7):
    # 获取屏幕的高
    x = driver.get_window_size()['width']
    # 获取屏幕宽
    y = driver.get_window_size()['height']
    time.sleep(5)
    driver.swipe(1/2 * x, n * y, 1/2 * x, 6/7 * y)


# swipe left Screen
def swipeLeft(driver):
    # 获取屏幕的高
    # print("swipeLeft")
    x = driver.get_window_size()['width']
    # 获取屏幕宽
    y = driver.get_window_size()['height']
    time.sleep(3)
    driver.swipe(6/7 * x, 1/2 * y, 1/7 * x, 1/2 * y)


# swipe right Screen
def swipeRight(driver):
    # 获取屏幕的高
    x = driver.get_window_size()['width']
    # 获取屏幕宽
    y = driver.get_window_size()['height']
    time.sleep(5)
    driver.swipe(1/7 * x, 1/2 * y, 5/7 * x, 1/2 * y, 200)

'''
system window pop
n：search times
'''
def window_pop(driver, xpath, n):
    for i in range(n):
        try:
            delayed_get_element(driver, 15, ("xpath", xpath)).click()
            log.info(f'定位成功{xpath}')
        except Exception as e:
            log.error(f'定位播放pop权限框失败{e}')


def find_id(driver, id):
    '''
    寻找元素
    :return:
    '''
    try:
        driver.find_element_by_id(id)
        return True
    except:
        log.error(f'未定位到元素：{id}')
        return False
#
#
def find_name(driver, name):
    '''
   判断页面是否存在某个元素
   :param name: text
   :return:
   '''
    xpath = f"//*[@text='{name}']"
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        log.error(f'未定位到元素：{name}')
        return False

def get_name(driver, name):
    '''
    定位页面text元素
    :param name:
    :return: 页面text元素
    '''
    xpath = f"//*[@text='{name}']"
    try:
        return delayed_get_element(driver, 15,("xpath", xpath))
    except:
        log.error(f'未定位到元素：{name}')


def get_xpath(driver, xpath):
    '''
    定位页面xpath元素
    :param xpath:
    :return:
    '''
    try:
        return delayed_get_element(driver, 15,("xpath", xpath))
    except:
        log.error(f'未定位到元素：{xpath}')


def get_ids(driver, id):
    '''
    定位页面resouce-id元素组
    :param id:
    :return:列表
    '''
    try:
        return delayed_get_element(driver, 10,("id", id))
    except:
        log.error(f'未定位到元素：{id}')

#
def page(driver, name):
    '''
    返回至指定页面
    :return:
    '''
    i = 0
    while i < 10:
        i = i + 1
        try:
            xpath = f"//*[@text='{name}']"
            driver.find_element_by_xpath(xpath)
            time.sleep(2)
            break
        except:
            os.popen("adb shell input keyevent 4")
            try:
                xpath = "//*[@text='确定']"
                driver.find_element_by_xpath(xpath).click()
                time.sleep(2)
            except:
                os.popen("adb shell input keyevent 4")
            try:
                driver.find_element_by_xpath("//*[@text='工作台']")
                time.sleep(2)
                break
            except:
                os.popen("adb shell input keyevent 4")

def click_screen_point(driver, x_size, y_size, millisecond):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    driver.tap([(x_size * x, y_size * y)], millisecond)

