"""Tests for SwearDetector"""
from swear_detector import SwearDetector


def test_simple():
    """Simple detection works"""
    badwords = ["study"]
    subs = dict()
    swear_detector = SwearDetector(badwords=badwords, substitutions=subs)
    inputs = ["hello", "world", "study"]
    expected = [False, False, True]
    results = list(map(swear_detector.is_unsafe, inputs))
    assert results == expected
