import unittest
import test_selenium_google_search
import test_selenium_login

"""
A test Suite, in your preferred framework saved as you see fit, that contains both task 1
and task 2 and lets us know via the output when each task begins and ends.
"""
suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(test_selenium_google_search.TestSeleniumGoogleSearch))
suite.addTest(unittest.makeSuite(test_selenium_login.TestSeleniumLogin))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
