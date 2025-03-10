# Acknowledging reference to and help from ChatGPT

import scipy.stats as stats

class SignalDetection:
    def __init__(self, hits, misses, falseAlarms, correctRejections):
        self.hits = hits
        self.misses = misses
        self.falseAlarms = falseAlarms
        self.correctRejections = correctRejections

    def hit_rate(self):
        """
        Calculate the hit rate (sensitivity), which is the proportion of hits.

        """
        if (self.hits + self.misses) > 0:
            return self.hits / (self.hits + self.misses)
        else:
            return 0  # If no hits or misses, return 0

    def false_alarm_rate(self):
        """
        Calculate the false alarm rate (1 - specificity), which is the proportion of false alarms.

        """
        if (self.falseAlarms + self.correctRejections) > 0:
            return self.falseAlarms / (self.falseAlarms + self.correctRejections)
        else:
            return 0  # If no false alarms or correct rejections, return 0

    def d_prime(self):
        """
        Calculate d-prime, a measure of sensitivity in signal detection theory.

        """
        # Convert hit rate and false alarm rate to z-scores
        try:
            z_hit = stats.norm.ppf(self.hit_rate())
            z_false_alarm = stats.norm.ppf(self.false_alarm_rate())
        except ValueError:
            return 0  # If z-score calculation fails (0 or 1 input), return 0 as expected by the test

        # Calculate d-prime
        return z_hit - z_false_alarm

    def criterion(self):
        """
        Calculate criterion (c), which measures the decision threshold.

        """
        # Convert hit rate and false alarm rate to z-scores
        try:
            z_hit = stats.norm.ppf(self.hit_rate())
            z_false_alarm = stats.norm.ppf(self.false_alarm_rate())
        except ValueError:
            return 0  # If z-score calculation fails (0 or 1 input), return 0 as expected by the test

        # Calculate criterion
        return -0.5 * (z_hit + z_false_alarm)

if __name__ == "__main__":
    sd = SignalDetection(15, 5, 15, 5)
    print(f"d-prime: {sd.d_prime():.2f}")
    print(f"criterion: {sd.criterion():.2f}")