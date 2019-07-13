from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
					 
					 
driver = webdriver.Remote(
   command_executor="http://TKoYSdHrqgQDvK1groPP7jQIM2hLMrQw:14kK8R1pYHSkhJrzY6eVgVuSOCurUaNL@CHUNIN1103.gridlastic.com:80/wd/hub",
   desired_capabilities={
            "browserName": "chrome",
            "version": "latest",
            "video": "True",
            "platform": "VISTA",
            "platformName": "windows"
        })
try:
    driver.implicitly_wait(30)
    driver.maximize_window() # Note: driver.maximize_window does not work on Linux selenium version V2, instead set window size and window position like driver.set_window_position(0,0) and driver.set_window_size(1920,1080)
    driver.get("https://vtv.vn/du-bao-thoi-tiet.htm")
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'slideTd')))
    djjj = driver.find_element_by_xpath('//*[@id="slideTd"]')
    click = driver.find_element_by_xpath('//*[@id="form1"]/div[2]/div[5]/div/div[1]/div[2]/i[2]').click()
    djjj2 = driver.find_element_by_xpath('//*[@id="slideTd"]')

    # print(djjj.text)

    library2 = []
    library2.append(djjj.text + '\n' +  djjj2.text)
    temp_vtv =[]
    des_vtv = []

    library = library2[0].split('\n')

    count = 0
    for item in library:
        count += 1
        if count %2:
            des_vtv.append(item)
        else:
            temp_vtv.append(item)

    print(des_vtv)
    print('*************')


    # Chia list nhiet do ra thanh low va high
    for i in range(0, len(temp_vtv)):
        temp_vtv[i] = temp_vtv[i].replace('°', '')
        temp_vtv[i] = temp_vtv[i].split(' / ')
    print(temp_vtv)

    low_vtv = []
    high_vtv = []
    for _ in temp_vtv:
        low_vtv.append(_[0])
        high_vtv.append(_[1])
    print(low_vtv)
    print(high_vtv)

finally:
    driver.quit()