import random
from model.contact import Contact


def test_edit_group(app):
    i = random.randint(1, 25)
    app.contact.edit_first(Contact(firstname="Tom" + str(i), middlename="J", lastname="Tomson", nickname="Tm",
                               title="Boss", company="Comp", address="address line", homephone="800-900",
                               email="auto@test.com", birth_year="1970",
                               secondary_address="address line secondary",
                               secondary_homephone="801-901", notes="contact record"))