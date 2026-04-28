from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreditCardPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self):
        self.driver.get("https://www.mymoneymantra.com/")

    def fill_form(self):
        # Credit Card click
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Credit Card']"))).click()

        # Name
        self.wait.until(EC.element_to_be_clickable(
            (By.NAME, "fullName"))).send_keys("Abhilash Kumar")

        # Mobile
        self.driver.find_element(By.NAME, "mobile").send_keys("9999999999")

        # Email
        self.driver.find_element(By.NAME, "email").send_keys("test@gmail.com")

        # Employment
        emp = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//label[contains(text(),'Employment')]/following::input[1]")))
        emp.send_keys("Salaried")

        # Income
        income = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//label[contains(text(),'Income')]/following::input[1]")))
        income.send_keys("50000")

        # Pincode
        pin = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[contains(@placeholder,'Pincode')]")))
        pin.send_keys("110001")

        # Submit
        submit = self.wait.until(EC.element_to_be_clickable(
            (By.ID, "personal-details-button")))
        self.driver.execute_script("arguments[0].click();", submit)

    # 🔥 Fixed OTP automation
    def enter_fixed_otp(self, otp="1234"):
        otp_boxes = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//input[@maxlength='1']"))
        )

        for i, digit in enumerate(otp):
            otp_boxes[i].send_keys(digit)

    def click_verify(self):
        verify = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='VERIFY']")))
        self.driver.execute_script("arguments[0].click();", verify)

    def is_success(self):
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(.,'Thank')]")))
        return True