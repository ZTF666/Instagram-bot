from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from credentials import login,pwd


class ZTF():
    def __init__(self):
        self.driver=webdriver.Chrome()

    def follow(self):
        

        
        # the number 30 is just for testing , until i figure out how to load everything correctly instead of doing this lol
        for y in range(1, 10):
            self.driver.find_element_by_tag_name('body').send_keys(Keys.END)
            self.driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
            #the 140 is an approximation of how many people show up in a fully loaded suggestion tab
        for x in range(1,31) :
            sleep(5)
            follow_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/div/div/div['+str(x)+']/div[3]/button')
            follow_btn.click()
            if(x == 30):
                self.driver.refresh()
                ZTF.follow(self)



    def login(self):

            #maximazing and opening IG
        self.driver.maximize_window()
        self.driver.get('https://www.instagram.com/')
       
        

        sleep(3)
        
        
        #switching windows
        base_window = self.driver.window_handles[0]
        # this one in case there's a pop up but there isn't in ig so ...
        # popup = self.driver.switch_to_window(self.driver.window_handles[1])

        #chosing login with fb
        gotofb_login =  self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[6]/button')
        gotofb_login.click()

        #login in with the credentials
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(login)
        pass_in = self.driver.find_element_by_xpath('//*[@id="pass"]')   
        pass_in.send_keys(pwd)
        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_btn.click()

        sleep(10)
        
        pwd_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/div[2]/form/div[3]/div/label/input')
        pwd_in.send_keys(pwd)

        login_btn2 = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/div[2]/form/div[5]/button')
        login_btn2.click()
        
        sleep(5)

        notnow_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        notnow_btn.click()

        sleep(2)

        seeAll = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[3]/div[1]/a')
        seeAll.click()

        ZTF.follow(self)

   

bot = ZTF()
bot.login()