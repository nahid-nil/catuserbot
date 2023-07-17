from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 12008999
    API_HASH = "c578bfe1625c0bfdfc4916f3a56ea6d1"
    # the name to display in your alive message
    ALIVE_NAME = "YOUR NIL"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://cctihzpp:z8bwA134TQR9wuerQQQbFXSgbVGSNetx@tuffi.db.elephantsql.com/cctihzpp"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "BQC3PicALruSS6xa-_at8JhaVbNJWf0V7aNVzBfg4oJHvrDipig18TG5rPSaPBFNgPw2Cu0AWf8M0O7lUbp27ZjL2KHkNws6d8S4pbElKzjvkVMdbizegB9gfxNfQ-DzddvS04RZdmPtTM6viKpQp2RdK-FWbT4DqEVnH5HmKwRsC34-ubuo5S8r8cBtxcbonfbsiX3Fpntp-PZrcb_Gc6KaZmdaztLvibgFpxHKQ1ah1132tVQiQHHvigxqa1Sp9oq_RZ6-h8fyFP6Dn1KSHnPEXsRAsHXNOgJXQGaSzCJevHAIovWXfF6lFt5dqXgzTa7K6pO6Bto5WPGR8lBOXfDfYgKSGgAAAAE0rwUXAA"
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5795573598:AAHAVju9fArv-H09tjXO0Zgs3RnA3RIkZoA"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001959450466
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"
