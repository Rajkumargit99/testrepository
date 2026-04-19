import time
import pytest
# from Dummy_booking_page import DummyBookingPage
# from data_file import *
from ...page_objects.dummy_website.Dummy_booking_page import DummyBookingPage
from ...page_objects.dummy_website.dummy_booking_data import *

@pytest.mark.usefixtures("get_driver")
class TestDummyBooking:

    def test_dummy_booking_verify(self):
        self.dp = DummyBookingPage(self.driver)
        self.dp.launch_dummy_website(url=website_url)
        time.sleep(1)
        self.dp.enter_fname(f_name=first_name)
        self.dp.enter_lname(l_name=last_name)
        time.sleep(1)
        self.dp.enter_dob(user_dob)
        self.dp.select_num_travellers(traveller_details)
        time.sleep(1)
        self.dp.enter_from_city(from_city=from_city_name)
        self.dp.enter_destination_city(dest_city=dest_city_name)
        time.sleep(1)
        self.dp.enter_billing_name(bill_name=billing_name)
        self.dp.enter_billing_phone(bill_phone=billing_phone)
        time.sleep(2)


