from pages.login_page import LoginPage
from pages.inventory_page import InvertoryPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import expect

def test_e2e_checkout(page):
  login = LoginPage(page)
  inventory = InvertoryPage(page)
  checkout = CheckoutPage(page)

  # 1: Login flow
  login.load()
  login.login("standard_user", "secret_sauce")

  # 2: Add to cart flow
  inventory.add_first_product_to_cart()
  inventory.goBack()
  inventory.sort("hilo")
  inventory.add_first_product_to_cart()
  inventory.goBack()
  inventory.sort("za")
  inventory.add_first_product_to_cart()
  inventory.goBack()
  inventory.go_to_cart()

  # 3: Check if it comes on cart or not
  expect(page).to_have_url("https://www.saucedemo.com/v1/cart.html")

  # 4: Checkout flow
  checkout.checkout('John', 'Deo', '122001')

  # 5: Check if order placed or not
  assert page.is_visible("text=THANK YOU FOR YOUR ORDER")

  page.wait_for_timeout(3000)
