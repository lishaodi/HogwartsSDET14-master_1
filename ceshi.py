from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions


class TestHogwards():

  def setup(self):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("w3c",False)
    self.driver = webdriver.Chrome(options=option)
    self.driver.maximize_window()
  def teardown(self):
    self.driver.quit()
  # def test_hogwarts(self):
  #   #driver = webdriver.Chrome()
  #   self.driver.get("https://testerhome.com/account/sign_in")
    # ele = self.driver.find_element_by_id("kw")
    # ele_search = self.driver.find_element_by_id("su")
    # ele.send_keys("ceshi")
    # action = TouchActions(self.driver)
    # action.tap(ele_search).perform()
    #
    # action.scroll_from_element(ele,0,10000).perform()
    # sleep(3)
  def test_from(self):
    self.driver.get("https://testerhome.com/account/sign_in")
    self.driver.find_element_by_id("user_login").send_keys("123")
    self.driver.find_element_by_id("user_password").send_keys("password")
    self.driver.find_element_by_id("user_remember_me").click()
    self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input').click()
    sleep(5)
