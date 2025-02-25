from src.Experiment import Experiment
from src.SignalDetection import SignalDetection

exp = Experiment()
exp.add_condition(SignalDetection(10, 5, 20, 15), "Condition 1")
print(exp.conditions, exp.labels)
