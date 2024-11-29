from dotenv import load_dotenv
load_dotenv()

class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    # DEV
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:.Ratch326985@127.0.0.1/mypokeapi"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    "ambiente": DevelopmentConfig,
}
