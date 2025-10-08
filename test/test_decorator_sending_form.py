import allure
from allure_commons.types import Severity

from test.page.page_decorator_allure import Page_text_box_allure_decorator


def test_decorator_sending_form(open_browser):

    page_text_box = Page_text_box_allure_decorator()

    allure.dynamic.tag("web-text-box-form")
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.feature('регистрация text-box')
    allure.dynamic.story('Заполнение,отправка и проверка результата регистрации пользователя')
    allure.dynamic.label("owner", "Konstantin")
    allure.dynamic.link("https://demoqa.com/text-box", name='Testing')

    (
        page_text_box.open_browser()
     .fill_full_name('Иван')
     .fill_email('Iivanov23@gmail.com')
     .fill_current_address('Тестовый переулок дом 45')
     .fill_permanent_address('Тестовый проезд дом 100')
     .click_submit_button()

    )

    page_text_box.registered_user_info()
