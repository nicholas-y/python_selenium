import random
from model.contact import Contact


def test_edit_group(app):
    i = random.randint(1, 25)
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Tester"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Tester" + str(i))
    contact.id = old_contacts[0].id
    app.contact.edit_first(contact)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contact_list)
    old_contacts[0] = contact
    assert old_contacts == new_contact_list
