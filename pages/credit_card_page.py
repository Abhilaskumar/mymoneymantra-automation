from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class CreditCardPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def open(self):
        self.driver.get("https://www.mymoneymantra.com/")
        self.driver.maximize_window()

    def fill_form(self):
        wait = self.wait
        driver = self.driver

        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Credit Card']"))).click()
        wait.until(lambda d: "credit" in d.current_url.lower())

        wait.until(EC.element_to_be_clickable((By.NAME, "fullName"))).send_keys("Abhilash Kumar")
        wait.until(EC.element_to_be_clickable((By.NAME, "mobile"))).send_keys("9999999999")
        wait.until(EC.element_to_be_clickable((By.NAME, "email"))).send_keys("testing@gmail.com")

        cc = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(.,'Yes')]")))
        driver.execute_script("arguments[0].click();", cc)

        emp = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//label[contains(text(),'Employment Type')]/following::input[1]")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", emp)
        time.sleep(1)
        emp.send_keys("Salaried")
        emp.send_keys(Keys.ENTER)

        income = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//label[contains(text(),'Income')]/following::input[1]")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", income)
        time.sleep(1)
        driver.execute_script("arguments[0].focus();", income)
        income.clear()
        income.send_keys("50000")
        income.send_keys(Keys.TAB)

        pin = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[contains(@placeholder,'Pincode')]")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", pin)
        time.sleep(1)
        pin.clear()
        pin.send_keys("110001")
        pin.send_keys(Keys.ARROW_DOWN)
        pin.send_keys(Keys.ENTER)

        try:
            checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']")))
            driver.execute_script("arguments[0].click();", checkbox)
        except:
            print("⚠️ Checkbox not found")

        submit = wait.until(EC.element_to_be_clickable((By.ID, "personal-details-button")))
        driver.execute_script("arguments[0].click();", submit)

        print("✅ Form submitted")

    # OTP pause
    def wait_for_manual_otp(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@maxlength='1']")))
        print("👉 OTP screen aa gaya")
        input("👉 OTP browser me daalo, phir Enter dabao...")
        time.sleep(3)

    # VERIFY (auto + fallback)
    def click_verify(self):
        try:
            verify_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Verify') or contains(.,'VERIFY')]"))
            )
            self.driver.execute_script("arguments[0].click();", verify_btn)
            print("✅ OTP Verified (button clicked)")
        except:
            print("⚠️ Verify button not found, maybe auto verified")

    # CONTINUE (safe)
    def click_continue(self):
        try:
            continue_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'CONTINUE') or contains(.,'Continue')]"))
            )
            self.driver.execute_script("arguments[0].click();", continue_btn)
            print("✅ Continue clicked")
        except:
            print("⚠️ Continue button not found (maybe auto redirect)")

    # SUCCESS
    def verify_success(self):
        msg = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(.,'Thank')]"))
        )
        print("🎉 Success Message:", msg.text)
        self.driver.save_screenshot("reports/success.png")
        return msg.text