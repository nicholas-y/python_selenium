import random
from model.group import Group


def test_edit_group_name(app, db,check_ui):
    i = random.randint(1, 25)
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test Group"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    old_groups.remove(group)
    group.name = "groupA" + str(i)
    old_groups.append(group)
    app.group.edit_group_by_id(group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_edit_group_header(app, db, check_ui):
    i = random.randint(1, 25)
    if app.group.count() == 0:
        app.group.create(Group(name="Test Group"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    old_groups.remove(group)
    group.header = "New header" + str(i)
    old_groups.append(group)
    app.group.edit_group_by_id(group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)