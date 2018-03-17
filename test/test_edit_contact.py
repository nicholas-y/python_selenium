import random
from model.contact import Contact


def test_edit_group(app, db, check_ui):
    i = random.randint(1, 25)
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Tester"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    old_contacts.remove(contact)
    contact.firstname = "Tester" + str(i)
    old_contacts.append(contact)
    app.contact.edit_contact_by_id(contact)
    assert len(old_contacts) == app.contact.count()
    new_contact_list = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
