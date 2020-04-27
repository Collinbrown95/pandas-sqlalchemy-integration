import pandas as pd

from schedule.config import DataConfig
from schedule.main.flat_to_hierarchical import flat_to_hierarchical

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
    df["last_name"] = df["last_name"].str.capitalize()
    df["first_name"] = df["first_name"].str.capitalize()
    df["job_title"] = df["job_title"].str.title()
    df["org_name"] = df["org_name"].str.lower().str.title()
    df["department_name"] = df["department_name"].str.title()
    return df    

def get_contacts_table():
    ''' Returns the contact info table of the database. '''
    df = load_as_dataframe()
    df = preprocess_columns(df)
    df = prepare_org_chart(df)

def prepare_org_chart(df, tree_depth=7):
    '''
    Creates hierarchical data of the organizational structure using the csv.
    Args:
        df: a pandas dataframe
        tree_depth: an int specifying how deep the org chart tree should go.
    Returns:
        org_chart: a python dict-like object containing the org chart.
    '''
    org_struc = df["org_structure"].drop_duplicates()
    org_struc = org_struc.str.split(":", n=-1, expand=True)
    columns = [i for i in range(0, min(tree_depth + 1, len(org_struc.columns)), 1)]
    org_struc = org_struc[columns]
    print("org struc df is\n", org_struc)
    org_struc = flat_to_hierarchical(org_struc)
    print("dataframe is\n", org_struc)

