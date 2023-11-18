import os,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException
from selenium.webdriver import ActionChains

URL = "https://tinder.com/ro"
EMAIL = os.environ["email"]
PASSWORD = os.environ["password"]

chrome_settings = webdriver.ChromeOptions()
chrome_settings.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_settings)
driver.get(URL)

time.sleep(2)

wait = WebDriverWait(driver=driver, timeout=30)
login_btn = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')))
login_btn.click()

loginWithFB_btn = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')))
loginWithFB_btn.click()

windows = driver.window_handles
driver.switch_to.window(windows[-1])

time.sleep(2)
declineFBCookies_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='_42ft _4jy0 _al66 _4jy3 _4jy1 selected _51sy']")))
declineFBCookies_btn.click()

emailInput = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]')))
emailInput.send_keys(EMAIL)

passwordInput = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pass"]')))
passwordInput.send_keys(PASSWORD)
passwordInput.send_keys(Keys.ENTER)

base_window = driver.window_handles[0]
driver.switch_to.window(base_window)

time.sleep(5)

locationPermission_btn = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')))
locationPermission_btn.click()

time.sleep(1)

notificationsPermission_btn = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/main/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')))
notificationsPermission_btn.click()

time.sleep(1)

cookies = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')))
cookies.click()

for swipes in range(100):
    time.sleep(1)

    try:
        like_btn = wait.until(EC.presence_of_element_located((By.XPATH, '#s-547617529 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > div > main > div > div > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Iso\(i\).W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-ds-border-gamepad-like-default\) > button')))
        actions = ActionChains(driver)
        actions.move_to_element(like_btn).click().perform()

    except ElementClickInterceptedException:
        try:
            match_popup = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".itsAMatch a")))
            match_popup.click()
        except:
            add_to_home_btn = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div/div[2]/button[2]/div[2]/div[2]")))
            add_to_home_btn.click()
    except NoSuchElementException:
        time.sleep(3)
        like_btn.click()