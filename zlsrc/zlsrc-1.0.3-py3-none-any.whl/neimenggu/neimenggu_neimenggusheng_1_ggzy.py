import json

import pandas as pd
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from zlsrc.util.etl import est_html, est_meta, add_info, est_meta_large




def f1(driver, num):
    locator = (By.XPATH, '//table[@class="table_text"]//tr[2]//a')
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator))
    url = driver.current_url
    cnum=re.findall('page=(\d+)',url)[0]
    #
    if num != int(cnum):
        url=re.sub('(?<=page=)\d+',str(num),url)
        val = driver.find_element_by_xpath('//table[@class="table_text"]//tr[2]//a').get_attribute('href')[-30:-2]
        driver.get(url)

        locator = (By.XPATH, "//table[@class='table_text']//tr[2]//a[not(contains(@href,'%s'))]" % val)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
    data = []
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='table_text').tbody
    lis = table.find_all('tr')[1:]
    for tr in lis[1:]:
        tds=tr.find_all('td')
        href= tr.find('a')['href']
        name = tr.find('a')['title']
        hy=tds[1].span['title']
        diqu=tds[2].span['title']
        ggstart_time=tds[-2].get_text(strip=True)
        ggend_time=tds[-1].get_text(strip=True)
        href=re.findall("http.+(?=')",href)[0]
        info=json.dumps({'hy':hy,'diqu':diqu,'ggend_time':ggend_time},ensure_ascii=False)
        tmp = [name, ggstart_time, href,info]

        data.append(tmp)
    df = pd.DataFrame(data=data)
    return df



def f2(driver):
    locator = (By.XPATH, '//table[@class="table_text"]//tr[2]//a')
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator))
    locator = (By.XPATH, '//div[@class="pagination"]/label[1]')
    total_page = WebDriverWait(driver, 30).until(EC.presence_of_element_located(locator)).text.strip()
    driver.quit()
    return int(total_page)



def f3(driver, url):
    driver.get(url)
    locator = (By.XPATH, '//div[@class="mian_list_03"][string-length()>100]')
    WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located(locator))
    before = len(driver.page_source)
    time.sleep(0.5)
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
    div = soup.find('div', class_='mian_list')
    return div


data = [
    ["gcjs_zhaobiao_gg","http://zbgg.nmgztb.com.cn/xxfbcms/category/bulletinList.html?searchDate=1994-07-16&dates=300&word=&categoryId=88&industryName=&area=&status=&publishMedia=&sourceInfo=&showStatus=&page=1",["name", "ggstart_time", "href", "info"],f1,f2,],
    ["gcjs_zhongbiaohx_gg","http://zbgg.nmgztb.com.cn/xxfbcms/category/candidateBulletinList.html?searchDate=1994-07-16&dates=300&word=&categoryId=91&industryName=&area=&status=&publishMedia=&sourceInfo=&showStatus=&page=1",["name", "ggstart_time", "href", "info"],f1,f2,],
    ["gcjs_zhongbiao_gg","http://zbgg.nmgztb.com.cn/xxfbcms/category/resultBulletinList.html?searchDate=1994-07-16&dates=300&word=&categoryId=90&industryName=&area=&status=&publishMedia=&sourceInfo=&showStatus=&page=1",["name", "ggstart_time", "href", "info"],f1,f2,],
    ["gcjs_biangeng_gg","http://zbgg.nmgztb.com.cn/xxfbcms/category/changeBulletinList.html?searchDate=1994-07-16&dates=300&word=&categoryId=89&industryName=&area=&status=&publishMedia=&sourceInfo=&showStatus=&page=1",["name", "ggstart_time", "href", "info"],f1,f2,],
    ["gcjs_zgys_gg","http://zbgg.nmgztb.com.cn/xxfbcms/category/qualifyBulletinList.html?searchDate=1994-07-16&dates=300&word=&categoryId=92&industryName=&area=&status=&publishMedia=&sourceInfo=&showStatus=&page=1",["name", "ggstart_time", "href", "info"],f1,f2,],

]
##该代码与内蒙古_neimenggusheng_2_ggzy 互相补充

def work(conp, **args):
    est_meta_large(conp, data=data, diqu="内蒙古自治区", **args)
    est_html(conp, f=f3, **args)


if __name__ == '__main__':
    work(conp=["postgres", "since2015", "192.168.3.171", "zlsrc", "neimenggu"],num=1,total=3)





