
import os
from datetime import datetime

def take_screenshot(driver, name="error"):
    os.makedirs("reports/screenshots", exist_ok=True)
    file = f"reports/screenshots/{name}_{datetime.now().strftime('%H%M%S')}.png"
    driver.save_screenshot(file)