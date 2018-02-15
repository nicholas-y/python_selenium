# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Tom", middlename="J", lastname="Tomson", nickname="Tm",
                               title="Boss", company="Comp", address="address line", homephone="800-900",
                               email="auto@test.com", birth_year="1970",
                               secondary_address="address line secondary",
                               secondary_homephone="801-901", notes="contact record"))
