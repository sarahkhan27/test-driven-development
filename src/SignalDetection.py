# Acknowledging referance to and help from some website tools for fixing codes/ errors

import scipy.stats as stats

class SignalDetection:
    def __init__(self, hits, misses, falseAlarms, correctRejections):
        """
        Initialize SignalDetection with raw counts instead of rates.

        Parameters:
            hits (int): Number of hits (true positives).
            misses (int): Number of misses (false negatives).
            falseAlarms (int): Number of false alarms (false positives).
            correctRejections (int): Number of correct rejections (true negatives).
        """
        # Compute hit rate and false alarm rate based on raw counts
        self.hits = hits
        self.misses = misses
        self.falseAlarms = falseAlarms
        self.correctRejections = correctRejections

        def hit_rate(self):
            """Calculate the hit rate (sensitivity), which is the proportion of hits."""
        if (self.hits + self.misses) > 0:
            return self.hits / (self.hits + self.misses)
        else:
            return 0  # If no hits or misses, return 0

    def false_alarm_rate(self):
        """Calculate the false alarm rate, which is the proportion of false alarms."""
        if (self.falseAlarms + self.correctRejections) > 0:
            return self.falseAlarms / (self.falseAlarms + self.correctRejections)
        else:
            return 0  # If no false alarms or correct rejections, return 0

    def d_prime(self):
        """
        Calculate d-prime, a measure of sensitivity in signal detection theory.

        Returns:
            float: The d-prime value.
        """
        # Convert hit rate and false alarm rate to z-scores
        try:
            z_hit = stats.norm.ppf(self.hit_rate())
            z_false_alarm = stats.norm.ppf(self.false_alarm_rate())
        except ValueError:
            return 0  

        # Calculate d-prime
        return z_hit - z_false_alarm

    def criterion(self):
        """
        Calculate criterion (c), which measures the decision threshold.

        Returns:
            float: The criterion value.
        """
        # Convert hit rate and false alarm rate to z-scores
        try:
            z_hit = stats.norm.ppf(self.hit_rate)
            z_false_alarm = stats.norm.ppf(self.false_alarm_rate)
        except ValueError:
            return 0  

        # Calculate criterion
        return -0.5 * (z_hit + z_false_alarm)