from pages.credit_card_page import CreditCardPage   # 👈 ye add karo

def test_credit_card_flow(driver):
    page = CreditCardPage(driver)

    page.open()
    page.fill_form()

    page.wait_for_manual_otp()

    page.click_verify()
    page.click_continue()

    msg = page.verify_success()

    assert "Thank" in msg