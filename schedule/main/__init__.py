from schedule.main.prepare_data import prepare_data
from schedule.main.employee.employee_table import create_employee_table

def main():
    '''
    The main function to be run in the scheduled job. Everything required in
    the workflow should be called from here.
    '''
    # Load dataframe, preprocess columns, and assign unique integers for each
    # entity that will have its own table.
    df = prepare_data()
    # Create the employees table
    create_employee_table(df)

if __name__ == "__main__":
    main()