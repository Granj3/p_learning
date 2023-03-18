# -*- coding: utf-8 -*-
from models.group import Group


def test_tst_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="tst_group_name", header="tst_logo", footer="tst_comment"))
    app.session.logout()
