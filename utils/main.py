from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(driver, url, username, password):
    """Авторизация"""
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "user").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//span[text()='Войти']").click()
    driver.implicitly_wait(10)


def upload_file(driver, file_path):
    """Загрузка файла"""
    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(file_path)


def delete_file(driver):
    """Удаление файла"""
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//label[contains(@for,'select_all_files')]").click()
    driver.find_element(By.CLASS_NAME, 'actions-selected').click()
    driver.find_element(By.XPATH, "//a[@class='menuitem action delete permanent']").click()

        
def delete_file_astra(driver):
    """Удаление файла"""
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//label[contains(@for,'select_all_files')]").click()
    driver.find_element(By.CLASS_NAME, 'actions-selected').click()
    driver.find_element(By.XPATH, "//a[@class='menuitem action delete permanent']").click()
    driver.find_element(By.XPATH, "//button[@class='primary']").click()
    


    