# pandas-sqlalchemy-integration
> A repository to showcase how Python's pandas library can be used to interact with a SQL database via SQLAlchemy. The primary use case for this type of integration is when a "data science" workflow needs to integrate with a software development workflow. This repository in particular is organized around a scheduled job that involves fetching, preprocessing, and writing data to a SQL database.

## Folder Organization

### data
For illustrative purposes, a small csv with fake data is included to simulate what raw data on employees of an organization might look like.

### schedule

#### config

#### main
All code that will run as part of the scheduled job goes in here.

#### test

#### playground
