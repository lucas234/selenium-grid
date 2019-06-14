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
            driver = webdriver.Remote(desired_capabilities=browser, command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub" % (USERNAME, API_KEY) )
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
