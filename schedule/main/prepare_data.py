import pandas as pd

from schedule.config import DataConfig
from schedule.main.search import get_path_to_node

def prepare_data():
    ''' Returns the prepared dataframe. '''
    df = load_as_dataframe()
    df = preprocess_columns(df)
    return create_table_keys(df)

def load_as_dataframe():
    ''' Returns a pandas dataframe containing the employee data. '''
    return pd.read_csv(DataConfig.ORIGINAL_DATA_PATH)

def preprocess_columns(df):
    '''
    Applies preprocessing to certain columns; returns the modified
    dataframe.
    Args:
        df: a pandas dataframe
    Returns:
        df: a pandas dataframe
    '''
    # Any data formatting goes here
    df["last_name"] = df["last_name"].str.lower()
    df["first_name"] = df["first_name"].str.lower()
    df["job_title"] = df["job_title"].str.lower()
    df["org_name"] = df["org_name"].str.lower()
    df["department_name"] = df["department_name"].str.lower()
    return df

def create_table_keys(df):
    '''
    Creates unique integer keys for organizations and departments so tables can
    be linked later on.
    '''
    # Use the index as the individaul id
    df["employee_id"] = df.index
    # Create unique integers for organization names
    df = df.assign(org_id=(df["org_name"]).astype('category').cat.codes)
    # Create unique integers for departments
    df = df.assign(dept_id=(df["department_name"]).astype('category').cat.codes)
    return df

def get_contacts_table():
    ''' Returns the contact info table of the database. '''
    df = load_as_dataframe()
    df = preprocess_columns(df)
    org_df, org_chart = prepare_org_chart(df)
    # Trying to find a node in the org chart
    org_df = generate_org_paths(org_df, org_chart)
    # print("temp is ", temp)

def prepare_org_chart(df, tree_depth=7):
    '''
    Creates hierarchical data of the organizational structure using the csv.
    Args:
        df: a pandas dataframe
        tree_depth: an int specifying how deep the org chart tree should go.
    Returns:
        org_chart: a python dict-like object containing the org chart.
    '''
    org_table = df[["org_name"]].drop_duplicates()
    # org_table["org_name"] = org_table["org_name"].drop_duplicates()
    org_struc = df["org_structure"].drop_duplicates()
    org_struc = org_struc.str.split(":", n=-1, expand=True)
    columns = [i for i in range(0, min(tree_depth + 1, len(org_struc.columns)), 1)]
    org_struc = org_struc[columns]
    return org_table, get_org_chart(org_struc)

def generate_org_paths(df, org_chart):
    '''
    Appends a dataframe with the path used to arrive at the particular node in
    the org chart.
    '''
    df["org_chart_path"] = df["org_name"].str.lower().apply(lambda x: get_path_to_node(x, org_chart))
    return df