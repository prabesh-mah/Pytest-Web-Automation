from webpages.EducationPage.TrainingPage import TrainingPage
import pytest
import time


@pytest.mark.regression
@pytest.mark.high_priority
class TestContactUs:

    def click_education_and_scroll_to_contact_us(self):
        contact_us = TrainingPage(self.driver)
        contact_us.hover_over_education_menu()
        contact_us.click_training()
        contact_us.check_contact_form_container()
        contact_us.scroll_using_js(900)

    @pytest.mark.order(26)
    @pytest.mark.timeout(30)
    @pytest.mark.high_priority
    def test_validate_form_fillup_with_empty_mandatory_details(self):
        self.click_education_and_scroll_to_contact_us()
        contact_us = TrainingPage(self.driver)
        contact_us.click_name()
        contact_us.click_phone_number()
        contact_us.click_email()
        contact_us.click_subject()
        contact_us.click_message()
        contact_us.scroll_using_js(100)
        contact_us.click_send_message_button()
        contact_us.error_message()
        # contact_us.visibility_of_success_box_for_invalid_case()

    @pytest.mark.order(27)
    @pytest.mark.timeout(50)
    @pytest.mark.high_priority
    def test_validate_form_fillup_with_invalid_email(self):
        self.click_education_and_scroll_to_contact_us()
        contact_us = TrainingPage(self.driver)
        contact_us.enter_name("Wicked Man")
        contact_us.enter_phone_number("")
        contact_us.enter_email("wicked@@fakeemail.com")
        contact_us.enter_subject("")
        contact_us.enter_message("This is demo message")
        contact_us.scroll_using_js(100)
        contact_us.click_send_message_button()
        contact_us.visibility_of_success_box_for_invalid_case()

    @pytest.mark.order(28)
    @pytest.mark.timeout(50)
    @pytest.mark.medium_priority
    def test_validate_form_fillup_by_clicking_send_button_multiple_times(self):
        self.click_education_and_scroll_to_contact_us()
        contact_us = TrainingPage(self.driver)
        for i in range(5):
            contact_us.click_send_message_button()
        contact_us.visibility_of_success_box_for_invalid_case()

    def fillup_form_and_submit_with_valid_details(self):
        self.click_education_and_scroll_to_contact_us()
        contact_us = TrainingPage(self.driver)
        contact_us.enter_name("Wicked Man")
        contact_us.enter_phone_number("9849984998")
        contact_us.enter_email("nepsealpha_test@mailto.plus")
        contact_us.enter_subject("demo mail")
        contact_us.enter_message("This is demo mail description")
        contact_us.scroll_using_js(100)
        contact_us.click_send_message_button()

    @pytest.mark.order(29)
    @pytest.mark.timeout(50)
    @pytest.mark.high_priority
    def test_validate_form_fillup_with_valid_details(self):
        self.fillup_form_and_submit_with_valid_details()
        contact_us = TrainingPage(self.driver)
        contact_us.visibility_of_success_box_for_valid_case()

    @pytest.mark.order(30)
    @pytest.mark.timeout(50)
    @pytest.mark.medium_priority
    def test_validate_reappeaing_of_success_dialog_box(self):
        self.fillup_form_and_submit_with_valid_details()
        contact_us = TrainingPage(self.driver)
        contact_us.click_ok_on_success_box()
        contact_us.click_premium_button()
        contact_us.hover_over_education_menu()
        contact_us.click_training()
        contact_us.visibility_of_success_box_for_invalid_case()
        contact_us.click_ok_on_success_box()
