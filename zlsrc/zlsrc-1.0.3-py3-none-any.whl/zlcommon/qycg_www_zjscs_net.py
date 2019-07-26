import re
from math import ceil
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from zlsrc.util.etl import est_html, est_meta, add_info
import time



def f1(driver, num):
    locator = (By.XPATH, "//div[@class='List3 BorderCCCNoTop']/ul/li[last()]/a")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator)).text.strip()

    locator = (By.XPATH, "//div[@class='List3 BorderCCCNoTop']/div/div")
    total_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator)).text.strip()
    cnum = re.findall(r'(\d+)/', total_page)[0]
    url = driver.current_url

    if int(cnum) != int(num):
        val = driver.find_element_by_xpath("//div[@class='List3 BorderCCCNoTop']/ul/li[last()]/a").get_attribute('href')[-12:]

        driver.execute_script("if(this.value==1){location='index.jhtml'}else{location='index_'+'%d'+'.jhtml'}this.disabled='disabled'" %(num))

        locator = (By.XPATH, '//div[@class="List3 BorderCCCNoTop"]/ul/li[last()]/a[not(contains(@href,"%s"))]'%(val))
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(locator))

    data = []
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.find('div', class_=re.compile('List3 BorderCCCNoTop')).ul
    lis = ul.find_all('li')

    for tr in lis:
        a = tr.find('a')
        try:
            name = a['title']
        except:
            name = a.text.strip()

        if 'http' in a['href']:
            href = a['href']
        else:
            href = 'http://www.zjscs.net:81' + a['href']
        ggstart_time = tr.find('span').text.strip()
        temp = [name, ggstart_time, href]
        data.append(temp)

    df = pd.DataFrame(data=data)
    df['info'] = None
    return df


def f2(driver):
    locator = (By.XPATH, "//div[@class='List3 BorderCCCNoTop']/ul/li[last()]/a")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator)).text.strip()

    locator = (By.XPATH, "//div[@class='List3 BorderCCCNoTop']/div/div")
    total_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator)).text.strip()
    num = re.findall(r'/(\d+)', total_page)[0]
    driver.quit()
    return int(num)


def f3(driver, url):
    driver.get(url)
    try:
        locator = (By.XPATH, "//div[@class='Padding10 Content top10'][string-length()>100]")
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(locator))
    except:
        locator = (By.XPATH, "//div[@class='Padding10 Content top10']/p")
        WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located(locator))
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
    div=soup.find('div',class_='W980 center WhiteBg paddingLR10')
    if div == None:raise ValueError
    return div


data = [
    ["qy_zhaobiao_gg",
     "http://www.zjscs.net:81/cggg/index.jhtml",
     ["name", "ggstart_time", "href", "info"], f1, f2],

    ["qy_zhongbiaohx_gg",
     "http://www.zjscs.net:81/jggg/index.jhtml",
     ["name", "ggstart_time", "href", "info"], f1, f2],

    ["qy_biangeng_gg",
     "http://www.zjscs.net:81/sxgz/index.jhtml",
     ["name", "ggstart_time", "href", "info"], f1, f2],

    ["qy_zgys_gg",
     "http://www.zjscs.net:81/zgys/index.jhtml",
     ["name", "ggstart_time", "href", "info"], f1, f2],

]




def work(conp, **args):
    est_meta(conp, data=data, diqu="中捷通信有限公司", **args)
    est_html(conp, f=f3, **args)


if __name__ == "__main__":
    work(conp=["postgres", "since2015", "192.168.3.171", "zlest1", "www_zjscs_net"])


    # for d in data:
    #     driver=webdriver.Chrome()
    #     url=d[1]
    #     print(url)
    #     driver.get(url)
    #     df = f2(driver)
    #     print(df)
    #     driver = webdriver.Chrome()
    #     driver.get(url)
    #
    #     df=f1(driver, 12)
    #     print(df.values)
    #     for f in df[2].values:
    #         d = f3(driver, f)
    #         print(d)
