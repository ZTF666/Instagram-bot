from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from credentials import login,pwd

class ZTF():
    def __init__(self):
        self.driver=webdriver.Chrome()

   



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
        ZTF.unfollow(self)

    def unfollow(self):
            #open profile
        profile = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/a')
        profile.click()
        sleep(5)
        ZTF.mylist(self)

    def mylist(self):
        # get following number
        following_number = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').text
        following_number = int(following_number[0:3])
        #open up the follwing tab
        following = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        following.click()
       

        # loop through everything and unfollows

        for K in range(1, (following_number + 1)):
                sleep(5)
                unfollow = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li['+str(K)+']/div/div[3]/button')
                unfollow.click()
                sleep(7)
                confirm = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]')
                confirm.click()
                #i only unfollow 11 at a time , for some reason, if higher it results in a crash
                if(K == 11):   
                    closemod = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button')
                    closemod.click()
                    ZTF.mylist(self)
        
  

   


bot = ZTF()
bot.login()