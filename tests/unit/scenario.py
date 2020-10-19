import pandas as pd 
import os

SCRIPT_PATH = os.path.dirname(__file__)

MOCK_VLANS = [(0, 1, 5),
              (0, 1, 8),
              (0, 0, 2),
              (0, 1, 2),
              (0, 0, 3),
              (0, 0, 4),
              (0, 0, 6),
              (0, 0, 7),
              (0, 0, 8),
              (0, 0, 10),
              (1, 0, 4),
              (1, 0, 7),
              (1, 0, 5),
              (1, 1, 5),
              (1, 1, 6),
              (1, 1, 9),
              (1, 0, 1),
              (1, 1, 1),
              (2, 1, 1),
              (2, 1, 4),
              (2, 1, 10)]

MOCK_SORTED_VLANS = [(1, 0, 1),
                     (1, 1, 1),
                     (2, 1, 1),
                     (0, 0, 2),
                     (0, 1, 2),
                     (0, 0, 3),
                     (0, 0, 4),
                     (1, 0, 4),
                     (2, 1, 4),
                     (0, 1, 5),
                     (1, 0, 5),
                     (1, 1, 5),
                     (0, 0, 6),
                     (1, 1, 6),
                     (0, 0, 7),
                     (1, 0, 7),
                     (0, 0, 8),
                     (0, 1, 8),
                     (1, 1, 9),
                     (0, 0, 10),
                     (2, 1, 10)]

MOCK_USEFUL_VLANS = [(1, 0, 1),
                     (1, 1, 1),
                     (2, 1, 1),
                     (0, 0, 2),
                     (0, 1, 2),
                     (2, 1, 4),
                     (0, 1, 5),
                     (1, 0, 5),
                     (1, 1, 5),
                     (1, 1, 6),
                     (0, 0, 8),
                     (0, 1, 8),
                     (1, 1, 9),
                     (2, 1, 10)]

MOCK_NON_REDUNDANT_VLANS = [(1, 1, 1),
                            (2, 1, 1),
                            (0, 1, 2),
                            (0, 0, 3),
                            (0, 0, 4),
                            (1, 0, 4),
                            (2, 1, 4),
                            (0, 1, 5),
                            (1, 1, 5),
                            (0, 0, 6),
                            (1, 1, 6),
                            (0, 0, 7),
                            (1, 0, 7),
                            (0, 1, 8),
                            (1, 1, 9),
                            (0, 0, 10),
                            (2, 1, 10)]

MOCK_USEFUL_VLANS_NON_REDUNDANT = [(1, 1, 1),
                                   (2, 1, 1),
                                   (0, 1, 2),
                                   (2, 1, 4),
                                   (0, 1, 5),
                                   (1, 1, 5),
                                   (1, 1, 6),
                                   (0, 1, 8),
                                   (1, 1, 9),
                                   (2, 1, 10)]

MOCK_AVAILABLE_VLANS_OUT_REDUNDANT = [(2, 1, 1),
                                      (0, 0, 2),
                                      (0, 1, 2),
                                      (2, 1, 4),
                                      (0, 1, 5),
                                      (1, 0, 5),
                                      (1, 1, 5),
                                      (1, 1, 6),
                                      (0, 0, 8),
                                      (0, 1, 8),
                                      (1, 1, 9),
                                      (2, 1, 10)]


MOCK_REDUNDANT_VLAN_INDEXES = [0, 1, 3, 4, 10, 11, 16, 17]

MOCK_REDUNDANT_USEFUL_VLAN_INDEXES = [0, 1, 3, 4, 7, 8, 10, 11]

MOCK_VLANS_DF = pd.DataFrame(MOCK_VLANS, columns=('device_id', 'primary_port', 'vlan_id'))
MOCK_SORTED_VLANS_DF = pd.DataFrame(MOCK_SORTED_VLANS, columns=('device_id', 'primary_port', 'vlan_id'))

MOCK_USEFUL_VLANS_DF = pd.DataFrame(MOCK_USEFUL_VLANS, columns=('device_id', 'primary_port', 'vlan_id'))
MOCK_USEFUL_VLANS_NON_REDUNDANT_DF = pd.DataFrame(MOCK_USEFUL_VLANS_NON_REDUNDANT, columns=('device_id', 'primary_port', 'vlan_id'))

MOCK_EMPTY_VLANS_DF = pd.DataFrame([], columns=('device_id', 'primary_port', 'vlan_id'))
MOCK_NON_REDUNDANT_VLANS_DF = pd.DataFrame(MOCK_NON_REDUNDANT_VLANS, columns=('device_id', 'primary_port', 'vlan_id'))

MOCK_AVAILABLE_VLANS_OUT_REDUNDANT_DF = pd.DataFrame(MOCK_AVAILABLE_VLANS_OUT_REDUNDANT, columns=('device_id', 'primary_port', 'vlan_id'))
MOCK_NON_REDUNDANT_VLANS_OUT_NOT_CROSSING_DF = pd.DataFrame(MOCK_NON_REDUNDANT_VLANS[1:], columns=('device_id', 'primary_port', 'vlan_id'))
MOCK_REDUNDANT_VLANS_OUT_CROSSING_DF = pd.DataFrame(MOCK_AVAILABLE_VLANS_OUT_REDUNDANT[1:], columns=('device_id', 'primary_port', 'vlan_id'))
