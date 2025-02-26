# Acknowledging referance to and help from some website tools for fixing codes/ errors

# src/SignalDetection.py
class SignalDetection:
    def __init__(self, hits, misses, falseAlarms, correctRejections):
        """Initialize SignalDetection with raw counts."""
        self.hits = hits
        self.misses = misses
        self.falseAlarms = falseAlarms
        self.correctRejections = correctRejections

    def hit_rate(self):
        """Calculate the hit rate (sensitivity)."""
        if self.hits + self.misses > 0:
            return self.hits / (self.hits + self.misses)
        return 0  # If no hits or misses, return 0

    def false_alarm_rate(self):
        """Calculate the false alarm rate (1 - specificity)."""
        if self.falseAlarms + self.correctRejections > 0:
            return self.falseAlarms / (self.falseAlarms + self.correctRejections)
        return 0  # If no false alarms or correct rejections, return 0
