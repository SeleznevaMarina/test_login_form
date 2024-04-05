import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


def test_invalid_email_registration(browser):
    page = browser.new_page()
    page.goto("https://koshelek.ru")
    page.get_by_text('Зарегистрироваться').click()
    # Ввод некорректного email
    page.get_by_label('Электронная почта').fill('invalid_email')
    page.get_by_label('Пароль').fill('123')
    expect(page.get_by_text("Формат e-mail: username@test.ru", exact=True)).to_be_visible()

    
def test_weak_password_registration(browser):
    page = browser.new_page()
    page.goto("https://koshelek.ru")
    page.get_by_text('Зарегистрироваться').click()
    # Ввод слабого пароля
    page.get_by_label('Пароль').fill('123')
    page.get_by_label('Электронная почта').fill('123')
    expect(page.get_by_text("Пароль должен содержать минимум 8 символов", exact=True)).to_be_visible()

    page.get_by_label('Пароль').blur()
    page.get_by_label('Пароль').fill('12345678')
    page.get_by_label('Электронная почта').fill('123')
    expect(page.get_by_text("Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры", exact=True)).to_be_visible()


def test_uncorrect_username_registration(browser):
    page = browser.new_page()
    page.goto("https://koshelek.ru")
    page.get_by_text('Зарегистрироваться').click()
    # Ввод короткого имени
    page.get_by_label('Имя пользователя').fill('Iam')
    page.get_by_label('Электронная почта').fill('1')
    expect(page.get_by_text("Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы", exact=True)).to_be_visible()
    # Ввод длинного имени
    page.get_by_label('Имя пользователя').blur()
    page.get_by_label('Имя пользователя').fill('12345678ыуапкепкепывпапукпцукпцки')
    expect(page.get_by_text("Превышен лимит символов: 32 максимум", exact=True)).to_be_visible()
    # Начинается не с буквы
    page.get_by_label('Имя пользователя').fill('45alisa')
    page.get_by_label('Электронная почта').fill('2')
    expect(page.get_by_text("Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы", exact=True)).to_be_visible()
    # Содержит невалидные символы
    page.get_by_label('Имя пользователя').fill('alisa_25;')
    page.get_by_label('Электронная почта').fill('3')
    expect(page.get_by_text("Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы", exact=True)).to_be_visible()
    # Содержит кириллицу
    page.get_by_label('Электронная почта').fill('3')
    expect(page.get_by_text("Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы", exact=True)).to_be_visible()


def test_missing_fields_registration(browser):
    page = browser.new_page()
    page.goto("https://koshelek.ru")
    page.get_by_text('Зарегистрироваться').click()
    # Оставление полей пустыми
    page.get_by_text('Далее').click()
    expect(page.get_by_text("Поле не заполнено", exact=True)).to_have_count(3)
    page.locator("//span[@class='v-icon notranslate v-icon--dense theme--light error--text']/input[@id='input-1720'[@aria-checked='false']]").is_visible()
    

def test_invalid_referal_code_registration(browser):
    page = browser.new_page()
    page.goto("https://koshelek.ru")
    page.get_by_text('Зарегистрироваться').click()
    # Неверный ввод реферального кода
    page.get_by_label('Реферальный код').fill('invalid_code')
    page.get_by_label('Электронная почта').fill('1')
    expect(page.get_by_text("Неверный формат ссылки", exact=True)).to_be_visible()