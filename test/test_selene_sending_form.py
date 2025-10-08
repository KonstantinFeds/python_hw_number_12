import allure
from allure_commons.types import Severity
from selene import browser, have


def test_selene_sending_form(open_browser):

    allure.dynamic.tag("web-text-box-form")
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.feature('регистрация text-box')
    allure.dynamic.story('Заполнение,отправка и проверка результата регистрации пользователя')
    allure.dynamic.label("owner", "Konstantin")
    allure.dynamic.link("https://demoqa.com/text-box", name='Testing')

    browser.open('/')
    browser.element('#userName').type('Иван')
    browser.element('#userEmail').type('Iivanov23@gmail.com')
    browser.element('#currentAddress').type('Тестовый переулок дом 45')
    browser.element('#permanentAddress').type('Тестовый проезд дом 100')
    browser.element('#submit').click()
    browser.element('#output').all('p').should(have.exact_texts('Name:Иван',
                                                                'Email:Iivanov23@gmail.com',
                                                                'Current Address :Тестовый переулок дом 45',
                                                                'Permananet Address :Тестовый проезд дом 100'))


