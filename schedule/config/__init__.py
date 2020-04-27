from configparser import ConfigParser

config = ConfigParser()
# Read in the default and local config files to populate our configuration
files_read = config.read(['./schedule/config/default.cfg', './schedule/config/local.cfg'])

class SQLAlchemyConfig:
    ''' Configuration to connect to SQLAlchemy. '''
    DB_HOST = config.get('database', 'host')
    DB_DIALECT = config.get('database', 'dialect')  # Used to construct a SQLAlchemy URL
    DB_PORT = int(config.get('database', 'port'))
    DB_NAME = config.get('database', 'name')
    DB_USER = config.get('database', 'user')
    DB_PASS = config.get('database', 'pass')

class DataConfig:
    ORIGINAL_DATA_PATH = config.get('data', 'original_data_path')