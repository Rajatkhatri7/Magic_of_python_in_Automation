from selenium import webdriver

user = input("Seach as u like : ")


driver= webdriver.Chrome('C:\\Users\\RAJAT\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get('https://pdfdrive.com')


searchbox = driver.find_element_by_xpath('//*[@id="q"]')
searchbox.send_keys(user)

searchButton = driver.find_element_by_xpath('//*[@id="search-form"]/button')
searchButton.click()
