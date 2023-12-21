from config import *
import pytest
# from conftest import *


#1 Форма "Авторизация"
def test_authorization_is_exists(auth):
    auth.go_to_site()
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_AUTH


# 2 Пункт меню "Почта" открывает форму авторизации по почте и паролю
def test_mail_is_clickable(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    assert auth.find_element(auth.LOCATOR_INPUT_MAIL)


# 3, 4
# Позитивная проверка авторизации по валидным телефону/почте и паролю.
# По умолчанию при открытии страницы открыта форма авторизации по телефону -- Вкладка "Телефон"
# При вводе почты вкладка "Телефон" переключается на вкладку "Почта"
@pytest.mark.fail_if_captcha
@pytest.mark.parametrize('username', [valid_phone, valid_email], ids=['valid phone', 'valid email'])
def test_auth_valid_data(auth, username):
    auth.go_to_site()
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)


# 5,6
# Негативные тесты авторизации по валидным телефону/почте и невалидному паролю.
@pytest.mark.fail_if_captcha
@pytest.mark.parametrize('username', [valid_phone, valid_email], ids=['valid phone', 'valid email'])
def test_auth_fake_password(auth, username):
    auth.go_to_site()
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, fake_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_ERROR_MSG).text == auth.ERROR_MSG_INVALID_DATA


# 7 Негативный тест авторизации по пустому полю ввода телефона и валидному паролю.
# 8 Негативный тест авторизации по пустому полю ввода телефона и пустому полю пароля.
@pytest.mark.parametrize('password', [valid_password, ''], ids=['valid password', 'invalid password (empty input)'])
def test_auth_empty_phone(auth, password):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_PHONE)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_PHONE_MSG


# 9 Негативный тест авторизации по пустому полю ввода почты и валидному паролю.
def test_auth_empty_mail(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_MAIL_MSG


# 10 Негативный тест авторизации по пустому полю ввода логина и валидному паролю.
def test_auth_empty_login(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LOGIN)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_LOGIN_MSG


# 11 Негативный тест авторизации по пустому полю ввода лицевого счета и валидному паролю.
def test_auth_empty_ls(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LS)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_LS_MSG


# 12 Ссылка "Забыл пароль" открывает форму "Восстановление пароля"
def test_forgot_password(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_FORGOT_PASSWORD)
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_RECOVERY


# 13 Ссылка "Зарегистрироваться" открывает форму "Регистрация"
def test_register(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_REGISTER)
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_REGISTRATION


# 14 Позитивная проверка авторизации по валидному телефону и паролю при вводе телефона во вкладку "Почта"

@pytest.mark.fail_if_captcha
def test_auth_valid_phone_tab_mail(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, valid_phone)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    active_tab_name = auth.find_element(auth.LOCATOR_ACTIVE_TAB).text
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)
    assert active_tab_name == 'Телефон'


# 15 Позитивная проверка авторизации по валидному телефону и паролю при вводе телефона во вкладку "Логин"
@pytest.mark.fail_if_captcha
def test_auth_valid_phone_tab_login(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LOGIN)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, valid_phone)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    active_tab_name = auth.find_element(auth.LOCATOR_ACTIVE_TAB).text
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)
    assert active_tab_name == 'Телефон'


# 16 Позитивная проверка авторизации по валидному телефону и паролю при вводе телефона во вкладку "Лицевой счет"
@pytest.mark.fail_if_captcha
def test_auth_valid_phone_tab_ls(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LS)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, valid_phone)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    active_tab_name = auth.find_element(auth.LOCATOR_ACTIVE_TAB).text
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert active_tab_name == 'Телефон'
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)


# 17 Позитивная проверка перехода на страницу авторизации через соц. сеть Вконтакте
def test_auth_social_network_vk(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_SOCIAL_NETWORK_VK)
    assert auth.find_element(auth.LOCATOR_IDENTIFIER_VK)


# 18 Позитивная проверка перехода на страницу авторизации через соц. сеть Однокласники
def test_auth_social_network_ok(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_SOCIAL_NETWORK_OK)
    assert auth.find_element(auth.LOCATOR_IDENTIFIER_OK)


# 19 Позитивная проверка перехода на страницу авторизации через почтовый клиент Mail.ru
def test_auth_social_mail(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_SOCIAL_MAIL)
    assert auth.find_element(auth.LOCATOR_IDENTIFIER_MAIL)


# 20 Позитивная проверка перехода на страницу авторизации через сервис клиент Yandex ID
def test_auth_social_yandex(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_SOCIAL_YANDEX)
    if auth.find_element(auth.LOCATOR_SOCIAL_YANDEX):
        auth.click_element(auth.LOCATOR_SOCIAL_YANDEX)
        assert auth.find_element(auth.LOCATOR_IDENTIFIER_YANDEX)
    else:
        assert auth.find_element(auth.LOCATOR_IDENTIFIER_YANDEX)


# 21 Позитивная проверка перехода на страницу пользовательского соглашения
def test_agreement_is_clickable(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_AGREEMENT)
    windows = auth.driver.window_handles
    auth.driver.switch_to.window(windows[-1])
    assert auth.find_element(auth.LOCATOR_AGREEMENT_ROOT)
