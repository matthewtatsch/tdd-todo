from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Go to homepage
        self.browser.get('http://localhost:8000')

        # Title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User is invited to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # User types "buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # Upon hitting enter, the page updates and now the page lists
        # '1: Buy peacock feathers" as an item in to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # A text box inviting to enter another item is present
        # user enters "Use peacock feathres to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates, and shows both items on the list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn(
            '2: Use peacock feathers to make a fly',
            [row.text for row in rows]
        )

        # The site has generated a unique url with some text explaining
        # that this is where the list is stored
        self.fail('Finish the test!')
        
        # User visits url and sees the to-do list is still there

if __name__ == '__main__':
    unittest.main()
