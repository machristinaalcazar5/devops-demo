import unittest
import sys
import os

# Add app directory to path so we can import app modules if needed
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

class TestApp(unittest.TestCase):
    def test_basic_assertion(self):
        # A simple test to validate pipeline execution
        self.assertEqual(1 + 1, 2)

if __name__ == "__main__":
    unittest.main()