import random
from model.group import Group


def test_edit_group_name(app):
    i = random.randint(1, 25)
    if app.group.count() == 0:
        app.group.create(Group(name="Test Group"))
    app.group.edit_first(Group(name="groupA" + str(i)))

def test_edit_group_header(app):
    i = random.randint(1, 25)
    if app.group.count() == 0:
        app.group.create(Group(name="Test Group"))
    app.group.edit_first(Group(header="New header" + str(i)))