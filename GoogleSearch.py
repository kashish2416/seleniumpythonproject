# To validate google landing page

import unittest
from selenium import webdriver
import time

class MyTestCase(unittest.TestCase):
    def test01(self):

        filePath ="C:\\Users\\kashish\\OneDrive\\Desktop\\TraningStuff\\selenium\\drivers\\chromedriver.exe"
        url = "https://www.google.com/"
        driver = webdriver.Chrome(filePath)
        time.sleep(1)

        driver.maximize_window()
        time.sleep(1)

        driver.fullscreen_window()
        time.sleep(2)
        driver.get(url)



if __name__ == '__main__':
    unittest.main()