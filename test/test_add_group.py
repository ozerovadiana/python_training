# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture

def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.open_home_page()
    app.session.login("admin", "secret")
    app.group.open_groups_page()
    app.group.init_group_creation()
    app.group.fill_group_form(Group(group_name="111", group_header="hdhdh", group_footer="dhdh"))
    app.group.submit_group_creation()
    app.group.return_to_group_page()
    app.session.logout()

def test_add_empty_group(app):
    app.session.open_home_page()
    app.session.login("admin", "secret")
    app.group.open_groups_page()
    app.group.init_group_creation()
    app.group.fill_group_form(Group(group_name="", group_header="", group_footer=""))
    app.group.submit_group_creation()
    app.group.return_to_group_page()
    app.session.logout()




