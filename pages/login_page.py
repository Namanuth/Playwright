class LoginPage:
  def __init__(self, page):
    self.page = page
    self.username = "#user-name"
    self.password = "#password"
    self.login_btn = "#login-button"

  def load(self):
    self.page.goto("https://www.saucedemo.com/v1/index.html")

  def login(self, username, password):
    self.page.fill(self.username, username)
    self.page.fill(self.password, "secret_sauce")
    self.page.click(self.login_btn)

    self.page.wait_for_timeout(3000)
