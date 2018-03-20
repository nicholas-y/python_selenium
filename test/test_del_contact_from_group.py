from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db_orm):
    if len(db_orm.get_group_list()) == 0:
        app.group.create(Group(name="Test Group"))
    if len(db_orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Tester"))
    if len(db_orm.get_groups_with_contacts()) == 0:
        contact = random.choice(db_orm.get_contact_list())
        group = random.choice(db_orm.get_group_list())
        app.contact.add_contact_to_group(contact.id, group.id)
    group_with_contacts = db_orm.get_groups_with_contacts()
    random_group = random.choice(group_with_contacts)
    random_contact = random.choice(db_orm.get_contacts_in_group(random_group))
    app.contact.del_contact_from_group(random_contact.id, random_group.id)
    assert (random_contact not in db_orm.get_contacts_in_group(random_group))

