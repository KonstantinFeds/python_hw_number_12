import allure
from selene import browser, have


class Page_text_box_allure_decorator:

    @allure.step('Открываем страницу с формой Text box')
    def open_browser(self):
        browser.open('/')
        return self

    @allure.step('Ввод значения в input Full Name')
    def fill_full_name(self,value):
        browser.element('#userName').type(value)
        return self

    @allure.step('Ввод значения в input Email')
    def fill_email(self,value):
        browser.element('#userEmail').type(value)
        return self

    @allure.step('Ввод значения в input Current Address')
    def fill_current_address(self,value):
        browser.element('#currentAddress').type(value)
        return self

    @allure.step('Ввод значения в input Permanent Address')
    def fill_permanent_address(self,value):
        browser.element('#permanentAddress').type(value)
        return self

    @allure.step('Клик по кнопке Submit')
    def click_submit_button(self):
        browser.element('#submit').click()
        return self

    @allure.step('Проверка информации о зарегистрированном пользователе')
    def registered_user_info(self):
        browser.element('#output').all('p').should(have.exact_texts('Name:Иван',
                                                                    'Email:Iivanov23@gmail.com',
                                                                    'Current Address :Тестовый переулок дом 45',
                                                                    'Permananet Address :Тестовый проезд дом 100'))





