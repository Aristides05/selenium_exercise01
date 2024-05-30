from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

target_url = "https://www.saucedemo.com/v1/inventory.html"
error_target_url = "https://www.test.com"

driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.maximize_window()

driver.get("https://www.saucedemo.com/v1/")

username = driver.find_element(By.XPATH, "//input[@name='user-name']").send_keys("standard_user")
password = driver.find_element(By.XPATH, "//input[@name='password']").send_keys("secret_sauce")
btn_login = driver.find_element(By.XPATH, "//input[@type='submit']").click()
assert driver.current_url == target_url, f"Não foi possivel acessar a página, a url esperada é: {target_url} e a atual é: {driver.current_url}"                 #assert correct
#assert driver.current_url == error_target_url, f"Não foi possivel acessar a página, a url esperada é: {error_target_url} e a atual é: {driver.current_url}"    #error assert
