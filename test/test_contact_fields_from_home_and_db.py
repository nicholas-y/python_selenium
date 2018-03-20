from model.contact import Contact
import random
import re

def test_contacts_from_home_page_and_db (app, db_orm):
    contacts_list = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db_orm.get_contact_list(), key=Contact.id_or_max)
    for contact in contacts_from_db:
        contact.all_phones = merge_phones_like_on_home_page(contact)
        contact.all_emails = merge_emails_like_on_home_page(contact)

    assert all((i.firstname == j.firstname and i.lastname == j.lastname and i.address == j.address and
                i.all_phones == j.all_phones and i.all_emails == j.all_emails)
               for i, j in (zip(contacts_list, contacts_from_db)))



def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.workphone, contact.mobilephone, contact.secondary_homephone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            [contact.email, contact.email2, contact.email3]))
