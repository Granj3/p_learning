from selenium import webdriver
from fixtures.session import SessionHelper
from fixtures.group import GroupHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome(executable_path=r'D:\x5prj\chromedriver.exe')
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()