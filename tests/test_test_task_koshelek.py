import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

# k-btn-header-signup 


def test_invalid_email_registration(browser):
    page = browser.new_page()
    page.goto("https://koshelek.ru/authorization/signup")

    # Ввод некорректного email
    # page.fill("input[name=username]", "testuser")
    assert page.fill("input[name=email]", "invalid_email")
    expect(page.get_by_text("Формат e-mail: username@test.ru", exact=True)).to_be_visible()
    # page.fill("input[name=password]", "password123")
    # page.click("input[type=submit]")

#     # Проверка сообщения об ошибке
#     assert page.inner_text(".error-message") == "Invalid email address."

# def test_weak_password_registration(browser):
#     page = browser.new_page()
#     page.goto("http://example.com/register")

#     # Ввод слабого пароля
#     page.fill("input[name=username]", "testuser")
#     page.fill("input[name=email]", "testuser@example.com")
#     page.fill("input[name=password]", "123")
#     page.click("input[type=submit]")

#     # Проверка сообщения об ошибке
#     assert page.inner_text(".error-message") == "Password must be at least 6 characters long."

# def test_existing_username_registration(browser):
#     page = browser.new_page()
#     page.goto("http://example.com/register")

#     # Регистрация с существующим именем пользователя
#     page.fill("input[name=username]", "existinguser")
#     page.fill("input[name=email]", "newuser@example.com")
#     page.fill("input[name=password]", "password123")
#     page.click("input[type=submit]")

#     # Проверка сообщения об ошибке
#     assert page.inner_text(".error-message") == "Username already taken. Please choose another one."

# def test_missing_fields_registration(browser):
#     page = browser.new_page()
#     page.goto("http://example.com/register")

#     # Оставление полей пустыми
#     page.click("input[type=submit]")

#     # Проверка сообщений об ошибках для каждого поля
#     assert page.inner_text(".error-message.username-error") == "Username is required."
#     assert page.inner_text(".error-message.email-error") == "Email is required."
#     assert page.inner_text(".error-message.password-error") == "Password is required."
