# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group

class HMTestSaaGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path=r'D:\x5prj\chromedriver.exe')
        self.wd.implicitly_wait(30)

    def test_tst_add_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.fill_group_form(wd, Group(name="tst_group_name", header="tst_logo", footer="tst_comment"))
        self.logout(wd)

    # def test_tst_add_empty_group(self):
    #     wd = self.wd
    #     self.login(wd, username="admin", password="secret")
    #     self.init_group_creation(wd)
    #     self.fill_group_form(wd, Group(name="", header="", footer=""))
    #     self.submit_group_creation(wd)
    #     self.return_to_groups_page(wd)
    #     self.select_group(wd)
    #     self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def select_group(self, wd):
        wd.find_element_by_name("selected[]").click()

    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def submit_group_creation(self, wd):
        wd.find_element_by_name("submit").click()
        self.open_groups_page(wd)
        self.select_group(wd)

    def fill_group_form(self, wd, group):
        self.init_group_creation(wd)
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        self.submit_group_creation(wd)


    def init_group_creation(self, wd):
        self.open_groups_page(wd)
        wd.find_element_by_name("new").click()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()


    def login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
