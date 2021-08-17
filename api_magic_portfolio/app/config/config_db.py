# Database Configuration
SERVER = 'zemoga-test-db.crhpedy9xxto.us-east-1.rds.amazonaws.com'
USER_NAME = 'zemoga_test_db'
PASSWORD = 'Zem0ga.101'
DATABASE = 'zemoga_test_db'
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER_NAME}:{PASSWORD}@{SERVER}/{DATABASE}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

