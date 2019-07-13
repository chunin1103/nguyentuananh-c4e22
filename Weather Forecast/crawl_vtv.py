from selenium import webdriver
chrome_path = r"C:\Users\tuan anh\selenium\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://vtv.vn/du-bao-thoi-tiet.htm")
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# print(driver.page_source.encode("utf-8"))

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'slideTd')))

# djjj = driver.find_element_by_xpath('//*[@id="slideTd"]')
# print(djjj.text)
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


driver.quit()