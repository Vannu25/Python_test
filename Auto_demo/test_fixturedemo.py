import pytest
from selenium import webdriver

# ----------------------------
# 🔧 Chrome Fixture
# ----------------------------
@pytest.fixture(scope='class')
def driver(request):
    print("\n[SETUP] Launching Chrome")
    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
    request.cls.driver = driver  # ✅ attach to test class
    yield driver
    print("\n[TEARDOWN] Closing Chrome")
    driver.quit()

# ----------------------------
# 🔧 Firefox Fixture
# ----------------------------
@pytest.fixture(scope='class')
def driver_ff(request):
    print("\n[SETUP] Launching Firefox")
    driver = webdriver.Firefox(executable_path='/snap/bin/geckodriver')
    request.cls.driver = driver
    yield
    print("\n[TEARDOWN] Closing Firefox")
    driver.quit()

# ----------------------------
# 🧪 Base Test Class for Chrome
# ----------------------------
@pytest.mark.usefixtures("driver")
class BaseChromeTest:
    pass

# ----------------------------
# 🧪 Base Test Class for Firefox
# ----------------------------
@pytest.mark.usefixtures("driver_ff")
class BaseFirefoxTest:
    pass

# ----------------------------
# ✅ Test Class using Chrome
# ----------------------------
class TestLinks(BaseFirefoxTest):

    def test_google(self):
        self.driver.get("https://www.google.com")
        assert "Google" in self.driver.title

    def test_facebook(self):
        self.driver.get("https://www.facebook.com")
        assert "Facebook" in self.driver.title

    def test_instagram(self):
        self.driver.get("https://www.instagram.com")
        assert "Instagram" in self.driver.title

# ----------------------------
# 🔁 To use Firefox instead of Chrome:
# class TestLinks(BaseFirefoxTest):
#     ...
