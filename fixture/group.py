from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    group_cache = None

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # open create group page
        wd.find_element_by_name("new").click()
        # enter group info
        self.fill_group_form(group)
        # click submit button
        wd.find_element_by_name("submit").click()
        # open group list page
        self.open_group_page()
        self.group_cache = None

    def fill_group_form(self, group):
        self.fill_group_form_field("group_name", group.name)
        self.fill_group_form_field("group_header", group.header)
        self.fill_group_form_field("group_footer", group.footer)

    def fill_group_form_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/groups.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def choose_first_group(self):
        self.choose_group_by_index(0)

    def choose_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def choose_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s'" % id).click()

    def click_edit_button(self):
        wd = self.app.wd
        wd.find_element_by_name("edit").click()

    def delete_first(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        # click on first group checkbox
        self.choose_group_by_index(index)
        # click Delete Group button
        wd.find_element_by_name("delete").click()
        # open group list page
        self.open_group_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()
        # click on first group checkbox
        self.choose_group_by_id(id)
        # click Delete Group button
        wd.find_element_by_name("delete").click()
        # open group list page
        self.open_group_page()
        self.group_cache = None

    def edit_first_group(self, group):
        self.edit_group_by_index(group, 0)

    def edit_group_by_index(self, group, index):
        wd = self.app.wd
        self.open_group_page()
        # click on first group checkbox
        self.choose_group_by_index(index)
        # click Edit Group button
        self.click_edit_button()
        # enter new info
        self.fill_group_form(group)
        # click Update button
        wd.find_element_by_name("update").click()
        # open group list page
        self.open_group_page()
        self.group_cache = None

    def edit_group_by_id(self, group):
        wd = self.app.wd
        self.open_group_page()
        # click on first group checkbox
        self.choose_group_by_id(group.id)
        # click Edit Group button
        self.click_edit_button()
        # enter new info
        self.fill_group_form(group)
        # click Update button
        wd.find_element_by_name("update").click()
        # open group list page
        self.open_group_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))

        return list(self.group_cache)


