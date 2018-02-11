def test_delete_group(app):
    app.session.do_login(username="admin", password="secret")
    app.group.delete_first()
    app.session.do_logout()