import random
from model.group import Group

i = random.randint(1, 25)

def test_edit_group(app):
    app.session.do_login(username="admin", password="secret")
    app.group.edit_first(Group(name="groupA" + str(i), header="group header", footer="group footer"))
    app.session.do_logout()