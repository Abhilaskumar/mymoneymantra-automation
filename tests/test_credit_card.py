from pages.credit_card_page import CreditCardPage


def test_credit_card_flow(driver):
    page = CreditCardPage(driver)

    page.open()
    page.fill_form()

    # 🔥 Fixed OTP
    page.enter_fixed_otp("1234")

    page.click_verify()

    assert page.is_success()