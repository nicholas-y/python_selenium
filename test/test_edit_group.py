import random
from model.group import Group


def test_edit_group_name(app):
    i = random.randint(1, 25)
    if app.group.count() == 0:
        app.group.create(Group(name="Test Group"))
    old_groups = app.group.get_group_list()
    group = Group(name="groupA" + str(i))
    index = random.randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_group_header(app):
    i = random.randint(1, 25)
    if app.group.count() == 0:
        app.group.create(Group(name="Test Group"))
    old_groups = app.group.get_group_list()
    group = Group(header="New header" + str(i))
    index = random.randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)