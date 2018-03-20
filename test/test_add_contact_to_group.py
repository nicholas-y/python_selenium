from model.contact import Contact
import random


def test_add_contact_to_group(app, db_orm):
    if len(db_orm.get_contacts_without_group()) == 0:
        app.contact.create(Contact(firstname="Tester"))
    contacts_not_in_groups = db_orm.get_contacts_without_group()
    contact = random.choice(contacts_not_in_groups)
    group = random.choice(db_orm.get_group_list())
    app.contact.add_contact_to_group(contact.id, group.id)
    assert (contact in db_orm.get_contacts_in_group(group))

