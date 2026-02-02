# test_priceramicdbsyncnode.py
"""
Tests for PriCeramicDBSyncNode module.
"""

import unittest
from priceramicdbsyncnode import PriCeramicDBSyncNode

class TestPriCeramicDBSyncNode(unittest.TestCase):
    """Test cases for PriCeramicDBSyncNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PriCeramicDBSyncNode()
        self.assertIsInstance(instance, PriCeramicDBSyncNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PriCeramicDBSyncNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
