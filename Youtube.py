from selenium import webdriver

user = input("Seach as u like : ")


driver= webdriver.Chrome('C:\\Users\\RAJAT\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.youtube.com')


searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys(user)

searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
searchButton.click()
