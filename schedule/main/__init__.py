from schedule.main.prepare_data import (get_contacts_table)

def main():
    '''
    The main function to be run in the scheduled job. Everything required in
    the workflow should be called from here.
    '''
    get_contacts_table()

if __name__ == "__main__":
    main()