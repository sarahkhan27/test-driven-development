import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.Experiment import Experiment

class TestExperiment(unittest.TestCase):
    def test_experiment_initialization(self):
        """Test that the Experiment constructor initializes an empty list."""
        exp = Experiment()
        self.assertTrue(hasattr(exp, 'conditions'))  # Check for 'conditions' instead of 'data'
        self.assertIsInstance(exp.conditions, list)  # Ensure conditions is a list
        self.assertEqual(exp.conditions, [])  # Ensure conditions is empty

if __name__ == "__main__":
    unittest.main()
