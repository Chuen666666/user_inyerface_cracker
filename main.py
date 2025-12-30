import ctypes
import time
from datetime import datetime
from pathlib import Path

import keyboard
import pyautogui
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 強制切換到英文輸入法
def switch_to_english():
    HWND_BROADCAST = 0xFFFF
    WM_INPUTLANGCHANGEREQUEST = 0x0050
    LANG_ENGLISH = 0x0409 # 美國英文
    ctypes.windll.user32.PostMessageW(HWND_BROADCAST, WM_INPUTLANGCHANGEREQUEST, 0, LANG_ENGLISH)

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)
driver.get('https://userinyerface.com/game.html')

try:
    wait = WebDriverWait(driver, 10)
    time.sleep(0.3)

    # 輸入密碼
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Choose Password"]')))
    password_input.send_keys(Keys.CONTROL + 'a', Keys.DELETE)
    password_input.send_keys('Qwertyuio1')

    # 輸入 Email
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Your email"]')))
    email_input.send_keys(Keys.CONTROL + 'a', Keys.DELETE)
    email_input.send_keys('a')

    # 輸入 Domain
    domain_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Domain"]')))
    domain_input.send_keys(Keys.CONTROL + 'a', Keys.DELETE)
    domain_input.send_keys('a')

    # 選擇 .com
    dropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'dropdown__field')))
    dropdown.click()

    dropdown_menu = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'dropdown__list')))
    dropdown_menu.send_keys(Keys.END)

    com_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "dropdown__list")]//div[text()=".com"]')))
    driver.execute_script('arguments[0].click();', com_option)

    # 取消勾選 Checkbox
    checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(@class, "checkbox__check")]/ancestor::label')))
    checkbox.click()

    # 點擊 Next 按鈕
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "button--secondary") and text()="Next"]')))
    next_button.click()

    # 點擊 Upload 按鈕
    upload_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'avatar-and-interests__upload-button')))
    upload_button.click()
    time.sleep(0.5)

    # 強制切換輸入法為英文
    switch_to_english()
    time.sleep(0.5)

    # 生成圖片+自動輸入圖片路徑
    current_dir = Path(__file__).resolve().parent
    img_path = current_dir / 'temp.png'

    img = Image.new("RGB", (64, 64), (255, 255, 255))
    img.save(img_path)
    time.sleep(0.3)

    pyautogui.write(str(img_path))
    time.sleep(0.5)
    pyautogui.press('enter')

    # 從最後一個 Checkbox 開始點擊 然後點擊原本的 1~3
    checkboxes = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[contains(@class, "icon-check checkbox__check")]')))

    driver.execute_script('arguments[0].click();', checkboxes[-1])
    for i in range(3):
        driver.execute_script('arguments[0].click();', checkboxes[i])

    # 勾選 Checkbox 之後才點擊 Next
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "button--stroked") and text()="Next"]')))
    next_button.click()

    # 清空所有 <input placeholder="Placeholder..."> 並輸入 a
    placeholders = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//input[@placeholder="Placeholder..."]')))
    
    for field in placeholders:
        field.send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        field.send_keys('a')

    # 選擇 Mr
    title_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "dropdown__field") and text()="Choose a title"]')))
    title_dropdown.click()

    mr_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "dropdown__list")]//div[text()="Mr"]')))
    driver.execute_script('arguments[0].click();', mr_option)

    # 選擇 Afghanistan
    country_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "dropdown__field")]//span[contains(@class, "country-dropdown__selected-country-name") and text()="Choose a country"]')))
    country_dropdown.click()

    afghanistan_flag = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "flag flag-af country-dropdown__flag-item")]')))
    driver.execute_script('arguments[0].click();', afghanistan_flag)

    # 獲取今天的日期
    today = datetime.today()
    day = str(today.day)
    month = today.strftime('%B')
    year = str(today.year)

    # 選擇 Day
    day_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "dropdown__field") and text()="Day"]')))
    day_dropdown.click()

    day_option = wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[contains(@class, "dropdown__list")]//div[text()="{day}"]')))
    driver.execute_script('arguments[0].click();', day_option)

    # 選擇 Month
    month_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "dropdown__field") and text()="Month"]')))
    month_dropdown.click()

    month_option = wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[contains(@class, "dropdown__list")]//div[text()="{month}"]')))
    driver.execute_script('arguments[0].click();', month_option)

    # 選擇 Year
    year_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "dropdown__field") and text()="Year"]')))
    year_dropdown.click()

    year_option = wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[contains(@class, "dropdown__list")]//div[text()="{year}"]')))
    driver.execute_script('arguments[0].click();', year_option)

    # 點擊 Male
    male_toggle = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "toggle-button toggle-button--left selected")]')))
    male_toggle.click()

    # 按下 Next 按鈕
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "button button--stroked button--white") and text()="Next"]')))
    next_button.click()

    # 等待所有 Checkbox 顯示
    checkboxes = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[contains(@class, "checkbox__box")]')))

    # 勾選所有 Checkbox
    for checkbox in checkboxes:
        driver.execute_script("arguments[0].click();", checkbox)

    # 按下 Validate 按鈕
    validate_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "button button--solid button--blue") and text()="Validate"]')))
    validate_button.click()

    # 按下 Not really, no 按鈕
    not_really_no_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "button button--solid button--transparent") and text()="Not really, no"]')))
    not_really_no_button.click()

except Exception as e:
    print(f'Error: {e}')

finally:
    if img_path.exists():
        img_path.unlink()

time.sleep(0.5)
keyboard.wait('enter')
driver.quit()