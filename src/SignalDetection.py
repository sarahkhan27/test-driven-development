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
        self.hits = hits
        self.misses = misses
        self.falseAlarms = falseAlarms
        self.correctRejections = correctRejections

    def hit_rate(self):
        """
        Calculate the hit rate (sensitivity), which is the proportion of hits.

        Returns:
            float: The hit rate.
        """
        if (self.hits + self.misses) > 0:
            return self.hits / (self.hits + self.misses)
        else:
            return 0  # If no hits or misses, return 0