from selenium import webdriver
from time import sleep

class Instagram:
    def __init__(self, username: str, password: str):
        self.driver = webdriver.Chrome()
        self.driver.get('https://instagram.com/')
        self.username = username
        self.password = password

    def _fill_user_pass(self, username_input_path:str, passwoard_input_path:str, log_in_btn_path:str) -> None:
        username_input = self.driver.find_element_by_xpath(username_input_path)
        username_input.send_keys(self.username)
        passwoard_input = self.driver.find_element_by_xpath(passwoard_input_path)
        passwoard_input.send_keys(self.password)
        sleep(0.5)
        log_in_btn = self.driver.find_element_by_xpath(log_in_btn_path)
        log_in_btn.click()
        sleep(2.5)

    def _log_in_facebook(self, is_two_factor: bool = False) -> None:
        facebook_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[5]/button')
        facebook_btn.click()
        sleep(1.5)
        cookie_btn = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]')
        cookie_btn.click()
        sleep(0.5)
        facebook_username_input_path = '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input'
        facebook_passwoard_input_path = '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input'
        facebook_btn_path = '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button'
        self._fill_user_pass(facebook_username_input_path, facebook_passwoard_input_path, facebook_btn_path)
        if is_two_factor:
            two_factor_input = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/form/div/div[2]/div[3]/span/input')
            two_factor = input('Insert Two-Factor Authentication\n')
            two_factor_input.send_keys(two_factor)
            continue_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/form/div/div[3]/div[1]/button')
            continue_btn.click()
            sleep(1.5)
            rember_browser_input = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/form/div/div[2]/div[2]/div[2]/input')
            rember_browser_input.click()
            sleep(0.5)
            continue_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/form/div/div[3]/div[1]/button')
            continue_btn.click()
            sleep(3)   

    def _log_in_instagram(self) -> None:
        instagram_username_input_path = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input'
        instagram_passwoard_input_path = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input'
        instagram_btn_path = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button'
        self._fill_user_pass(instagram_username_input_path, instagram_passwoard_input_path, instagram_btn_path)   
        

    def log_in(self, is_facebook: bool = False, is_two_factor: bool = False) -> None:
        cookie_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
        cookie_btn.click()
        sleep(1.5)
        if is_facebook:
            self._log_in_facebook(is_two_factor)
        else:
            self._log_in_instagram()
        notification_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notification_btn.click()
