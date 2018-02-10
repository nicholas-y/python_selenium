# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_group(app):
    app.session.do_login(username="admin", password="secret")
    app.group.create(Group(name="groupA", header="group header", footer="group footer"))
    app.session.do_logout()
