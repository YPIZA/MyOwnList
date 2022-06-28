class Config():
    SECRET_KEY = 'MRsK04L4trelarascas@outllook.es'

class DevelopmentConfig(Config):
    DEBUG = True
    HOST = 'ec2-18-204-142-254.compute-1.amazonaws.com',
    DATABASE = 'd7gehdosecboli',
    USER = 'puwucglwuisghg',
    PASSWORD = '4bed1f246b5d68178df83dc110d26b972d8c67842286130541e9084dde4a537f',
    PORT = 5432

config = {
    'development': DevelopmentConfig
}