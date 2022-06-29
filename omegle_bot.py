import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random


msg1 = "I'm a bot, I was coded to wish people well. Have an amazing day!"
msg2 = "I'm a bot, it's wonderful to meet you."
msg3 = "I'm a bot coded to wish people well :]"
msg4 = "I'm a bot designed to spread positivity"

messages = [msg1,msg2,msg3,msg4]
greetings = ["Heyo!","Henlo","Hey!","Hi!"]
endings = ["You're an amazing person.","Thank you so much for being you, you got this man.","Take care and stay safe.","Have an amazing day."]

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.omegle.com")

time.sleep(6)

n = 0

while True:
    try:
        greeting_msg = random.choice(greetings)
        main_msg = random.choice(messages)
        ending_msg = random.choice(endings)

        text_area = driver.find_element("xpath", "/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[2]/div/textarea")
        send_btn = driver.find_element("xpath", "/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[3]/div/button")
        new_btn = driver.find_element("xpath", "/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[1]/div/button")

        for letter in greeting_msg:
            text_area.send_keys(letter)

        send_btn.click()
        time.sleep(1)

        for letter in main_msg:
            text_area.send_keys(letter)
            time.sleep(0.001)
            n += 1

        send_btn.click()
        time.sleep(1)

        for letter in ending_msg:
            text_area.send_keys(letter)
            time.sleep(0.001)

        send_btn.click()
        time.sleep(1)


        new_btn.click()
        new_btn.click()
        new_btn.click()
        time.sleep(2)

    except:
        exit_btn = driver.find_element("xpath", "/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[1]/div/button")
        exit_btn.click()
        time.sleep(1)
