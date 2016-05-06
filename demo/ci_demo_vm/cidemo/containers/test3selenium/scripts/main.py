from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time
import unittest

NODE_ADDRESS = 'http://' + os.environ['SELENIUMHUB_PORT_4444_TCP_ADDR'] + ":" + str(os.environ['SELENIUMHUB_PORT_4444_TCP_PORT']) + '/wd/hub'

class AdminWebpage(unittest.TestCase):
	def setUp(self):
		# NOTE
		# Setting a driver every test like this is not ideal for a bunch of
		# tests, this is for demonstrative purposes only.  A better solution
		# would probably be to reuse the browser for a suite of tests,
		# or create a new container with browser for each test.
		print("setting up driver")
		self.driver = webdriver.Remote(
			command_executor=NODE_ADDRESS,
			desired_capabilities=DesiredCapabilities.FIREFOX
		)
		print("Remote to " + NODE_ADDRESS + " acquired")

	def tearDown(self):
		print("tearing down driver")
		self.driver.close()

	def testFindZiggy(self):
		self.driver.get("https://www.google.ca")
		assert "Google" in self.driver.title