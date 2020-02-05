from unittest

class SmokeTest(TestCase):
	def testsmoke(self):
		self.assertEquals(2+2,4)

if __name__ == '__main__':
	unittest.main