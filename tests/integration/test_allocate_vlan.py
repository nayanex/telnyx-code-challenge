import unittest
import pandas as pd
import numpy as np

from src.vlan_allocator import generate_output_csv_file

MOCK_REQUESTS_DF = pd.read_csv("data/test_requests.csv")
MOCK_VLANS_DF = pd.read_csv("data/test_vlans.csv")
MOCK_OUTPUT_DF = pd.read_csv("data/test_output.csv")

MOCK_SORTED_VLANS_DF = MOCK_VLANS_DF.sort_values(by=['vlan_id', 'device_id', 'primary_port'])


class VlanAllocatorTestCase(unittest.TestCase):
    def test_vlan_allocator_happy_path(self):
        expected_output = generate_output_csv_file(MOCK_SORTED_VLANS_DF, MOCK_REQUESTS_DF)
        self.assertTrue(np.array_equal(MOCK_OUTPUT_DF, expected_output))
