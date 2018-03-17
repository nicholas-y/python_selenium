# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, check_ui, json_contact):
    contact = json_contact
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contact_list = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)