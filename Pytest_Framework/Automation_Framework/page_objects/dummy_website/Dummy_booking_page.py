# from selenium_base import SeleniumBase
from ...base.selenium_base import SeleniumBase
from .Dummy_booking_locators import *

class DummyBookingPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_dummy_website(self, url):
        self.driver.get(url)

    def enter_fname(self, f_name):
        self.enter_text(fs_name, f_name)

    def enter_lname(self, l_name):
        self.enter_text(ls_name, l_name)

    def enter_from_city(self, from_city):
        self.enter_text(from_city_field, from_city)

    def enter_destination_city(self, dest_city):
        self.enter_text(dest_city_field, dest_city)

    def enter_billing_name(self, bill_name):
        self.enter_text(billing_name_field, bill_name)

    def enter_billing_phone(self, bill_phone):
        self.enter_text(billing_phone_field, bill_phone)

    def enter_dob(self, dob):
        self.enter_text(dob_calender, dob)

    def select_male(self):
        self.click_element(male_ration_btn)

    def select_num_travellers(self, value):
        self.select_dropdown_value(travellers_dropdown, value)