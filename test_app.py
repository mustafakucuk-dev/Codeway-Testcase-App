import unittest
from app import hello

class TestHelloApp(unittest.TestCase):

  def test_hello(self):
    self.assertIn(hello(), "I have been visited")

if __name__ == '__main__':
  unittest.main()