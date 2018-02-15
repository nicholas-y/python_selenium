import random
from model.group import Group


def test_edit_group_name(app):
    i = random.randint(1, 25)
    app.group.edit_first(Group(name="groupA" + str(i)))

def test_edit_group_header(app):
    i = random.randint(1, 25)
    app.group.edit_first(Group(header="New header" + str(i)))