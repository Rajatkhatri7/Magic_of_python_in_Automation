from selenium import webdriver

user = input("Seach as u like : ")


driver= webdriver.Chrome('C:\\Users\\RAJAT\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.google.com')


searchbox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchbox.send_keys(user)

searchButton = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
searchButton.click()
