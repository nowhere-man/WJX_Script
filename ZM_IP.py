'''
获取芝麻ip的json格式
芝麻ip：获取IP有效时间5-25分钟，获取不消耗次数，使用才消耗次数
'''
import time
import pyperclip
import selenium
import requests
import datetime
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import Config


def get_driver():
    options = webdriver.ChromeOptions()
    path = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(executable_path=path,options=options)
    # 防止自动化检测
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',{'source':'Object.defineProperty(navigator,"webdriver",{get:()=>undefined})'})
    return driver


url1 = "https://jahttp.zhimaruanjian.com/users_getapi/"

def logion(driver):
    try:
        # 关闭广告
        driver.find_element(By.XPATH, '/html/body/div[5]/div[9]/div/div[1]/span').click()
        # 点击登录
        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/a').click()
    except:
        pass
    # 输入账号密码
    driver.find_element(By.XPATH, '//*[@id="login_phone"]').send_keys("你的账号")
    driver.find_element(By.XPATH, '//*[@id="login_password"]').send_keys("你的密码")
    # 获取滑块位置
    sour = driver.find_element(By.CSS_SELECTOR,'#nc_2_n1z')
    # 获取滑条
    ele = driver.find_element(By.CSS_SELECTOR,'#nc_2__scale_text > span')
    # 点击滑块暂停0.5s（防止拖动太快被检测）
    driver.find_element(By.CSS_SELECTOR,'#nc_2_n1z').click()
    time.sleep(0.5)
    # 拖动滑块滑条末尾
    ActionChains(driver).drag_and_drop_by_offset(sour, ele.size['width'], -sour.size['height']).perform()
    # 点击登录
    driver.find_element(By.XPATH, '//*[@id="login"]').click()

def put_request(driver,batch):
    input = driver.find_element(By.XPATH, '//*[@id="api-content"]/div[1]/div/div/div[1]/div[5]/div[2]/div[1]/div/div[1]/div/input')
    input.clear()    # 清空输入框
    input.clear()    # 再清空一次
    time.sleep(0.5)
    input.send_keys(f'{batch}')  # 输入需要的ip数量
    driver.find_element(By.XPATH, '//*[@id="api-content"]/div[1]/div/div/div[1]/div[8]/div[2]/div/label[2]').click()  # ip的稳定时长5-25分钟
    driver.find_element(By.XPATH, '//*[@id="api-content"]/div[1]/div/div/div[1]/div[9]/div[2]/div/label[2]/span').click() # 选择json
    driver.find_element(By.XPATH, '//*[@id="api-content"]/div[1]/div/div/div[1]/div[13]/div[2]/div/label[2]').click() # 选择城市
    driver.find_element(By.XPATH, '//*[@id="api-content"]/div[1]/div/div/div[1]/div[14]/div[2]/div[2]/div/label[1]/span[1]/span').click() # 北京
    driver.find_element(By.XPATH, '//*[@id="api-content"]/div[1]/div/div/div[1]/div[14]/div[2]/div[2]/div/label[27]/span[1]/span').click() # 陕西
    driver.find_element(By.XPATH, '//*[@id="api-content"]/div[1]/div/div/div[1]/div[14]/div[2]/div[2]/div/label[18]/span[1]/span').click() # 湖南
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="api-content"]/div[1]/div/div/div[1]/div[19]/div[2]/div').click() # 点击生成API

def get_json(copied_url):
    res = requests.post(copied_url)
    result = res.text
    return result


if __name__ == '__main__':
    config = Config.Config()
    driver = get_driver()   # 获取driver
    driver.get(url1)        # 打开网站
    driver.find_element(By.XPATH,'//*[@id="api-content"]/div[1]/div/div/div[1]/div[19]/div[2]/div').click() # 点击生成API
    time.sleep(0.5)         # 等待登录页面加载
    logion(driver)          # 登录
    time.sleep(1)           # 等待登录成功
    put_request(driver,config.batch)     # 再次填充要求
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="api-content"]/div[1]/div/div/div[1]/div[19]/div[2]/div').click() # 点击生成API
    driver.find_element(By.XPATH, '//*[@id="api-content"]/div[1]/div/div/div[1]/div[20]/div[1]/div[2]/div[2]/a[1]').click() # 点击复制链接
    time.sleep(1)         # 等待复制
    copied_url = pyperclip.paste()  # 复制剪切板内容

    # 输出剪切板url
    print('-'*50)
    print("ip地址如下：")
    print(copied_url)
    print('-'*50)

    # 得到ip的json形式（拿到10个ip）
    json_result = get_json(copied_url)
    print(json_result)

    # 将ip的json形式存入文件中
    with open('ip.json', 'w', encoding='utf-8') as f:
        f.write(json_result)
        print("写入完成!")