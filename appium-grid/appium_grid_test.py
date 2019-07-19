# coding=utf-8
import unittest
from appium import webdriver
import time
import os

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class AndroidSimpleTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.0',
            'deviceName': '520381b347dd148b',
            "app": PATH("./test-app.apk"),
            # 声明中文
            "unicodeKeyboard": 'True',
            # 声明中文，否则不支持中文
            "resetKeyboard": 'True',
            # 执行时不重新安装包
            'noReset': 'True',
        }
        self.driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_something(self):
        self.driver.find_element_by_accessibility_id("buttonStartWebviewCD").click()
        input_field = self.driver.find_element_by_id('name_input')
        time.sleep(1)
        input_field.clear()
        input_field.send_keys('Appium User')
        self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"Send me your name!\")").click()
        self.driver.implicitly_wait(4)
        self.assertTrue(self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"This is my way of saying hello\")").is_displayed())
        self.driver.find_element_by_id("goBack").click()


if __name__ == '__main__':
    unittest.main()
