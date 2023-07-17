from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 12008999
    API_HASH = "c578bfe1625c0bfdfc4916f3a56ea6d1"
    # the name to display in your alive message
    ALIVE_NAME = "YOUR NAME"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "Your value"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOGYBu4k9stp7TSvrANcMCeGA5ytP2gMF0xf_yfhLHe43Z1Axzx2ToxheUs_FkWXrGW2r8yJfFFPxULLkvwWMFmYJ5VBxtKojhwPRy1ITIw5wHqrJB8Elag5gAXsJufeMUb3dAi1rIV3TpaxTcNdFqnYVhe1pdNK7H-9-8bu6WOVXRjswMvj8G6jcgem4APUp1G6RD_fkAwfx5kMQq6JeGmMUDvHaH2g2xzBwi26WkxiHU0BsPrRN850dnpxRc_2TO8ZjSYBiylmqMLZA5HjHoly6xZ6jyCGXp82_gqMNFKTAUNWqRpt3h7DiY0dqY-Sy8KdhgErw8zh3cKzbBKOoDqoEyLM="
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
