from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Text
from sqlalchemy.orm import relationship

from schedule.config import SQLAlchemyConfig
from schedule.main.utils.db_utils import assemble_sqlalchemy_url


def create_employee_table(df):
    '''
    Creates the employees table in the database.
    '''
    engine = create_engine(assemble_sqlalchemy_url(SQLAlchemyConfig))
    df[["employee_id","last_name", "first_name", "job_title", "org_id", "dept_id"]].to_sql(
        "employees",
        engine,
        if_exists="replace",
        index=False,
        chunksize=1000,
        dtype={
            "id": Integer,
            "last_name": Text,
            "first_name": Text,
            "job_title": Text,
            "org_id": Integer,
            "dept_id": Integer,
        })

