#             █ █ ▀ █▄▀ ▄▀█ █▀█ ▀
#             █▀█ █ █ █ █▀█ █▀▄ █
#              © Copyright 2022
#           https://t.me/hikariatama
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html


# meta pic: https://static.hikari.gay/purr_icon.png
# meta banner: https://mods.hikariatama.ru/badges/purr.jpg
# requires: pydub python-ffmpeg
# meta developer: @hikarimods
# scope: ffmpeg
# scope: hikka_only
# scope: hikka_min 1.2.10

import random

import requests
from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class KeywordMod(loader.Module):
    """Жалуется на чат"""

    strings = {"name": "Report"}

    @loader.unrestricted
    async def purrcmd(self, message: Message):
        """Sends 'report' voice message"""
            
        args = str(message.text).split(' ')
        if len(args) < 2:
            times = 1
        else: 
            if args[1].isdigit():
                times=int(args[1])


        if len(args) < 3:

            comment = 'Delete chat!'
        else:
            comment = ' '.join(args[2:])
        for i in range(times):
            for reason in reasons:
            
                await self._client(
                    functions.account.ReportPeerRequest(
                        peer=message.peer_id,
                        reason=reason,
                        message=comment
                    )
                )
                try:
                    reason_text = str(reason).replace('InputReportReason','').replace('()','')
                    await message.edit(f'Жалоба {reason_text} отправлена!')
                except Exception as e:
                    print(e)

        await message.edit(f'<b>Жалобы ({int(times)}) успешно отправлены!</b>',parse_mode='html')
