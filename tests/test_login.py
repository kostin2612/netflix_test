import allure
import pytest
from allure import step
from pages.login_page import LoginPage


@pytest.mark.parametrize("username, password, valid", [
    ("valid_user", "valid_pass", True),
    ("invalid_user", "valid_pass", False),
    ("valid_user", "invalid_pass", False),
    ("invalid_user", "invalid_pass", False)
])
@allure.title("Проверка входа по валидным/невалидным логину и паролю")
def test_netflix_login(page, username, password, valid):
    login_page = LoginPage(page)

    with step("Открываем страницу логина"):
        login_page.open()

    with step("Вводим логин и пароль"):
        login_page.login(username, password)

    with step("Проверяем результат"):
        if valid:
            assert login_page.is_logged_in(), 'Не смогли зайти с валидными username и password'
        else:
            assert "You can use a sign-in code, reset your password or try again" in login_page.get_error_message(), \
                "Нет сообщения о невалидных username и password"
