from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
# options.headless = True
driver = webdriver.Chrome(options=options)

driver.get("http://localhost:1667/#/")


def test_cookies(a):  # 1: nem fogad el, 2: elfogad cookie-t
    try:
        kuki = driver.find_elements_by_xpath("/html/body/div/footer/div/div/div/div[2]/button[" + str(a) + "]/div")
        if len(kuki) > 0:
            kuki[0].click()
        return True
    except:
        return False


def test_nincs_cookigomb():
    kuki1 = driver.find_elements_by_xpath("/html/body/div/footer/div/div/div/div[2]/button[1]/div")
    kuki2 = driver.find_elements_by_xpath("/html/body/div/footer/div/div/div/div[2]/button[2]/div")
    return len(kuki1) + len(kuki2) == 0


def test_ide_oda_kattint():  # Vizsgálja a Home, a Sign in és a Sign up linkek működését.
    try:
        navlinkek = driver.find_elements_by_class_name("nav-link")
        navlinkek[2].click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        navlinkek[1].click()
        time.sleep(2)
        driver.back()
        return True
    except:
        return False

def test_1():
    assert test_cookies(2)  # Elfogadja a Cookie-kat.
def test_2():
    assert test_nincs_cookigomb()  # Ha elfogadtam, már nincs Cookie-gomb.
def test_3():
    assert test_ide_oda_kattint()

driver.close()
