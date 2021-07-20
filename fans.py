from bs4 import BeautifulSoup as BS
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

driver.find_element_by_id("email").clear()
driver.find_element_by_id("email").send_keys("waswang@gmail.com")
driver.find_element_by_id("pass").clear()
driver.find_element_by_id("pass").send_keys("")
driver.find_element_by_name("login").click()
time.sleep(3)

driver.get("https://www.facebook.com/phoenix.cheng.96")

def scroll(scrolltimes=1):
  for i in range(scrolltimes):
    #每一次頁面滾動都是滑到網站最下方
    js = 'window.scrollTo(0, document.body.scrollHeight);'
    driver.execute_script(js)
    print("+",end = "")
    time.sleep(3)

scroll(5)
print("")

soup = BS(driver.page_source, "html.parser")
# viewbox = soup.find_all("div", class_ = "bp9cbjyn m9osqain j83agx80 jq4qci2q bkfpd7mw a3bd9o3v kvgmc6g5 wkznzc2l oygrvhab dhix69tm jktsbyx5 rz4wbd8a osnr6wyh a8nywdso s1tcr66n")

# print("抓到{}篇文章".format(len(viewbox)))
# for v in viewbox:
#   thumbs = v.find_all("div" , class_ = "bp9cbjyn j83agx80 buofh1pr ni8dbmo4 stjgntxs")
#   for thumb in thumbs:
#     count = thumb.text
#     print(count.split(" ")[0],"個讚",end = ",")

#   c_s = v.find_all("span",class_ = "d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh m9osqain")
#   if len(c_s) >= 1:
#     print(c_s[0].text,end = ",")
#   if len(c_s) == 2:
#     print(c_s[1].text,end = "")
#   print("")

contents = soup.find_all("div" , class_ = "ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a")
print("找到{}篇文章".format(len(contents)))
for content in contents:
  print(content.text)
