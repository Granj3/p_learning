from selenium import webdriver
from fixtures.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome(executable_path=r'D:\x5prj\chromedriver.exe')
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def init_group_creation(self):
        wd = self.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()

    def fill_group_form(self, group):
        wd = self.wd
        self.init_group_creation()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        self.submit_group_creation()

    def submit_group_creation(self):
        wd = self.wd
        wd.find_element_by_name("submit").click()
        self.open_groups_page()
        self.select_group()

    def return_to_groups_page(self):
            wd = self.wd
            wd.find_element_by_link_text("group page").click()

    def select_group(self):
        wd = self.wd
        wd.find_element_by_name("selected[]").click()

    def destroy(self):
        self.wd.quit()