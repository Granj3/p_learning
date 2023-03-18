# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from models.contact import Contact
import unittest


class AddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path=r'D:\x5prj\chromedriver.exe')
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_contact_and_fill(wd, Contact(firstname="Johnnie", midlename="Green", lastname="Walker", nickname="JWG", title="-", company="Destillary", address="Scotland", home_num="12345", mob_num="67890", work_num="11111", fax="22222", email="test@tst.com",
                                     email2="test2@tst.com", email3="test3@tst.com", homepage="www.leningrad.www.ru", bday="6", bmonth="March", byear="1990", aday="7", amonth="June", secondary_addres="Secondary_addres", ayear="1993",
                                     secondary_home="Secondary_home", secondary_notes="Secondary_notes"))
        self.retutn_to_homepage(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def retutn_to_homepage(self, wd):
        wd.find_element_by_link_text("home page").click()

    def create_contact_and_fill(self, wd, contact):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.midlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_num)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mob_num)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_num)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.secondary_addres)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondary_home)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.secondary_notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def home_page(self, wd):
        wd.get("http://localhost/addressbook/edit.php")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()