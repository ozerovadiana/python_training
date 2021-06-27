# -*- coding: utf-8 -*-
from selenium import webdriver
import pytest
from application_contact import Application
from contact import *

@pytest.fixture

def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.open_home_page()
    app.log_in("admin", "secret")
    app.fill_name(contact_info_name(first_name="diana", middle_name="olegovna", last_name="ozerova"))
    app.fill_nickname("ozerovadiana")
    app.fill_title("qwerty")
    app.fill_company("google")
    app.fill_address("russia")
    app.fill_phones(contact_phones(mobile="9853811234", home_phone="123456", work_phone="1234567"))
    app.fill_emails(contact_emails(email="sss@ss.ru", email2="sssss@ssss.ru", email3="qwer@fr.ru"))
    app.fill_bday(contact_info_bday(bday_day="7", bday_month="May", bday_year="1996"))
    app.fill_secondary(contact_secondary(address2="russia,moscow", phone2="1", notes="wwww"))
    app.log_out()

