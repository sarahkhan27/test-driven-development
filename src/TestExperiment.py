import unittest
from src.Experiment import Experiment
from src.SignalDetection import SignalDetection

class TestExperiment(unittest.TestCase):
    def test_add_condition(self):
        exp = Experiment()
        sdt = SignalDetection(20, 10, 15, 5)
        exp.add_condition(sdt, label="Condition 1")
        self.assertEqual(len(exp.conditions), 1)
        self.assertEqual(exp.labels[0], "Condition 1")

def test_sorted_roc_points(self):
    exp = Experiment()
    exp.add_condition(SignalDetection(30, 10, 20, 10), label="A")
    exp.add_condition(SignalDetection(50, 5, 10, 35), label="B")
    fa_rates, h_rates = exp.sorted_roc_points()
    self.assertTrue(all(x <= y for x, y in zip(fa_rates, fa_rates[1:])))

def test_compute_auc(self):
    exp = Experiment()
    exp.add_condition(SignalDetection(40, 0, 0, 60), label="Perfect")
    self.assertAlmostEqual(exp.compute_auc(), 1.0, places=2)
