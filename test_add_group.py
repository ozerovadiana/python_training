# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture

def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.open_home_page()
    app.login("admin", "secret")
    app.open_groups_page()
    app.init_group_creation()
    app.fill_group_form(Group(group_name="111", group_header="hdhdh", group_footer="dhdh"))
    app.submit_group_creation()
    app.return_to_group_page()
    app.logout()

def test_add_empty_group(app):
    app.open_home_page()
    app.login("admin", "secret")
    app.open_groups_page()
    app.init_group_creation()
    app.fill_group_form(Group(group_name="", group_header="", group_footer=""))
    app.submit_group_creation()
    app.return_to_group_page()
    app.logout()




