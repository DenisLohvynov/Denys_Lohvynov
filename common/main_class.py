from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time
import json
import re


class AddRemoveUser:
    def __init__(
            self, binary_location: str | None, service_location: str | None):
        if binary_location is None and service_location is None:
            self.driver = webdriver.Firefox()
        if binary_location is None and service_location is not None:
            service = Service(service_location)
            self.driver = webdriver.Firefox(service=service)
        if binary_location is not None and service_location is None:
            options = Options()
            options.binary_location = binary_location
            self.driver = webdriver.Firefox(options=options)
        if binary_location is not None and service_location is not None:
            options = Options()
            options.binary_location = binary_location
            service = Service(service_location)
            self.driver = webdriver.Firefox(service=service, options=options)
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1024, 768)
        self.driver.implicitly_wait(10)
        with open("common/Paths.json", encoding='UTF-8') as f:
            self.paths = json.load(f)

    def login_page(self):
        def data_for_logging_in(driver, passL, passP):
            elemL = driver.find_element(By.XPATH, passL)
            elemP = driver.find_element(By.XPATH, passP)

            return (re.search(r'Username\s*:\s*(.+)', elemL.text).group(1),
                    re.search(r'Password\s*:\s*(.+)', elemP.text).group(1))

        self.driver.get(
            'https://opensource-demo.orangehrmlive.com' +
            '/web/index.php/auth/login')
        login, password = data_for_logging_in(
            self.driver, self.paths["Background"]["passL"],
            self.paths["Background"]["passP"])

        self.driver.find_element(
            By.XPATH, self.paths["Background"]["loginP"]).send_keys(login)
        self.driver.find_element(
            By.XPATH, self.paths["Background"]["passwordP"]).send_keys(
                password)
        self.driver.find_element(
            By.XPATH, self.paths["Background"]["buttonP"]).click()
        # time.sleep(100)

    def to_Admin(self):
        time.sleep(6)
        admin_path = self.paths["To_Admin"]["admin_path"]
        self.driver.find_element(By.XPATH, admin_path).click()
        time.sleep(6)
        users1_path = self.paths["To_Admin"]["users1_path"]

        self.driver.find_element(By.XPATH, users1_path).click()
        time.sleep(5)
        users2_path = self.paths["To_Admin"]["users2_path"]
        self.driver.find_element(By.XPATH, users2_path).click()
        time.sleep(3)

    def add_new_user(self, name: str):
        add_button_path = self.paths["add_new_user"]["add_button_path"]

        self.driver.find_element(By.XPATH, add_button_path).click()
        user_role_path = self.paths["add_new_user"]["user_role_path"]

        self.driver.find_element(By.XPATH, user_role_path).click()

        self.driver.find_element(
            By.XPATH, '//span[contains(text(),"ESS")]').click()

        employee_name_path = self.paths["add_new_user"]["employee_name_path"]

        self.driver.find_element(
            By.XPATH, employee_name_path).send_keys("Od")

        time.sleep(2)

        self.driver.find_element(
            By.XPATH, '//span[contains(text(),"Odis  Adalwin")]').click()

        status_path = self.paths["add_new_user"]["status_path"]

        self.driver.find_element(By.XPATH, status_path).click()

        self.driver.find_element(
            By.XPATH, '//span[contains(text(),"Enabled")]').click()

        username_path = self.paths["add_new_user"]["username_path"]

        self.driver.find_element(
            By.XPATH, username_path).send_keys(name)

        password1_path = self.paths["add_new_user"]["password1_path"]

        self.driver.find_element(
            By.XPATH, password1_path).send_keys("?Password1")

        password2_path = self.paths["add_new_user"]["password2_path"]

        self.driver.find_element(
            By.XPATH, password2_path).send_keys("?Password1")

        save_button_path = self.paths["add_new_user"]["save_button_path"]

        time.sleep(2)

        self.driver.find_element(By.XPATH, save_button_path).click()

        time.sleep(5)

    def check_wether_in_table(self, name: str) -> bool:
        self.driver.refresh()
        time.sleep(3)

        # xpath_check = f'//div[@class="oxd-table-row ' +\
        #     'oxd-table-row--with-border" and contains(., "{name}")]'

        # found = WebDriverWait(self.driver, 10).until(
        #     ec.presence_of_element_located((By.XPATH, xpath_check)))

        xpath_found_row = f'//div[@class="oxd-table-row oxd-table-row--with-border" and contains(., "{name}")]'

        try:
            found_row = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, xpath_found_row)))
            found_row.find_element(By.XPATH, f'//div[contains(., "{name}")]')
            found_row.find_element(By.XPATH, '//div[contains(., "ESS")]')
            found_row.find_element(
                By.XPATH, '//div[contains(., "Odis Adalwin")]')
            found_row.find_element(By.XPATH, '//div[contains(., "Enabled")]')
        except TimeoutException as e:
            return False
        return True

    def delete_raw(self, name: str):
        xpath_delete = f'//div[@class="oxd-table-row ' +\
            f'oxd-table-row--with-border" and contains(., "{name}")]' +\
            f'//i[@class="oxd-icon bi-trash"]'
        self.driver.find_element(By.XPATH, xpath_delete).click()
        time.sleep(1)
        self.driver.find_element(
            By.XPATH, '//button[contains(.,"Yes, Delete")]').click()
        time.sleep(1)

    def __del__(self):
        self.driver.close()
