# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class AddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path=r'D:\x5prj\chromedriver.exe')
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/edit.php")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Johnnie")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Green")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Walker")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("JWG")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("-")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("Destillary")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Scotland")
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("12345")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("67890")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("11111")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("22222")
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("test@tst.com")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("test2@tst.com")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("test3@tst.com")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("www.leningrad.www.ru")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("6")
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("March")
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1990")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("7")
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("June")
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("1993")
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("Secondary_addres")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("Secondary_home")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("Secondary_notes")
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_link_text("home page").click()
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element_by_link_text("Logout").click()

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