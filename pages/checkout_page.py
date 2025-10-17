from playwright.sync_api import expect

class CheckoutPage:
  def __init__(self, page):
    self.page = page
    self.checkout_btn = ".checkout_button"
    self.first_name = "#first-name"
    self.last_name = "#last-name"
    self.postal_code = "#postal-code"
    self.continue_btn = "#continue"
    self.finish_btn = "#finish"
    self.confirmation_msg = ".complete-header"

  def fill_details(self, first_name, last_name, postal_code):
    self.page.fill(self.first_name, first_name)
    self.page.fill(self.last_name, last_name)
    self.page.fill(self.postal_code, postal_code)
    self.page.click(self.continue_btn)
    # self.page.get_by_role('link', name=self.finish_btn).click()

  def complete_order(self):
    self.page.click(self.finish_btn)
    expect(self.page.locator(self.confirmation_msg)).to_have_text("Thank you for your order!")