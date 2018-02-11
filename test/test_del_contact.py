def test_delete_contact(app):
    app.session.do_login(username="admin", password="secret")
    app.contact.delete_first()
    app.session.do_logout()