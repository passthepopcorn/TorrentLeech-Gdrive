from tobrot.sample_config import Config

#read readme too before filling these stuffs

class Config(Config):
    TG_BOT_TOKEN= "1617094186:AAGNOR5LjJxhaIvhKNwE7o4SixmWwbkNCIM" #imp
    APP_ID = 3075557 #imp
    API_HASH = "ef2233c17efb4043324454e9fd98dd01" #imp
    AUTH_CHANNEL = [-1001343836143, 1672278713] #imp replace your_id with your id from telegram or delete
    INDEX_LINK = "https://drive.passthepopcorn.workers.dev/0:/"
    GLEECH_COMMAND = "gleech@passthepopcorn_bot"
    YTDL_COMMAND = 'ytdl@passthepopcorn_bot'
    TELEGRAM_LEECH_COMMAND_G = "tleech@passthepopcorn_bot"
    CLONE_COMMAND_G = "gclone"
    PYTDL_COMMAND_G = "pytdl"
    DESTINATION_FOLDER = "TorrentLeech-Gdrive"
    LEECH_COMMAND = "leech@passthepopcorn_bot"
    CANCEL_COMMAND_G = "cancel@passthepopcorn_bot"
    RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.-XX9fgU--","token_type":"Bearer","refresh_token":"1//0gLZEp8-VV2rZyourtCgYIARAAGBASNwF-","expiry":"2020-09-03T14:22:34.599776393Z"}\nteam_drive = """
    #put your config(replacing new lines with \n) in triple quote like above: """<your one liner config>"""
