class Experiment:
    def __init__(self):
        """Initialize an empty experiment with a list to store SDT objects and labels."""
        self.conditions = []
        self.labels = []

from src.SignalDetection import SignalDetection

def add_condition(self, sdt_obj, label=None):
    """Adds a SignalDetection object and an optional label to the experiment."""
    if not isinstance(sdt_obj, SignalDetection):
        raise TypeError("sdt_obj must be an instance of SignalDetection")
    self.conditions.append(sdt_obj)
    self.labels.append(label)

def sorted_roc_points(self):
    """Returns sorted false alarm and hit rates for the ROC curve."""
    if not self.conditions:
        raise ValueError("No conditions added to the experiment.")
    false_alarm_rates = [cond.false_alarm_rate() for cond in self.conditions]
    hit_rates = [cond.hit_rate() for cond in self.conditions]
    sorted_pairs = sorted(zip(false_alarm_rates, hit_rates))
    return zip(*sorted_pairs)  # Unzips into two lists
