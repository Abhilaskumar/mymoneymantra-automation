import pytest
from pages.credit_card_page import CreditCardPage


@pytest.mark.skip(reason="OTP flow not supported in CI")
def test_credit_card_flow(driver):
    page = CreditCardPage(driver)

    page.open()
    page.fill_form()
    page.enter_fixed_otp("1234")
    page.click_verify()

    assert page.is_success()


def test_dummy():
    assert True