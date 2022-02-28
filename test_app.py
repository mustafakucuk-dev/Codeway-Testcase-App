import unittest
from app import hello

class TestHelloApp(unittest.TestCase):

  def test_hello(self):
    self.assertIn("I have been visited",hello())

if __name__ == '__main__':
  unittest.main()