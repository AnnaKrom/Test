import pytest
import os
import dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.main import login, upload_file, delete_file, delete_file_astra


dotenv.load_dotenv()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'doc.txt')


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_file_del_vanil(driver):
    vanilla_url = 'https://test-vanilla.promo.astradisk.ru/login'

    # Тестирование на ванильной версии
    login(driver, vanilla_url, USERNAME, PASSWORD)
    upload_file(driver, file_path)
    delete_file(driver)

    assert WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[@class='uploadmessage']"))
        ), 'Подтверждение! Файлы удалились на ванильной версии.'


def test_file_del_astra(driver):
    astra_url = "https://test-disk.promo.astradisk.ru/login"

    # Тестирование на Astra.Disk
    login(driver, astra_url, USERNAME, PASSWORD)
    upload_file(driver, file_path)
    delete_file_astra(driver)

    assert WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[@class='uploadmessage']"))
        ), 'Подтверждение! Файлы удалились на Astra.Disk версии.'