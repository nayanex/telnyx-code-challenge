import os
import shutil
import unittest
import pandas as pd
import mock
import numpy as np
from pandas.util.testing import assert_frame_equal

from src.vlan_allocator import trim_sorted_vlans_df, drop_unavailable_redundant_vlans, drop_unavailable_non_redundant_vlans, populate_output,\
     get_lowest_available_vlan_with_redundancy, get_lowest_available_vlan_no_redundancy, generate_output_csv_file

from unit.scenario import MOCK_SORTED_VLANS_DF, MOCK_REDUNDANT_VLAN_INDEXES, MOCK_USEFUL_VLANS_DF, MOCK_USEFUL_VLANS_NON_REDUNDANT_DF, \
     MOCK_AVAILABLE_VLANS_OUT_REDUNDANT_DF, MOCK_EMPTY_VLANS_DF, MOCK_NON_REDUNDANT_VLANS_DF, MOCK_NON_REDUNDANT_VLANS_OUT_NOT_CROSSING_DF, \
     MOCK_REDUNDANT_VLANS_OUT_CROSSING_DF, MOCK_REDUNDANT_USEFUL_VLAN_INDEXES

class VlanAllocatorTrimSortedVlansDfTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_sorted_vlans_df = MOCK_SORTED_VLANS_DF
        self.mock_redundant_vlan_indexes = MOCK_REDUNDANT_VLAN_INDEXES
    
    def test_trim_sorted_vlans_df_should_raise_exception_when_vlans_not_provided(self):
        with self.assertRaises(Exception) as exception:
            trim_sorted_vlans_df([], self.mock_redundant_vlan_indexes)
        self.assertEqual("Empty list provided for: (vlan dataframe)", exception.exception.message)

    def test_trim_sorted_vlans_df_no_redundant_vlans(self):
        trim_sorted_vlans_df(self.mock_sorted_vlans_df, [])
        assert_frame_equal(MOCK_USEFUL_VLANS_NON_REDUNDANT_DF.reset_index(drop=True), self.mock_sorted_vlans_df.reset_index(drop=True))

    def test_trim_sorted_vlans_df_drop_useless_secondary_ports(self):
        trim_sorted_vlans_df(self.mock_sorted_vlans_df, self.mock_redundant_vlan_indexes)
        self.assertTrue(self.mock_sorted_vlans_df.shape[0] == 14)
        self.assertTrue(np.array_equal(MOCK_USEFUL_VLANS_DF, self.mock_sorted_vlans_df.values))
  
class VlanAllocatorDropUnavailableRedundantVlansTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_useful_vlans_df = MOCK_USEFUL_VLANS_DF
        self.mock_redundant_vlan_indexes = MOCK_REDUNDANT_VLAN_INDEXES
        self.rows_to_drop = [0, 1]
    
    def test_drop_unavailable_redundant_vlans_no_rows_to_drop(self):
        drop_unavailable_redundant_vlans([], self.mock_useful_vlans_df, self.mock_redundant_vlan_indexes)
        self.assertTrue(np.array_equal(MOCK_USEFUL_VLANS_DF, self.mock_useful_vlans_df.values))
        self.assertEqual(self.mock_redundant_vlan_indexes, MOCK_REDUNDANT_VLAN_INDEXES)
    
    def test_drop_unavailable_redundant_vlans_vlan_dataframe_not_provided(self):
        with self.assertRaises(Exception) as exception:
            drop_unavailable_redundant_vlans(self.rows_to_drop, MOCK_EMPTY_VLANS_DF, self.mock_redundant_vlan_indexes)
        self.assertEqual("There are no vlans available.", exception.exception.message)
    
    def test_drop_unavailable_redundant_vlans_no_redundant_vlan_indexes(self):
        with self.assertRaises(Exception) as exception:
            drop_unavailable_redundant_vlans(self.rows_to_drop, self.mock_useful_vlans_df, [])
        self.assertEqual("There are no redundant vlans available.", exception.exception.message)
    
    def test_drop_unavailable_redundant_vlans_proper_rows_to_drop_and_redundant_vlans_provided(self):
        drop_unavailable_redundant_vlans(self.rows_to_drop, self.mock_useful_vlans_df, self.mock_redundant_vlan_indexes)
        assert_frame_equal(MOCK_AVAILABLE_VLANS_OUT_REDUNDANT_DF.reset_index(drop=True), self.mock_useful_vlans_df.reset_index(drop=True))

class VlanAllocatorDropUnavailableNonRendundantVlansTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_useful_vlans_df = MOCK_USEFUL_VLANS_DF
        self.mock_non_redundant_vlans_df = MOCK_NON_REDUNDANT_VLANS_DF
        self.mock_redundant_vlan_indexes = MOCK_REDUNDANT_USEFUL_VLAN_INDEXES
        self.rows_to_drop = [0]
    
    def test_drop_unavailable_non_redundant_vlans_no_rows_to_drop(self):
        drop_unavailable_non_redundant_vlans([],self.mock_useful_vlans_df, self.mock_redundant_vlan_indexes)
        self.assertTrue(np.array_equal(MOCK_USEFUL_VLANS_DF, self.mock_useful_vlans_df))
        self.assertEqual(self.mock_redundant_vlan_indexes, MOCK_REDUNDANT_USEFUL_VLAN_INDEXES)
    
    def test_drop_unavailable_non_redundant_vlans_vlan_dataframe_not_provided(self):
        with self.assertRaises(Exception) as exception:
            drop_unavailable_non_redundant_vlans(self.rows_to_drop, MOCK_EMPTY_VLANS_DF, self.mock_redundant_vlan_indexes)
        self.assertEqual("There are no vlans available.", exception.exception.message)

    def test_drop_unavailable_non_redundant_vlans_no_redundant_vlan_indexes(self):
        drop_unavailable_non_redundant_vlans(self.rows_to_drop, self.mock_non_redundant_vlans_df, [])
        self.assertTrue(np.array_equal(MOCK_NON_REDUNDANT_VLANS_OUT_NOT_CROSSING_DF, self.mock_non_redundant_vlans_df.values))
    
    def test_drop_unavailable_non_redundant_vlans_proper_rows_to_drop_and_redundant_vlans_provided(self):
        drop_unavailable_non_redundant_vlans(self.rows_to_drop, self.mock_useful_vlans_df, self.mock_redundant_vlan_indexes)
        assert_frame_equal(MOCK_AVAILABLE_VLANS_OUT_REDUNDANT_DF.reset_index(drop=True), self.mock_useful_vlans_df.reset_index(drop=True))

class VlanAllocatorGenerateOutputCsvFileTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_sorted_vlans_df = MOCK_SORTED_VLANS_DF
        self.mock_redundant_vlan_indexes = MOCK_REDUNDANT_VLAN_INDEXES
    
    def test_generate_output_csv_redundant_request_when_no_secondary_ports_available(self):
       pass
    
    def test_generate_output_csv_primary_request_when_no_primary_ports_available(self):
       pass

    def test_generate_output_csv_primary_more_requests_than_available_vlans(self):
       pass
