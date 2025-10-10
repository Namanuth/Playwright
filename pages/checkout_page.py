class CheckoutPage:
  def __init__(self, page):
    self.page = page
    self.checkout_btn = ".checkout_button"
    self.first_name = "#first-name"
    self.last_name = "#last-name"
    self.postal_code = "#postal-code"
    self.continue_btn = ".cart_button"
    self.finish_btn = "FINISH"

  def checkout(self, first_name, last_name, postal_code):
    self.page.locator(self.checkout_btn).click()
    self.page.fill(self.first_name, first_name)
    self.page.fill(self.last_name, last_name)
    self.page.fill(self.postal_code, postal_code)
    self.page.locator(self.continue_btn).click()
    self.page.get_by_role('link', name=self.finish_btn).click()