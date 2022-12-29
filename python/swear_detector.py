"""Class to detect swear words even with some character substitutions"""
from typing import List, Dict


class SwearDetector:
    """Class to filter content with prohibited words"""

    def __init__(self, badwords: List[str], substitutions: Dict[str, str]) -> None:
        pass

    def is_unsafe(self, text: str) -> bool:
        """Returns true if the given text contains a bad word"""
        return False

def __main__():
  badwords = ["study"]
  subs = dict()
  swear_detector = SwearDetector(badwords=badwords, substitutions=subs)
  inputs = ["hello", "world", "study"]
  for input in inputs:
    detected = swear_detector.is_unsafe(input)
    if detected:
      print(f'{input} is unsafe')