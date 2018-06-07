import unittest, os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UnhumanSiteTests(unittest.TestCase):
    # def setUp(self):
    #     # create a new Firefox session
    #     geckopath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'geckodriver')
    #     print(geckopath)

    #     self.driver = webdriver.Firefox(executable_path=geckopath)
    #     self.driver.implicitly_wait(30)
    #     self.driver.maximize_window()

    #     self.driver.get('https://unhuman.pl/')


    def test_a(self):
        self.assertTrue(True)

    def test_b(self):
        self.assertTrue(True)

    def test_c(self):
        self.assertTrue(True)

    def test_d(self):
        self.assertTrue(True)

    # def test_currency_changed(self):
    #     """
    #         Currency change should change basket's balance currency symbol
    #     """
    #     #change currency
    #     self.driver.get(self.driver.current_url + 'settings.php?curr=EUR')

    #     #wait until page reloads
    #     myElem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'menu_basket')))

    #     menu_basket = self.driver.find_element_by_id('menu_basket')
    #     balance = menu_basket.find_element_by_xpath('//a/strong')

    #     self.assertTrue('€' in balance.text)

    # def test_empty_search(self):
    #     """
    #         Should display error message that text is too short
    #     """
    #     search_btn = self.driver.find_element_by_xpath('//*[@id="menu_search"]/button')
    #     search_btn.click()

    #     #wait until page reloads
    #     myElem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'searching')))

    #     error_message_tag = self.driver.find_element_by_xpath('//*[@id="menu_messages_warning"]/div/p')

    #     self.assertEqual(error_message_tag.text, 'Podany tekst jest zbyt krótki. Spróbuj podać dłuższy tekst lub skorzystaj z wyszukiwarki.')


    # def  test_hoodie_128_visible_items(self):
    #     """
    #         Checks if there is exacly 128 items to display in hoodie section
    #     """
    #     # hover over men navigation element
    #     men_element = self.driver.find_element_by_xpath("//*[@id=\"menu_categories\"]/ul[2]/li[1]")
    #     ActionChains(self.driver).move_to_element(men_element).perform()

    #     # wait for menu to show up
    #     element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"menu_categories\"]")))

    #     #click hoodie
    #     element_to_click = self.driver.find_element_by_xpath("//*[@id=\"menu_categories\"]/ul[2]/li[1]/ul/li[2]/ul/li[1]")
    #     element.click()

    #     #wait until page loads
    #     myElem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'filter_form')))

    #     product_table = self.driver.find_element_by_xpath("//*[@id=\"search\"]")
    #     product_elements = product_table.find_elements_by_class_name("product_wrapper")

    #     self.assertEqual(len(product_elements), 128)

    # def test_contact_info(self):
    #     """
    #         Checks if contact informations are set corectly
    #     """
    #     phone_href = self.driver.find_element_by_xpath('//*[@id="top_contact"]/a[1]').get_attribute('href')
    #     mail_href = self.driver.find_element_by_xpath('//*[@id="top_contact"]/a[2]').get_attribute('href')

    #     self.assertEqual(phone_href, 'tel:616460023')
    #     self.assertEqual(mail_href, 'mailto:sklep@unhuman.pl')

    # def test_sale_menu_color(self):
    #     """
    #         Checks if sale color is red
    #     """
    #     sale_selector = self.driver.find_element_by_xpath('//*[@id="menu_categories"]/ul[2]/li[6]/a')
    #     self.assertEqual(sale_selector.value_of_css_property('color'), 'rgb(191, 80, 80)')

    # def test_basket_balance_and_phone(self):
    #     """
    #         Basket balance should be zero and phone should be hidden
    #     """
    #     menu_basket = self.driver.find_element_by_id('menu_basket')
    #     balance = menu_basket.find_element_by_xpath('//a/strong')
    #     phone = menu_basket.find_element_by_css_selector('span.hidden-phone')

    #     self.assertEqual(balance.text, '0,00 zł')
    #     self.assertIsNotNone(phone)

    @unittest.skip("Test skip")
    def test_skip(self):
        """
            Always skiped test
        """
        raise NotImplementedError

    # def tearDown(self):
    #     # close the browser window
    #     self.driver.quit()

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    #unittest.main(verbosity=2)
