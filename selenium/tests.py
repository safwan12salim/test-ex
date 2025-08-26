import os
import pathlib
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

class WebPageTests(unittest.TestCase):
    
    def setUp(self):
        """Set up the webdriver before each test"""
        self.driver = webdriver.Chrome()
    
    def tearDown(self):
        """Close the webdriver after each test"""
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()
    
    def test_title(self):
        self.driver.get(file_uri("counter.html"))
        self.assertEqual(self.driver.title, "Counter")
    
    def test_increase(self):
        self.driver.get(file_uri("counter.html"))
        increase = self.driver.find_element(By.ID, 'increase')
        increase.click()
        time.sleep(0.5)
        self.assertEqual(self.driver.find_element(By.TAG_NAME, 'h1').text, "1")
    
    def test_decrease(self):
        self.driver.get(file_uri("counter.html"))
        decrease = self.driver.find_element(By.ID, 'decrease')
        decrease.click()
        time.sleep(0.5)
        self.assertEqual(self.driver.find_element(By.TAG_NAME, 'h1').text, "-1")
    
    def test_multiple_increase(self):
        self.driver.get(file_uri("counter.html"))
        increase = self.driver.find_element(By.ID, 'increase')
        for i in range(3):
            increase.click()
            time.sleep(0.2)
        time.sleep(0.5)
        self.assertEqual(self.driver.find_element(By.TAG_NAME, 'h1').text, "3")

if __name__ == "__main__":
    unittest.main()