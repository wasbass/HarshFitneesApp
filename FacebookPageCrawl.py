from os import sep, system
from bs4 import BeautifulSoup
import time
from selenium import webdriver
import csv
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
email = ""
password = ""

def login(e,p):
  driver.get("https://www.facebook.com/")
  driver.find_element_by_id("email").send_keys(e)
  driver.find_element_by_id("pass").send_keys(p)
  driver.find_element_by_name("login").click()
  driver.implicitly_wait(5)

login(email,password)
driver.get("https://www.facebook.com/phoenix.cheng.96")
driver.implicitly_wait(10)

def scroll(scrolltimes=1):
  for i in range(scrolltimes):
    #每一次頁面滾動都是滑到網站最下方
    js = 'window.scrollTo(0, document.body.scrollHeight);'
    driver.execute_script(js)
    time.sleep(3)
    content_more = driver.find_elements_by_xpath("//div[starts-with(@id,'jsc_c')]/div/div/span/div/div/div")
    for more in content_more:
      try:
        more.click()
        print("O",end="")
      except:
        print("X",end="")
        continue
    print("")

scroll(10)

soup = BeautifulSoup(driver.page_source, "html.parser")
allbox = soup.find_all("div", class_ = "rq0escxv l9j0dhe7 du4w35lb hybvsw6c io0zqebd m5lcvass fbipl8qg nwvqtn77 k4urcfbm ni8dbmo4 stjgntxs sbcfpzgs")
articlebox = allbox[5:-3] #第6項開始才是貼文，最後2項會重複

print("抓到{}篇文章".format(len(articlebox)))
n = len(articlebox)

#創立csv檔
with open("chang.csv" ,mode= "w",encoding="utf-8-sig" , newline='') as file:
    writer = csv.writer(file ,delimiter=',')
    writer.writerow(["date","likes","comments","shares","content"])

def getword(word,sep):
  w = word.text
  w = w.split(sep)[0]
  return w

def writeincsv(L):
  with open("chang.csv" ,mode= "a+",encoding="utf-8-sig" , newline='') as file:
    writer = csv.writer(file ,delimiter=',')
    writer.writerow(L)

for i in range(n):
  time = articlebox[i].find("a" , class_ = "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw")
  try:
    date = time.text
    date = date.replace("=","")
    #print(date)
  except:
    date = ""

  thumb = articlebox[i].find("div" , class_ = "bp9cbjyn j83agx80 buofh1pr ni8dbmo4 stjgntxs")
  try:
    count = getword(thumb, sep = " ")
  except:
    count = ""

  c_s = articlebox[i].find_all("span",class_ = "d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh m9osqain")
  try:
    if len(c_s) == 1:
      if "留言" in c_s[0].text:
        comment = getword(c_s[0] , sep = "則")
        share = ""
      else:
        comment = ""
        share = getword(c_s[0] , sep = "次")
    elif len(c_s) == 2:
      comment = getword(c_s[0] , sep = "則")
      share   = getword(c_s[1] , sep = "次")
  except:
    comment = ""
    share   = ""

  try:
    content = articlebox[i].find("div" , class_ = "ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a").text
  except:
    try:
      content = articlebox[i].find("div" , class_ = "ecm0bbzt hv4rvrfc e5nlhep0 dati1w0a").text
    except:
      try:
        content = articlebox[i].find("div" , class_ = "qt6c0cv9 hv4rvrfc dati1w0a jb3vyjys").text
      except:
        content = ""
  L = [date , count , comment , share,content]
  writeincsv(L)

driver.close()
