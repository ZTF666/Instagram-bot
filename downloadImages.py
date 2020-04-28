from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from credentials import login,pwd,profile
import urllib.request



class ZTF():

    def __init__(self):

        
        ZTF.download(self)
    
    def download(self):
            self.driver=webdriver.Chrome()
            self.driver.get('https://www.instagram.com/'+profile)
        
            sleep(5)
            for i in range(1,7):
                self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                sleep(5)
            self.driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
            sleep(5)
            # article = self.driver.find_element_by_class_name('ySN3v')
            elem = self.driver.find_elements_by_class_name('FFVAD')
            file1 = open("test.txt","a+")

            for el in elem:
                file1.write(el.get_attribute('src')+'\n')

            sleep(5)

            ZTF.DownloadImages(self)

      

    def DownloadImages(self):
            c =int(0)
            my_list=[]
            with open('test.txt') as f:
                my_list = list(f)
            X = int(0)
            
            for link in my_list:
                urllib.request.urlretrieve(link,'image'+str(X)+'.jpg')
                X+=1
        

   
        


   


bot = ZTF()

