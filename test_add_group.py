# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_group(app):
    app.do_login(username="admin", password="secret")
    app.create_new_group(Group(name="groupA", header="group header", footer="group footer"))
    app.do_logout()