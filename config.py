
class Config:
    #CONFIG BASE DATOS
    USER_DB = 'postgres'
    PASS_DB ='dipi1138'
    URL_DB = 'localhost'
    NAME_DB = 'electrus'
    FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

    SQLALCHEMY_DATABASE_URI = FULL_URL_DB
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False
