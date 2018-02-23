import random
from model.contact import Contact


def test_edit_group(app):
    i = random.randint(1, 25)
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Tester"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Tester" + str(i))
    index = random.randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
