def test_delete_first__group(app):
    app.session.open_home_page()
    app.session.login("admin", "secret")
    app.group.delete_first_group()
    app.session.logout()
