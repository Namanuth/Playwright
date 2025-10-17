from playwright.sync_api import expect
from utils.config_reader import load_config

class LoginPage:
  def __init__(self, page):
    self.page = page
    self.username = "#user-name"
    self.password = "#password"
    self.login_btn = "#login-button"
    self.error_msg = "[data-test='error']"

  def load(self):
    config = load_config()
    base_url = config["base_url"]
    self.page.goto(base_url)

  def login(self, username, password, retries=2, wait_between_retries=2):
      """
      Attempts login with retry mechanism.
      Returns True if login successful, False otherwise.
      """
      for attempt in range(retries):
          self.page.fill(self.username, username)
          self.page.fill(self.password, password)
          self.page.click(self.login_btn)

          try:
              expect(self.page).to_have_url(
                  "https://www.saucedemo.com/inventory.html", timeout=5000
              )
              print(f"Login successful on attempt {attempt + 1}.")
              return True
          except AssertionError:
              # Check if error message is visible
              try:
                  self.page.wait_for_selector(self.error_msg, timeout=2000)
                  error_text = self.page.text_content(self.error_msg)
                  print(f"Login failed: {error_text.strip()}")
                  return False 
              except TimeoutError:
                  print(f"Attempt {attempt + 1} failed — retrying...")
                  if attempt < retries:
                      time.sleep(wait_between_retries)
                      self.page.reload()
                  else:
                      print("Login failed after all retries.")
                      return False
