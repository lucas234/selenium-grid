from selenium import webdriver
import time

# dr = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
# dr = webdriver.Firefox(executable_path="./drivers/geckodriver.exe")
# dr = webdriver.Ie(executable_path="./drivers/IEDriverServer.exe")
dr = webdriver.Edge(executable_path="./drivers/MicrosoftWebDriver.exe")
print dr.name
print dr.title
dr.get('https://www.baidu.com/')
dr.maximize_window()
time.sleep(2)
# open new window
# JS1 = 'window.open("https://www.sogou.com");'
# dr.execute_script(JS1)
# time.sleep(2)
# update title
JS1 = "document.title='xxxxxx';"
dr.execute_script(JS1)
# popup title
time.sleep(1)
print dr.title
# JS2 = r"alert($(document).attr('title'));"
# dr.execute_script(JS2)

# JS3=r"alert('hello, world!');"
# dr.execute_script(JS3)


def scroll(driver):
    driver.execute_script(""" 
    (function () {
        var y = document.body.scrollTop; 
        var step = 100; window.scroll(0, y); 
        function f() { 
            if (y < document.body.scrollHeight) { 
                y += step; window.scroll(0, y); 
                setTimeout(f, 50); } 
            else { window.scroll(0, y); 
                    document.title += "scroll-done"; } 
                    } 
            setTimeout(f, 1000); })(); """)


dr.find_element_by_id("kw").send_keys("selenium")
dr.find_element_by_id("su").click()
# scroll(dr)

