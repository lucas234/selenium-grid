import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        ds = {'platform': 'ANY',
              'browserName': "chrome",
              'version': '',
              'javascriptEnabled': True
              }
        self.dr = webdriver.Remote('http://localhost:4444/wd/hub', desired_capabilities=ds)

    def test_something(self):
        self.dr.get("https://www.baidu.com")
        self.assertEqual(self.dr.name, "chrome")

    def test_search_button(self):
        self.dr.get("https://www.baidu.com")
        self.assertTrue(self.dr.find_element_by_id("su").is_displayed())

    def tearDown(self):
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
