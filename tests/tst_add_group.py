# -*- coding: utf-8 -*-
import pytest
from models.group import Group
from fixtures.application_group import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_tst_add_group(app):
    app.session.login(username="admin", password="secret")
    app.fill_group_form(Group(name="tst_group_name", header="tst_logo", footer="tst_comment"))
    app.session.logout()
