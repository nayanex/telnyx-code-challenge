import pandas as pd
from src.validator import check_not_empty, validate_dataframe

output = []


def trim_sorted_vlans_df(sorted_vlans_df, redundant_vlan_indexes=None):
    validate_dataframe(sorted_vlans_df)
    
    if redundant_vlan_indexes is None:
        redundant_vlan_indexes = []

    useless_rows = sorted_vlans_df[(sorted_vlans_df.primary_port == 0) & (~sorted_vlans_df.index.
                                                                          isin(redundant_vlan_indexes))].index.tolist()
    sorted_vlans_df.drop(useless_rows, inplace=True)    


def drop_unavailable_redundant_vlans(rows_to_drop, sorted_vlans_df, redundant_vlan_indexes):
    if not rows_to_drop:
        return True

    validate_dataframe(sorted_vlans_df)
    check_not_empty(redundant_vlan_indexes)

    sorted_vlans_df.drop(rows_to_drop, inplace=True)
    del redundant_vlan_indexes[:2]

    return True


def drop_unavailable_non_redundant_vlans(rows_to_drop, sorted_vlans_df, redundant_vlan_indexes=None):
    if not rows_to_drop:
        return True
    
    validate_dataframe(sorted_vlans_df)

    if redundant_vlan_indexes is None:
        redundant_vlan_indexes = []
    
    crossing_redundant_vlans_index = redundant_vlan_indexes.index(rows_to_drop[-1]) if rows_to_drop[-1] in \
                                                                                       redundant_vlan_indexes else None

    if crossing_redundant_vlans_index is None:
        sorted_vlans_df.drop(rows_to_drop, inplace=True)
        return True

    drop_unavailable_crossing_non_redundant_vlans(rows_to_drop, sorted_vlans_df, redundant_vlan_indexes, crossing_redundant_vlans_index)
    
    return True

def drop_unavailable_crossing_non_redundant_vlans(rows_to_drop, sorted_vlans_df, redundant_vlan_indexes, crossing_redundant_vlans_index):
    if crossing_redundant_vlans_index % 2 == 0:
        rows_to_drop.append(redundant_vlan_indexes[crossing_redundant_vlans_index + 1])
        sorted_vlans_df.drop(rows_to_drop, inplace=True)
        del redundant_vlan_indexes[crossing_redundant_vlans_index:crossing_redundant_vlans_index + 2]
    else:
        rows_to_drop.append(redundant_vlan_indexes[crossing_redundant_vlans_index-1])
        sorted_vlans_df.drop(rows_to_drop, inplace=True)
        del redundant_vlan_indexes[crossing_redundant_vlans_index-1:crossing_redundant_vlans_index + 1]
    return True


def populate_output(lowest_vlans_indexes, request_id, sorted_vlans_df):
    for index in lowest_vlans_indexes:
        device_id = sorted_vlans_df.loc[index]['device_id']
        primary_port = sorted_vlans_df.loc[index]['primary_port']
        vlan_id = sorted_vlans_df.loc[index]['vlan_id']
        output.append((request_id, device_id, primary_port, vlan_id))

    
def get_lowest_available_vlan_with_redundancy(request_id, sorted_vlans_df, redundant_vlan_indexes):
    lowest_vlans_indexes = redundant_vlan_indexes[:2]
    populate_output(lowest_vlans_indexes, request_id, sorted_vlans_df)
    drop_unavailable_redundant_vlans(lowest_vlans_indexes, sorted_vlans_df, redundant_vlan_indexes)


def get_lowest_available_vlan_no_redundancy(request_id, sorted_vlans_df, redundant_vlan_indexes):
    lowest_vlans_indexes = sorted_vlans_df[(sorted_vlans_df.primary_port == 1)].head(1).index.tolist()
    populate_output(lowest_vlans_indexes, request_id, sorted_vlans_df)
    drop_unavailable_non_redundant_vlans(lowest_vlans_indexes, sorted_vlans_df, redundant_vlan_indexes)


def generate_output_csv_file(sorted_vlans_df, requests_df):
    redundant_vlans = sorted_vlans_df.groupby(['device_id','vlan_id'])['primary_port'].filter(lambda g: g.nunique() > 1).reset_index()
    redundant_vlan_indexes = redundant_vlans['index'].tolist()

    trim_sorted_vlans_df(sorted_vlans_df, redundant_vlan_indexes)

    for request_id, redundant in requests_df.itertuples(index=False):
        if redundant:
            get_lowest_available_vlan_with_redundancy(request_id, sorted_vlans_df, redundant_vlan_indexes)
        else:
            get_lowest_available_vlan_no_redundancy(request_id, sorted_vlans_df, redundant_vlan_indexes)

    output_df = pd.DataFrame(output, columns=('request_id', 'device_id', 'primary_port', 'vlan_id'))

    return output_df
