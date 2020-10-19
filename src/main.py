#!/usr/bin/env python

import sys
from src.vlan_allocator import generate_output_csv_file
import pandas as pd

requests_df = pd.read_csv("data/requests.csv")
vlans_df = pd.read_csv("data/vlans.csv")

sorted_vlans_df = vlans_df.sort_values(by=['vlan_id', 'device_id', 'primary_port'])

file_name = 'data/output.csv'

SUCCESS_EXIT_CODE = 0


def main():
    output_df = generate_output_csv_file(sorted_vlans_df, requests_df)
    output_df.to_csv(file_name, encoding='utf-8', index=False)

    return SUCCESS_EXIT_CODE


if __name__ == '__main__':
    sys.exit(main())
