class InvertoryPage:
  def __init__(self, page):
    self.page = page
    self.inventory_item = ".inventory_item"
    self.add_to_cart_btn = "button.btn_inventory"
    self.cart_icon = "#shopping_cart_container"
    self.sort_dropdown = ".product_sort_container"

  def add_first_product_to_cart(self):
    self.page.locator(self.add_to_cart_btn).first.click()

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