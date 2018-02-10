# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(app):
    app.do_login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="Tom", middlename="J", lastname="Tomson", nickname="Tm" ,
                                        title="Boss", company="Comp", address="address line", homephone="800-900",
                                        email="auto@test.com", birth_year="1970",
                                        secondary_address="address line secondary",
                                        secondary_homephone="801-901", notes="contact record"))
    app.do_logout()