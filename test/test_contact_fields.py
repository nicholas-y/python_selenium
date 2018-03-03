from model.contact import Contact
import random
import re

def test_phone_on_home_page (app):
    contacts_list = app.contact.get_contact_list()
    index = random.randrange(len(contacts_list))
    contact_from_home_page = contacts_list[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails == merge_emails_like_on_home_page(contact_from_edit_page)


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
