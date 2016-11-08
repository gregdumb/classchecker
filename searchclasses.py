from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://webadvisor.ohlone.edu/WebAdvisor/WebAdvisor?TYPE=M&PID=CORE-WBMAIN&TOKENIDX=792058356")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("acctToolbar")

#load the login page
login_text = driver.find_element_by_xpath("//*[contains(text(), 'Log In')]")
login_link = login_text.find_element_by_xpath("..")
login_link.click()

#enter username
username_box = driver.find_element_by_id("USER_NAME")
username_box.send_keys("NAME_REDACTED")

#enter password
password_box = driver.find_element_by_id("CURR_PWD")
password_box.send_keys("PW_REDACTED")

#click login
login_button = driver.find_element_by_name("SUBMIT2")
login_button.click();

#click students
student_button = driver.find_element_by_link_text("Students")
student_button.click();

#click "register and drop sections"
register_text = driver.find_element_by_xpath("//*[contains(text(), 'Register and Drop Sections')]")
register_link = register_text.find_element_by_xpath("..")
register_link.click()


while True:
    driver.refresh()
    driver.refresh()
    test = driver.find_element_by_id("LIST_VAR2_1")
    classsize = test.text
    num = int(classsize[0:classsize.find(" ")])
    if num > 0:
        print("The class is open!");
    else:
        print("Class is closed");
    time.sleep(5)



#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
#driver.close()
