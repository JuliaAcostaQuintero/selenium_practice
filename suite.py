from cgi import test
import unittest
import testcases

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(testcases))

runner = unittest.TextTestRunner()
result = runner.run(suite)
