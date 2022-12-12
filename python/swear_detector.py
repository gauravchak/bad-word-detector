"""Class to detect swear words even with some character substitutions"""
from typing import List, Dict


class SwearDetector:
    """Class to filter content with prohibited words"""

    def __init__(self, badwords: List[str], substitutions: Dict[str, str]) -> None:
        pass

    def is_unsafe(self, text: str) -> bool:
        """Returns true if the given text contains a bad word"""
        return False
