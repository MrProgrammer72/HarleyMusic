#
# Copyright (C) 2021-present by TeamHarley@Github, < https://github.com/TeamHarley >.
#
# This file is part of < https://github.com/TeamHarley/HarleyMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamHarley/HarleyMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

from pyrogram import filters

import config
from strings import get_command
from HarleyMusic import app
from HarleyMusic.misc import SUDOERS
from HarleyMusic.utils.database import add_off, add_on
from HarleyMusic.utils.decorators.language import language

# Commands
LOGGER_COMMAND = get_command("LOGGER_COMMAND")


@app.on_message(filters.command(LOGGER_COMMAND) & SUDOERS)
@language
async def logger(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await add_on(config.LOG)
        await message.reply_text(_["log_2"])
    elif state == "disable":
        await add_off(config.LOG)
        await message.reply_text(_["log_3"])
    else:
        await message.reply_text(usage)
