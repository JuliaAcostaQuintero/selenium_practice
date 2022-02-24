import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PageObjects.page_index import PageIndex
from PageObjects.item_page import ItemPage
from PageObjects.checkout import Checkout
from PageObjects.dresses_page import DressesPage
from PageObjects.contact_form import ContactForm
from helpers.locators import CheckoutLocators, PageIndexLocators, PageDressesLocators, ContactFormLocators


class TestCases(unittest.TestCase):
    def setUp(self):
        option = Options()
        option.add_argument('--disable-gpu')
        option.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.get('http://automationpractice.com/index.php')
        self.indexPage = PageIndex(self.driver)
        self.ItemPage = ItemPage(self.driver)
        self.Checkout = Checkout(self.driver)
        self.DressesPage = DressesPage(self.driver)
        self.ContactForm = ContactForm(self.driver)

    def test_buy_items(self):
        self.driver.implicitly_wait(10)
        self.indexPage.search('blouse')
        self.result_text = self.driver.find_element(
            *PageIndexLocators.search_results).text
        self.assertTrue(
            '1 result has been found.' in self.result_text)
        self.indexPage.click_item()
        self.ItemPage.select_size('L')
        self.ItemPage.select_quantity(4)
        self.ItemPage.add_to_cart()
        self.Checkout.user_name('zaith.jexiel@icelogs.com')
        self.Checkout.password('12345')
        self.Checkout.terms_of_service()
        self.Checkout.pay_by_wire()
        self.confirmation = self.driver.find_element(
            *CheckoutLocators.confirm_message)
        self.assertTrue(
            'Your order on My Store is complete.' in self.confirmation.text)

    def test_dresses(self):
        self.driver.implicitly_wait(5)
        self.DressesPage.click_dresses_link()
        self.DressesPage.select_options()
        self.first_product = self.driver.find_element(
            *PageDressesLocators.first_product)
        self.assertTrue('Printed Chiffon Dress' in self.first_product.text)

    def test_customer_contact(self):
        self.driver.implicitly_wait(5)
        self.indexPage.click_contact_link()
        self.ContactForm.select_subject("Customer service")
        self.ContactForm.enter_email("zaith.jexiel@icelogs.com")
        self.ContactForm.attach_file(
            'C:/Users/julia.acosta/Desktop/práctica automation selenium/helpers/files/IN170967.pdf')
        self.ContactForm.enter_message(
            "message to send")
        self.ContactForm.click_send()
        self.assertTrue('Your message has been successfully sent to our team.' in self.driver.find_element(
            *ContactFormLocators.confirm_message).text)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
