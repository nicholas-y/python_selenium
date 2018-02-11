class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # open create group page
        wd.find_element_by_name("new").click()
        # enter group info
        self.enter_group_info(group)
        # click submit button
        wd.find_element_by_name("submit").click()
        # open group list page
        wd.find_element_by_link_text("group page").click()

    def enter_group_info(self, group):
        wd = self.app.wd
        # enter group name
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        # enter group header
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        # enter group footer
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_group_page()
        # click on first group checkbox
        wd.find_element_by_name("selected[]").click()
        # click Delete Group button
        wd.find_element_by_name("delete").click()
        # open group list page
        wd.find_element_by_link_text("group page").click()

    def edit_first(self, group):
        wd = self.app.wd
        self.open_group_page()
        # click on first group checkbox
        wd.find_element_by_name("selected[]").click()
        # click Edit Group button
        wd.find_element_by_name("edit").click()
        # enter new info
        self.enter_group_info(group)
        # click Update button
        wd.find_element_by_name("update").click()
        # open group list page
        wd.find_element_by_link_text("group page").click()

