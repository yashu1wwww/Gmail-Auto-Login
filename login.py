from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&continue=https%3A%2F%2Fmail.google.com&service=mail&ec=GAlAFw&flowName=GlifWebSignIn&flowEntry=AddSession")

input=driver.find_element_by_xpath('//*[@id="identifierId"]')
input.send_keys('yakannaohoh@gmail.com')

input=driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
input.click()

input=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
input.send_keys('Baar123@#$%')

input=driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[3]')
input.click()

