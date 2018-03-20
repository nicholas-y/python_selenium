from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    contact_cache = None

    def open_create_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        # open create new contact page
        self.open_create_contact_page()
        # enter contact info
        self.fill_contact_form(contact)
        # click Enter button
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def choose_first_contact(self):
        self.choose_contact_by_index(0)

    def choose_contact_by_index(self, index):
        wd = self.app.wd
        # click on first contact checkbox
        wd.find_elements_by_name("selected[]")[index].click()

    def choose_contact_by_id(self, id):
        wd = self.app.wd
        # click on first contact checkbox
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def click_edit_button(self):
        self.click_edit_button_by_index(0)

    def click_edit_button_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector("#maintable img[title='Edit']")[index].click()

    def click_edit_button_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()

    def delete_first(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # open home page with contacts list
        self.app.open_home_page()
        # choose contact
        self.choose_contact_by_index(index)
        # click Delete button
        wd.find_element_by_css_selector("input[value=\"Delete\"]").click()
        # accept alert
        wd.switch_to_alert().accept()
        # open home page with contacts list
        self.app.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        # open home page with contacts list
        self.app.open_home_page()
        # choose contact
        self.choose_contact_by_id(id)
        # click Delete button
        wd.find_element_by_css_selector("input[value=\"Delete\"]").click()
        # accept alert
        wd.switch_to_alert().accept()
        # open home page with contacts list
        self.app.open_home_page()
        self.contact_cache = None

    def edit_first(self, contact):
        self.edit_contact_by_index(contact, 0)

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        # open home page with contacts list
        self.app.open_home_page()
        # choose contact
        self.click_edit_button_by_index(index)
        # enter contact info
        self.fill_contact_form(contact)
        # click Update button
        wd.find_element_by_name("update").click()
        # open contacts list page
        self.app.open_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, contact):
        wd = self.app.wd
        # open home page with contacts list
        self.app.open_home_page()
        # choose contact
        self.click_edit_button_by_id(contact.id)
        # enter contact info
        self.fill_contact_form(contact)
        # click Update button
        wd.find_element_by_name("update").click()
        # open contacts list page
        self.app.open_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.fill_contact_form_field("firstname", contact.firstname)
        self.fill_contact_form_field("middlename", contact.middlename)
        self.fill_contact_form_field("lastname", contact.lastname)
        self.fill_contact_form_field("nickname", contact.nickname)
        self.fill_contact_form_field("title", contact.title)
        self.fill_contact_form_field("company", contact.company)
        self.fill_contact_form_field("address", contact.address)
        self.fill_contact_form_field("home", contact.homephone)
        self.fill_contact_form_field("mobile", contact.mobilephone)
        self.fill_contact_form_field("work", contact.homephone)
        self.fill_contact_form_field("email", contact.email)
        # enter Birthday
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").click()

        self.fill_contact_form_field("byear", contact.birth_year)
        # enter secondary contact info
        self.fill_contact_form_field("address2", contact.secondary_address)
        self.fill_contact_form_field("phone2", contact.secondary_homephone)
        self.fill_contact_form_field("notes", contact.notes)

    def fill_contact_form_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            # enter contact info
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_css_selector("td")
                last_name = cells[1].text
                first_name = cells[2].text
                address = cells[3].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, id=id,
                                                  all_phones=all_phones, address=address, all_emails=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.click_edit_button_by_index(index)
        homephone = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("mobile").get_attribute("value")
        mobilephone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, address=address, email=email, email2=email2,
                       email3=email3, homephone=homephone, workphone=workphone, mobilephone=mobilephone,
                       secondary_homephone=secondaryphone)

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id(contact_id).click()
        wd.find_element_by_css_selector("select[name='to_group'] option[value='%s']" % group_id).click()
        wd.find_element_by_name("add").click()
        wd.find_element_by_css_selector("a[href='./?group=%s']" % group_id).click()

    def del_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("select[name='group'] option[value='%s']" % group_id).click()
        wd.find_element_by_id(contact_id).click()
        wd.find_element_by_name("remove").click()
        wd.find_element_by_css_selector("a[href='./?group=%s']" % group_id).click()



