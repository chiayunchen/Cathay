'''
1. 使用Chrome App到國泰世華銀行官網(https://www.cathaybk.com.tw/cathaybk/)並將畫面截圖。
開啟網頁，並截圖
    >>1. 截圖功能
    >>2. 等待元素方式
2. 點選左上角選單，進入 個人金融 > 產品介紹 > 信用卡列表，需計算有幾個項目並將畫面截圖。
    1. 進入信用卡列表選單後截圖
    2. 計算有幾項目在信用卡選單下面
    >>1. 元素查詢方式
3. 個人金融 > 產品介紹 > 信用卡 > 卡片介紹 > 計算頁面上所有(停發)信用卡數量並截圖
    1. 進入信用卡列表選單後計算(停發)信用卡數量並截圖
    2. 比對計算(停發)信用卡數量與截圖數量相同
    >>1. 元素查找方式
    >>2. 截圖數量計算
Overall:
1. Coding style
2. Error handling
3. 是否有考慮跨平台支援
4. Logging
'''

import time
import logging
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_UI():
    #1.setup log path and create log directory
    logName = 'MyProgram.log'
    logDir = 'log'
    logPath = logDir + '/' + logName

    #create log directory 
    os.makedirs(logDir,exist_ok=True)

    #2.create logger, then setLevel
    allLogger = logging.getLogger('allLogger')
    allLogger.setLevel(logging.DEBUG)

    #3.create file handler, then setLevel
    #create file handler
    fileHandler = logging.FileHandler(logPath,mode='w')
    fileHandler.setLevel(logging.DEBUG)

    #4.create stram handler, then setLevel
    #create stream handler
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.DEBUG)

    #5.create formatter, then handler setFormatter
    AllFormatter = logging.Formatter("%(asctime)s - [line:%(lineno)d] - %(levelname)s: %(message)s")
    fileHandler.setFormatter(AllFormatter)
    streamHandler.setFormatter(AllFormatter)

    #6.logger addHandler
    allLogger.addHandler(fileHandler)
    allLogger.addHandler(streamHandler)

    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    op = webdriver.ChromeOptions()
    op.add_experimental_option("mobileEmulation", mobile_emulation)
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    driver.get("https://www.cathaybk.com.tw/cathaybk/")
    time.sleep(2)

    # 等待搜尋欄位及活動專區出現
    try:
        element_activity = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/section/div[3]/div[4]/div/div[6]/a/div[1]/img[1]')))
        allLogger.info('活動專區 XPATH is located')
        element_search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/section/div[3]/div[3]/div/div/div[1]/div/a[1]')))
        allLogger.info('搜尋欄位 XPAHT is located')
    except Exception as e:
        allLogger.exception(e)
    finally:
        time.sleep(2)

    try:
        driver.save_screenshot('1_homepage.png')
        allLogger.info('1_homepage.png is saved')
    except Exception as e:
        allLogger.exception(e)
    
#    driver.execute_script("window.scrollTo(0, 740);")
#    driver.save_screenshot('1_homepage_02.png')
#    driver.execute_script("window.scrollTo(740, 1500);")
#    driver.save_screenshot('1_homepage_03.png')
#    driver.execute_script("window.scrollTo(1501, 2300);")
#    driver.save_screenshot('1_homepage_04.png')
#    driver.execute_script("window.scrollTo(2501, 3000);")
#    driver.save_screenshot('1_homepage_05.png')


    # 點選左上角選單
    try:
        button_search = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]')
        allLogger.info('左上角選單 XPATH is located')
    except Exception as e:
        allLogger.exception(e)
    button_search.click()

    # 點選產品介紹
    try:
        button_search = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1]')
        allLogger.info('產品介紹 XPATH is located')
    except Exception as e:
        allLogger.exception(e)
    button_search.click()

    # 點選信用卡
    try:
        button_search = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]')
        allLogger.info('信用卡 XPATH is located')
    except Exception as e:
        allLogger.exception(e)
    button_search.click()

    # 確定項目出現
    try:
        element_search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a[1]')))
        allLogger.info('項目 XPATH is located')
    except Exception as e:
        allLogger.exception(e)
    finally:
        time.sleep(2)
    driver.save_screenshot('2_creditcardlist.png')
    allLogger.info('2_creditcardlist.png is saved - 總共8個項目')

# 2. 計算有幾項目在信用卡選單下面 - 8 
# /html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a[1]
# /html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a[2]
# /html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a[3]
# /html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a[4]
# /html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a[5]
# /html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a[6]
# /html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a[7]
# /html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a[8]

    # 點選卡片介紹
    try:
        button_search = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a[1]')
        allLogger.info('卡片介紹 XPATH is located')
    except Exception as e:
        allLogger.exception(e)
    button_search.click()

    # 點選停發卡
    try:
        driver.execute_script("window.scrollTo(3188, 3888);")
        button_search = driver.find_element(By.XPATH, '/html/body/div[1]/main/article/section[6]/div/div[1]/div/div/div[2]')
        allLogger.info('Scroll down to 停發卡')
    except Exception as e:
        allLogger.exception(e)
    
    # 確定卡片出現
    try:
        element_search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[1]/div[1]/div/div[1]')))
        allLogger.info('停發卡片 XPATH is located')
    except Exception as e:
        allLogger.exception(e)
    finally:
        time.sleep(2)
    driver.save_screenshot('3_creditcard_1.png')
    allLogger.info('3_creditcard_1 is saved')

    for i in range(2, 14):
        # 點選向右移動畫面
        xpath = f'/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[{i}]'
        try:
            button_search = driver.find_element(By.XPATH, xpath)
            allLogger.info('向右移動 XPATH is located')
        except Exception as e:
            allLogger.exception(e)
        button_search.click()
        # 確定卡片出現
        try:
            element_search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[1]/div[1]/div/div[1]')))
            allLogger.info('停發卡片 XPATH is located')
        except Exception as e:
            allLogger.exception(e)
        finally:
            time.sleep(2)
        driver.save_screenshot(f'3_creditcard_{i}.png')
        allLogger.info(f'3_creditcard_{i}.png is saved')
    allLogger.info(f'總共{i}張停發卡')

    driver.quit()
    
    #7.logger remove handler
    allLogger.removeHandler(streamHandler)
    allLogger.removeHandler(fileHandler)

assert test_UI() == None