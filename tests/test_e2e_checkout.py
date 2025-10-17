import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import expect
from utils.data_reader import get_product_list
from utils.config_reader import load_config

@pytest.mark.parametrize("user_type", ["valid", "invalid"])

def test_e2e_checkout(page, user_type):
  config = load_config()
  login = LoginPage(page)

  # 1: Login flow
  login.load()
  creds = config["users"][user_type]
  result = login.login(creds["username"], creds["password"])

  if not result and user_type == 'valid':
      pytest.fail(f"Login should have succeeded for {creds['username']}, but failed even after retries.")
  elif result and user_type == 'invalid':
      pytest.fail(f"Login succeeded unexpectedly for {creds['username']}.")
  elif not result and user_type == 'invalid':
      print(f"Expected failure handled for {creds['username']}.")
      pytest.xfail(f"Expected failure: {creds['username']} cannot login")
      pytest.skip("Skipping further steps due to invalid credentials.")

  page.screenshot(path="screenshots/step1_login.png")

  if user_type == "valid":
    inventory = InventoryPage(page)
    expected_products = get_product_list()
    inventory.validate_products(expected_products)
    inventory.sort("hilo")
    inventory.add_products_to_cart(count = 2)
    inventory.sort("lohi")
    inventory.add_products_to_cart(count = 2)
    page.screenshot(path="screenshots/inventory_page.png")
    inventory.go_to_cart()

    page.screenshot(path="screenshots/cart_page.png")

    cart = CartPage(page)
    cart.validate_cart(4)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(page)
    # Checkout flow
    checkout.fill_details("John", "Doe", "122001")
    page.screenshot(path="screenshots/checkout_page.png")
    checkout.complete_order()
    page.screenshot(path="screenshots/completed_order.png")

  else:
    print("Expected failure handled.")

  page.wait_for_timeout(3000)
