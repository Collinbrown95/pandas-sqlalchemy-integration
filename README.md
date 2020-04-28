# pandas-sqlalchemy-integration
> A repository to showcase how Python's pandas library can be used to interact with a SQL database via SQLAlchemy. The primary use case for this type of integration is when a "data science" workflow needs to integrate with a software development workflow. This repository in particular is organized around a scheduled job that involves fetching, preprocessing, and writing data to a SQL database.

## Folder Organization

### data
For illustrative purposes, a small csv with fake data is included to simulate what raw data on employees of an organization might look like.

### schedule

#### config

#### main
All code that will run as part of the scheduled job goes in here.

There is a ```main``` function which, in this example, is run as a scheduled job using Python's ```apscheduler``` library.

```main``` should call all functions that are required to perform the workflow. Beyond this, there is no restriction on how modules should be structured inside of the main folder.

<img src='https://g.gravizo.com/svg?
 digraph G {
   main -> prepare_data [label="1"];
   prepare_data -> {load_as_dataframe; preprocess_columns; create_table_keys};
   prepare_data -> main [color="red" label="df"];
   main -> create_contacts_table [label="2"];
   main -> create_organizations_table [label="3"];
   main -> create_departments_table [label="4"];
 }
'/>

#### test

#### playground
