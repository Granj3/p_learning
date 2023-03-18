# -*- coding: utf-8 -*-
from models.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact_and_fill(Contact(firstname="Johnnie", midlename="Green", lastname="Walker", nickname="JWG", title="-", company="Destillary", address="Scotland", home_num="12345", mob_num="67890", work_num="11111", fax="22222", email="test@tst.com",
                                     email2="test2@tst.com", email3="test3@tst.com", homepage="www.leningrad.www.ru", bday="6", bmonth="March", byear="1990", aday="7", amonth="June", secondary_addres="Secondary_addres", ayear="1993",
                                     secondary_home="Secondary_home", secondary_notes="Secondary_notes"))
    app.session.logout()
