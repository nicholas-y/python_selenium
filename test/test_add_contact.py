# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Tom", middlename="J", lastname="Tomson", nickname="Tm",
                               title="Boss", company="Comp", address="address line", homephone="800-900",
                               email="auto@test.com", birth_year="1970",
                               secondary_address="address line secondary",
                               secondary_homephone="801-901", notes="contact record")
    app.contact.create(contact)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contact_list)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
