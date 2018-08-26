from selenium import webdriver
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
        self.fail('Finish the test!')

        # User is invited to enter a to-do item

        # User types "buy peacock feathers" into a text box

        # Upon hitting enter, the page updates and now the page lists
        # '1: Buy peacock feathers" as an item in to-do list

        # A text box inviting to enter another item is present
        # user enters "Use peacock feathres to make a fly"

        # The page updates, and shows both items on the list

        # The site has generated a unique url with some text explaining
        # that this is where the list is stored

        # User visits url and sees the to-do list is still there

if __name__ == '__main__':
    unittest.main()
