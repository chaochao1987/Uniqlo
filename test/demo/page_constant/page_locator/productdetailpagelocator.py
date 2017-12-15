class Product_Detail_Page_Locator(object):
    # SIZE = 'xpath=//ul[@id="listChipSize"]/li/div[@title="{}"]'
    PRODUCT_NAME = 'xpath=//h1[@id="goodsNmArea"]'
    SIZE_SELECTED = 'xpath=//ul[@id="listChipSize"]/li[div[@title="{}"]]'
    # COLOR = 'xpath=//ul[@id="listChipColor"]/li/div[@title="{}"]'
    COLOR_SELECTED = 'xpath=//ul[@id="listChipColor"]/li[div[@title="{}"]]'

    QUANTITY = 'id=selectNum'
    CART = 'id=intoCartOff'
    CART_LOGO = 'xpath=//li[a[@id="gnav_cart_trigger"]]'
    ADDED_MSG = '//div[@id="msgAddedCart"]'
