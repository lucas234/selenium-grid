# coding=utf-8
# auther：Liul5
# date：2019/6/13 17:13
# tools：PyCharm
# Python：2.7.15

from queue import Queue
from threading import Thread
from selenium import webdriver
import time

USERNAME = "user@email.com"
API_KEY = "12345"

q = Queue(maxsize=0)

browsers = [
    {"os_api_name": "Win7x64-C2", "browser_api_name": "IE10", "name": "Python Parallel"},
    {"os_api_name": "Win8.1", "browser_api_name": "Chrome43x64", "name": "Python Parallel"},
]

# put all of the browsers into the queue before pooling workers
for browser in browsers:
    q.put(browser)

num_threads = 10


def test_runner(q):
    while q.empty() is False:
        try:
            browser = q.get()
            print("%s: Starting" % browser["browser_api_name"])
            driver = webdriver.Remote(desired_capabilities=browser,
                                      command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub" % (
                                      USERNAME, API_KEY))
            print("%s: Getting page" % browser["browser_api_name"])
            driver.get("http://crossbrowsertesting.com")
            print("%s: Quitting browser and ending test" % browser["browser_api_name"])
        except:
            print("%s: Error" % browser["browser_api_name"])
        finally:
            driver.quit()
            time.sleep(15)
            q.task_done()


for i in range(num_threads):
    worker = Thread(target=test_runner, args=(q,))
    worker.setDaemon(True)
    worker.start()

q.join()

##############################just note###################################################
# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from time import sleep

# driver = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", desired_capabilities=DesiredCapabilities.CHROME)
# driver = selenium.webdriver.remote.webdriver.WebDriver(command_executor="http://127.0.0.1:4444/wd/hub",
#                                                        desired_capabilities=DesiredCapabilities.CHROME)
# 1.实现串行多浏览器执行脚本
# 浏览器数组
# lists = ['chrome', 'firefox']

# 通过不同的浏览器执行脚本
# for browser in lists:
#     driver = webdriver.Remote(
#         command_executor='http://127.0.0.1:4444/wd/hub',
#         desired_capabilities={'platform': 'ANY',
#                               'browserName': browser,
#                               'version': '',
#                               'javascriptEnabled': True
#                               })
#     driver.get("http://www.baidu.com")
#     driver.find_element_by_id("kw").send_keys("python")
#     driver.find_element_by_id("su").click()
#     sleep(2)
# driver.quit()

# # 2.实现串行多节点（分布式）执行脚本
# d = {"http://192.168.40.220:5555/wd/hub": "chrome",
#      "http://192.168.40.220:5556/wd/hub": "firefox"}
# for host, browser in d.items():
#     driver = webdriver.Remote(
#         command_executor=host,
#         desired_capabilities={'platform': 'ANY',
#                               'browserName': browser,
#                               'version': '',
#                               'javascriptEnabled': True
#                               })
#     driver.get("http://www.baidu.com")
#     driver.find_element_by_id("kw").send_keys("python")
#     driver.find_element_by_id("su").click()
#     sleep(2)
