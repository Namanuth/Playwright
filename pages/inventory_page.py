class InventoryPage:
  def __init__(self, page):
    self.page = page
    self.inventory_items = ".inventory_item"
    self.add_to_cart_btn = "button.btn_inventory"
    self.cart_icon = "#shopping_cart_container"
    self.sort_dropdown = ".product_sort_container"
    self.go_back = ".inventory_details_back_button"
    self.inventory_item_name = ".inventory_item_name"

  def add_products_to_cart(self, count = 2):
    for i in range(count):
        self.page.locator(self.add_to_cart_btn).nth(i).click()

  def go_to_cart(self):
    self.page.click(self.cart_icon)

  def sort(self, paramerter):
    if paramerter == "hilo":
      self.page.locator(self.sort_dropdown).select_option('Price (high to low)')
    elif paramerter == "lohi":
      self.page.locator(self.sort_dropdown).select_option('Price (low to high)')
    elif paramerter == "za":
      self.page.locator(self.sort_dropdown).select_option('Name (Z to A)')
    elif paramerter == "az":
      self.page.locator(self.sort_dropdown).select_option('Name (A to Z)')

  def goBack(self):
    self.page.locator(self.go_back).click()

  def validate_products(self, expected_products):
    actual = [el.inner_text() for el in self.page.locator(self.inventory_item_name).all()]
    for product in expected_products:
        assert product in actual, f"{product} not found on page"