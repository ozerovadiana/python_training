# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import *

def test_add_contact(app):
    app.session.open_home_page()
    app.session.login("admin", "secret")
    app.contact.contact_full()
    app.session.logout()

