# coding=utf-8

from selenium import webdriver
from time import sleep

browser = webdriver.Chrome(executable_path="/Users/kHRYSTAL/Downloads/chromedriver")
browser.get("https://jinshuju.net/f/EwZkQr")
sleep(1)
browser.set_window_size(1400, 800)
name = browser.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div/form/div[3]/div[1]/div[2]/div/div/div[2]/div[1]/div/span/span/input")
name.send_keys("张三")  # 姓名
student_type = browser.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div/form/div[3]/div[1]/div[3]/div/div/div[2]/div[1]/div/span/div/div[1]/div/div/label/span[1]/input")
student_type.click()
student_mingzu = browser.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div/form/div[3]/div[1]/div[5]/div/div/div[2]/div[1]/div/span/input")
student_mingzu.send_keys("汉")
student_date = browser.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div/form/div[3]/div[1]/div[7]/div/div/div[2]/div[1]/div/span/div/span/input")
student_date.send_keys("2019-04-25")
student_number = browser.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div/form/div[3]/div[1]/div[9]/div/div/div[2]/div[1]/div/span/input")
student_number.send_keys("12020375335009")
student_phone = browser.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div/form/div[3]/div[1]/div[11]/div/div/div[2]/div[1]/div/span/div/span/input")
student_phone.send_keys("13900000000")
student_address = browser.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div/form/div[3]/div[1]/div[13]/div/div/div[2]/div[1]/div/span/input")
student_address.send_keys("天津市西青区")
student_sub = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/form/div[5]/div[1]/button")
student_sub.click()
