
import allure
from selene import browser, have



class Page_text_box_allure_steps:

    def open_browser(self):
        with allure.step('Открываем страницу с формой Text box'):
            browser.open('/')
            return self

    def fill_full_name(self, value):
        with allure.step('Ввод значения в input Full Name'):
            browser.element('#userName').type(value)
            return self

    def fill_email(self,value):
        with allure.step('Ввод значения в input Email'):
            browser.element('#userEmail').type(value)
            return self

    def fill_current_address(self,value):
        with allure.step('Ввод значения в input Current Address'):
            browser.element('#currentAddress').type(value)
            return self


    def fill_permanent_address(self,value):
        with allure.step('Ввод значения в input Permanent Address'):
            browser.element('#permanentAddress').type(value)
        return self

    def click_submit_button(self):
        with allure.step('Клик по кнопке Submit'):
            browser.element('#submit').click()
        return self


    def registered_user_info(self):
        with allure.step('Проверка информации о зарегистрированном пользователе'):
            browser.element('#output').all('p').should(have.exact_texts('Name:Иван',
                                                                    'Email:Iivanov23@gmail.com',
                                                                    'Current Address :Тестовый переулок дом 45',
                                                                    'Permananet Address :Тестовый проезд дом 100'))


class Page_text_box:
    pass