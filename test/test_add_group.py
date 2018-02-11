# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.do_login(username="admin", password="secret")
    app.group.create(Group(name="groupA", header="group header", footer="group footer"))
    app.session.do_logout()
