
#!/usr/bin/python
import unittest2, os

if __name__ == '__main__':
	import unittest2
	loader = unittest2.TestLoader()
	tests = unittest2.defaultTestLoader.discover(os.getcwd() + '/tests')
	testRunner = unittest2.runner.TextTestRunner()
	testRunner.run(tests)
