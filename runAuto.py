from selenium import webdriver
path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://facebook.com/')

driver.execute_script("window.open('about:blank','secondtab') ")
driver.switch_to.window("secondtab")
driver.get('https://www.google.com/')


driver.execute_script("window.open('about:blank','thirdtap') ")
driver.switch_to.window("thirdtap")
driver.get('https://www.twitter.com/')

driver.execute_script("window.open('about:blank','forthtap') ")
driver.switch_to.window("forthtap")
driver.get('https://www.instgram.com/')

driver.execute_script("window.open('about:blank','fifthtap') ")
driver.switch_to.window("fifthtap")
driver.get('https://www.linkedin.com/')

driver.execute_script("window.open('about:blank','sexedtap') ")
driver.switch_to.window("sexedtap")
driver.get('https://www.youtupe.com/')

driver.execute_script("window.open('about:blank','seventap') ")
driver.switch_to.window("seventap")
driver.get('https://www.upwork.com/')

# print(driver.title)
# driver.quit()


# import pandas as pd
# df = pd.read_excel("numbers.xlsx")
# listOfNumbers = df['numbers']
# for x in listOfNumbers:
#   print(x)
#   print("yousef Is Khara")
