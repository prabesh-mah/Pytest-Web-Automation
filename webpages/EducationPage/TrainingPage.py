from webpages.BasePage import BasePage
from webpages.BaseLocators import NavigationMenuLocator
from selenium.webdriver.common.by import By
import time


class TrainingLocator(BasePage):
    education = (
        By.XPATH, "//ul[@class='sf-menu']/descendant::a[@title='Education']")
    training = (
        By.XPATH, "//ul[@class='sf-menu']/descendant::a[@title='Training']")
    contact_form_container = (By.XPATH, "//form[@id='contact_form']")
    name = (By.XPATH, "//input[contains(@placeholder,'Name')]")
    phone_number = (By.XPATH, "//input[contains(@placeholder,'Phone')]")
    email = (By.XPATH, "//input[contains(@placeholder,'Email')]")
    subject = (By.XPATH, "//input[contains(@placeholder,'Subject')]")
    message = (By.XPATH, "//textarea[contains(@placeholder,'Message')]")
    send_message_button = (By.XPATH, "//input[@name = 'submit']")
    success_box = (
        By.CSS_SELECTOR, "div[role='dialog'][aria-labelledby='swal2-title']")
    success_box_text = (
        By.XPATH, "//h2[text()='Thank You for your request, We will be In contact with you ASAP']")
    ok_button = (
        By.XPATH, "//button[@type='button' and contains(text(),'OK')]")


class TrainingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_premium_button(self):
        self.click(NavigationMenuLocator.premium_button)

    def hover_over_education_menu(self):
        self.move_to_element(TrainingLocator.education)

    def click_training(self):
        self.click(TrainingLocator.training)

    def check_contact_form_container(self):
        self.check_element(TrainingLocator.contact_form_container)

    def enter_name(self, name):
        self.type(TrainingLocator.name, name)

    def click_name(self):
        self.click(TrainingLocator.name)

    def enter_phone_number(self, contactNumber):
        self.type(TrainingLocator.phone_number, contactNumber)

    def click_phone_number(self):
        self.click(TrainingLocator.phone_number)

    def enter_email(self, emailAddress):
        self.type(TrainingLocator.email, emailAddress)

    def click_email(self):
        self.click(TrainingLocator.email)

    def enter_subject(self, subject):
        self.type(TrainingLocator.subject, subject)

    def click_subject(self):
        self.click(TrainingLocator.subject)

    def enter_message(self, message):
        self.type(TrainingLocator.message, message)

    def click_message(self):
        self.click(TrainingLocator.message)

    def click_send_message_button(self):
        self.click(TrainingLocator.send_message_button)

    def visibility_of_success_box(self):
        self.check_element(TrainingLocator.success_box)

        text = "Thank You for your request, We will be In contact with you ASAP"

        visible_text = self.is_text_visible(
            TrainingLocator.success_box_text, text)

        if self.is_text_visible(
                TrainingLocator.success_box_text, text):
            assert True
        else:
            assert False

    def invisibility_of_success_box(self):
        self.check_element(TrainingLocator.success_box)

        text = "Thank You for your request, We will be In contact with you ASAP"

        visible_text = self.is_text_visible(
            TrainingLocator.success_box_text, text)

        if self.is_text_visible(
                TrainingLocator.success_box_text, text):
            assert False
        else:
            assert True

    def click_ok_on_success_box(self):
        self.click(TrainingLocator.ok_button)
