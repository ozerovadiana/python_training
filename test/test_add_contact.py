# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import *

@pytest.fixture

def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.open_home_page()
    app.session.login("admin", "secret")
    app.contact.fill_name(contact_info_name(first_name="diana", middle_name="olegovna", last_name="ozerova"))
    app.contact.fill_nickname("ozerovadiana")
    app.contact.fill_title("qwerty")
    app.contact.fill_company("google")
    app.contact.fill_address("russia")
    app.contact.fill_phones(contact_phones(mobile="9853811234", home_phone="123456", work_phone="1234567"))
    app.contact.fill_emails(contact_emails(email="sss@ss.ru", email2="sssss@ssss.ru", email3="qwer@fr.ru"))
    app.contact.fill_bday(contact_info_bday(bday_day="7", bday_month="May", bday_year="1996"))
    app.contact.fill_secondary(contact_secondary(address2="russia,moscow", phone2="1", notes="wwww"))
    app.session.logout()

