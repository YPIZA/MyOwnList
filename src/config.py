class Config():
    SECRET_KEY = 'MRsK04L4trelarascas@outllook.es'

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}