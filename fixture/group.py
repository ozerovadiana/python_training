class GroupHelper:
    def __init__(self,app):
        self.app=app

    def open_groups_page(self):
        # open groups page
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def init_group_creation(self):
        # init group creation
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def fill_group_form(self, group):
        # fill group form
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
      wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.group_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.group_footer)

    def submit_group_creation(self):
        # submit group creation
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def return_to_group_page(self):
        # return to group page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()