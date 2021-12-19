# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/AbiantXchuan/dUltroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AbiantXchuan/Ultroid/blob/main/LICENSE/>.

from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, eor, get_string, ultroid_cmd

REPOMSG = """
• **ABIANTxULTRO* •\n
• Repo - [Click Here](https://github.com/AbiantXchuan/Ultroid)
• Addons - [Click Here](https://github.com/AbiantXchuan/UltroidAddons)
• Support - @abiantInherexRSKA
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://github.com/AbiantXchuan/Ultroid"),
        Button.url("Addons", "https://github.com/AbiantXchuan/UltroidAddons"),
    ],
    [Button.url("Support Group", "t.me/abiantInherexRSKA")],
]

ULTSTRING = """🎇 **Thanks for Deploying Ultroid Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@ultroid_cmd(
    pattern="repo$",
    type=["official", "manager"],
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info("Error while repo command : " + str(er))
    await eor(e, REPOMSG)


@ultroid_cmd(pattern="ultroid$")
async def useUltroid(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://telegra.ph/file/54a917cc9dbb94733ea5f.jpg",
        buttons=button,
    )
    await eor(rs, f"**[Click Here]({msg.message_link})**")
