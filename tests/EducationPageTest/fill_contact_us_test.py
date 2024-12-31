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
    @pytest.mark.timeout(50)
    @pytest.mark.medium_priority
    @pytest.mark.skip
    def test_validate_form_fillup_by_clicking_send_button_multiple_times(self):
        self.click_education_and_scroll_to_contact_us()
        contact_us = TrainingPage(self.driver)
        for i in range(5):
            contact_us.click_send_message_button()
        contact_us.invisibility_of_success_box()

    test_data = [
        ("27", "", "", "", "", "", "validate_form_fillup_with_empty_mandatory_details"),
        ("28", "Wicked Man", "1234567890", "test@@@1.com", "Demo",
         "This is demo message", "validate_form_fillup_with_invalid_email"),
        ("29", "Wicked Man", "1234567890", "", "Demo",
         "This is demo message", "validate_form_fillup_with_empty_email"),
        ("30", "Wicked Man", "1234567890", "nepsealpha_test@mailto.plus", "Demo",
         "This is demo message", "fillup_form_and_submit_with_valid_details")
    ]

    @pytest.mark.skip
    @pytest.mark.parametrize("order, name, contact, email, subject, message, test_case", test_data)
    def test_form_fillup(self, order, name, contact, email, subject, message, test_case):
        pytest.mark.order(order)
        self.click_education_and_scroll_to_contact_us()
        contact_us = TrainingPage(self.driver)
        contact_us.enter_name(name)
        contact_us.enter_phone_number(contact)
        contact_us.enter_email(email)
        contact_us.enter_subject(subject)
        contact_us.enter_message(message)
        contact_us.scroll_using_js(100)
        contact_us.click_send_message_button()

        # Validation
        if test_case == "validate_form_fillup_with_empty_mandatory_details":
            contact_us.invisibility_of_success_box()
        elif test_case == "validate_form_fillup_with_invalid_email":
            contact_us.invisibility_of_success_box()
        elif test_case == "validate_form_fillup_with_empty_email":
            contact_us.invisibility_of_success_box()
        elif test_case == "fillup_form_and_submit_with_valid_details":
            contact_us.visibility_of_success_box()
        else:
            assert False

    def fillup_form_and_submit_with_valid_details(self):
        self.click_education_and_scroll_to_contact_us()
        contact_us = TrainingPage(self.driver)
        contact_us.enter_name("Wicked Man")
        contact_us.enter_phone_number("1234567890")
        contact_us.enter_email("nepsealpha_test@mailto.plus")
        contact_us.enter_subject("Demo")
        contact_us.enter_message("This is demo message")
        contact_us.scroll_using_js(100)
        contact_us.click_send_message_button()

    @pytest.mark.order(31)
    @pytest.mark.timeout(50)
    @pytest.mark.medium_priority
    def test_validate_reappeaing_of_success_dialog_box(self):
        self.fillup_form_and_submit_with_valid_details()
        contact_us = TrainingPage(self.driver)
        contact_us.click_ok_on_success_box()
        contact_us.click_premium_button()
        contact_us.hover_over_education_menu()
        contact_us.click_training()
        contact_us.visibility_of_success_box()
        contact_us.click_ok_on_success_box()
