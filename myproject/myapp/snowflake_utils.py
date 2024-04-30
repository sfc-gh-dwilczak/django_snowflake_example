from sqlalchemy import create_engine
from django.conf import settings
from snowflake.sqlalchemy import URL

def get_snowflake_engine():
    url = URL(
        account=settings.SNOWFLAKE_ACCOUNT,
        user=settings.SNOWFLAKE_USER,
        password=settings.SNOWFLAKE_PASSWORD,
        database=settings.SNOWFLAKE_DATABASE,
        schema=settings.SNOWFLAKE_SCHEMA,
        warehouse=settings.SNOWFLAKE_WAREHOUSE,
        role=settings.SNOWFLAKE_ROLE,
    )
    engine = create_engine(url)
    return engine