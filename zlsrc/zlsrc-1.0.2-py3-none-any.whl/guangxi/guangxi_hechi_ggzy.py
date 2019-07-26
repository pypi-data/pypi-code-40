import re
import time

from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from zlsrc.util.etl import est_meta,est_html

def f1(driver,num):
    locator = (By.XPATH,'//tr[@style="min-height: 32px;"]//a')
    WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located(locator))
    val = driver.find_element_by_xpath('//tr[@style="min-height: 32px;"]//a').get_attribute("href")[-40:]
    cnum = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//td[@class="yahei redfont"]'))).text
    if int(cnum) != int(num):
        url = re.sub(r"Paging=\d+",'Paging='+str(num),driver.current_url)
        driver.get(url)
        locator = (By.XPATH, '//tr[@style="min-height: 32px;"]//a[not(contains(@href,"%s"))]'%val)
        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(locator))
    page = driver.page_source
    body = etree.HTML(page)
    data = []
    content_list = body.xpath('//tr[@style="min-height: 32px;"]')
    for content in content_list:
        name = content.xpath("./td/a/text()")[0].strip()

        ggstart_time = content.xpath("./td[2]/text()")[0].strip()
        url = "http://218.65.221.79" + content.xpath("./td/a/@href")[0]
        temp = [name, ggstart_time, url]
        data.append(temp)
        # print(temp)
    df = pd.DataFrame(data=data)
    df["info"]=None
    return df


def f2(driver):
    total_temp = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//td[contains(text(),'末页')]"))).get_attribute("title")
    total_page = re.findall(r'第(\d+)页',total_temp)[0]
    driver.quit()
    return int(total_page)

def f3(driver, url):
    driver.get(url)
    locator = (By.ID, "tblInfo")
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(locator))
    before = len(driver.page_source)
    time.sleep(0.1)
    after = len(driver.page_source)
    i = 0
    while before != after:
        before = len(driver.page_source)
        time.sleep(0.1)
        after = len(driver.page_source)
        i += 1
        if i > 5: break
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    div = soup.find('table', id='tblInfo')
    return div


data =[

    ["gcjs_zhaobiao_gg",
     "http://218.65.221.79/gxhczbw/showinfo/biao.aspx?categorynum=001001001",
     ["name", "ggstart_time", "href", "info"], f1, f2],
    ["gcjs_biangeng_gg",
     "http://218.65.221.79/gxhczbw/showinfo/biao.aspx?CategoryNum=001001002",
     ["name", "ggstart_time", "href", "info"], f1, f2],
    ["gcjs_kongzhijia_gg",
     "http://218.65.221.79/gxhczbw/showinfo/biao.aspx?CategoryNum=001001004",
     ["name", "ggstart_time", "href", "info"], f1, f2],
    ["gcjs_zhongbiaohx_gg",
     "http://218.65.221.79/gxhczbw/showinfo/biao.aspx?CategoryNum=001001005",
     ["name", "ggstart_time", "href", "info"], f1, f2],


    ["zfcg_zhaobiao_gg",
     "http://218.65.221.79/gxhczbw/showinfo/biao.aspx?CategoryNum=001004001",
     ["name", "ggstart_time", "href", "info"], f1, f2],
    ["zfcg_biangeng_gg",
     "http://218.65.221.79/gxhczbw/showinfo/biao.aspx?CategoryNum=001004002",
     ["name", "ggstart_time", "href", "info"], f1, f2],
    ["zfcg_zhongbiaohx_gg",
     "http://218.65.221.79/gxhczbw/showinfo/biao.aspx?CategoryNum=001004004",
     ["name", "ggstart_time", "href", "info"], f1, f2],
    ["zfcg_kongzhijia_gg",
     "http://218.65.221.79/gxhczbw/showinfo/biao.aspx?CategoryNum=001004005",
     ["name", "ggstart_time", "href", "info"], f1, f2],

]

def work(conp,**arg):
    est_meta(conp, data=data, diqu="广西省河池市",**arg)
    est_html(conp, f=f3,**arg)



if __name__ == "__main__":

    conp=["postgres", "since2015", "192.168.3.171", "guangxi", "hechi"]
    import sys
    arg=sys.argv
    if len(arg) >3:
        work(conp,num=int(arg[1]),total=int(arg[2]),html_total=int(arg[3]))
    elif len(arg) == 2:
        work(conp, html_total=int(arg[1]))
    else:
        work(conp)
