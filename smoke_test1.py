from selenium import webdriver
from selenium.webdriver.support.color import Color

#imports for selenium WebDriverWait

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select


driver=webdriver.Chrome(executable_path='Drivers/chromedriver.exe')
driver.get("https://techskillacademy.net/brainbucket/index.php?route=account/login")

driver.maximize_window()  #maximizing the browser window

logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

# Natalia 5/6/21
# when you are clicking on the "Continue" or "Login" buttons,
# use WebDriverWait with expected condition element_to_be_clickable instead of driver.find_element_by*

wait=WebDriverWait(driver, 10)
new_registrant_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Continue')]")))


#getting the background color of the button
backround_color = new_registrant_btn.value_of_css_property("background-color")
converted_background_color = Color.from_string(backround_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'
new_registrant_btn.click()

# Natalia 5/6/21
# after clicking on the “Continue” button Registration page should launch.
# Add an explicit wait here until the “Register Account” title will be visible.

register_account=wait.until(
    EC.visibility_of_element_located((By.XPATH, "//h1[contains(.,'Register Account')]")))

#Register Account
#Personal Details
firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.clear()
firstname_input.send_keys("Natalia")

# Natalia Staver 4/25/2021


# Last Name Input
lastname_field = driver.find_element_by_xpath("//fieldset/div[3]")
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class

lastname_input = driver.find_element_by_id("input-lastname")
lastname_input.clear()
lastname_input.send_keys("Staver")

# e-mail input
e_mail_field = driver.find_element_by_xpath("//fieldset/div[4]")
e_mail_field_class = e_mail_field.get_attribute("class")
assert "required" in e_mail_field_class

e_mail_input = driver.find_element_by_id("input-email")
e_mail_input.clear()
e_mail_input.send_keys("staver.natalia@yahoo.com")

# Telephone
telephone_field = driver.find_element_by_xpath("//fieldset/div[5]")
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class

telephone_input = driver.find_element_by_id("input-telephone")
telephone_input.clear()
telephone_input.send_keys("589-663-0000")

# Verifies background-color of Continue button

continue_botton = driver.find_element_by_xpath("//input[@class='btn btn-primary']")

backround_color = continue_botton.value_of_css_property("background-color")
converted_background_color = Color.from_string(backround_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'
continue_botton.click()

# select country

country_dropdown=driver.find_element_by_id("input-country")
country_dropdown_select = Select(country_dropdown)
country_dropdown_select.select_by_value("30")

#Natalia Staver 5/8
#Select your state from the Region/State dropdown

driver.implicitly_wait(10)

Region_State_dropdown = driver.find_element_by_id("input-zone")
Region_State_dropdown.click()


Region_State_dropdown_select=Select(Region_State_dropdown)
Region_State_dropdown_select.select_by_value("440")

# Check “I have read and agree to the Privacy Policy”

privacy_policy=driver.find_element_by_xpath("//input[@name='agree' and @value='1']")
privacy_policy.click()

#Select “No” in the subscription
subscribe_btn=driver.find_element_by_xpath("//input[@name='newsletter' and @value='0']")
if not subscribe_btn.is_selected():
    subscribe_btn.click()


#Verify that you are able to land on the Registration form after selecting the ‘Register’ option
account_btn = driver.find_element_by_xpath("//a[@title='My Account']")
account_btn.click()

register_option = driver.find_element_by_xpath("//*[@class='dropdown-menu dropdown-menu-right']/li[1]")
register_option.click()


#Select the ‘Login’ option and verify that you are able to land on the login page.
account_btn = driver.find_element_by_xpath("//a[@title='My Account']")
account_btn.click()

login_option = driver.find_element_by_xpath("//a[contains(text(),'Login')]")
login_option.click()


