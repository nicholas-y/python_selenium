import random
from model.group import Group


def test_edit_group_name(app):
    i = random.randint(1, 25)
    app.session.do_login(username="admin", password="secret")
    app.group.edit_first(Group(name="groupA" + str(i)))
    app.session.do_logout()
