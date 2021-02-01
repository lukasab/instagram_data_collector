from selenium import webdriver

class Instagram:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
