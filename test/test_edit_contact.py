import random
from model.contact import Contact


def test_edit_group(app):
    i = random.randint(1, 25)
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Tester"))
    app.contact.edit_first(Contact(firstname="Tester" + str(i)))