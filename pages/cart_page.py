from playwright.sync_api import expect

class CartPage:
  def __init__(self, page):
      self.page = page
      self.checkout_btn = "#checkout"
      self.cart_item = ".cart_item"

  def proceed_to_checkout(self):
    expect(self.page).to_have_url("https://www.saucedemo.com/cart.html")
    self.page.click(self.checkout_btn)

  def validate_cart(self, expected_count):
    expect(self.page.locator(self.cart_item)).to_have_count(expected_count, timeout=5000)
    print(f"Cart contains {expected_count} products.")
  