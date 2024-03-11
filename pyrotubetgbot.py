import os, random, string
from pytube import YouTube
from pyrogram import Client, types, filters

series1 = list(string.ascii_lowercase)
series2 = list(string.ascii_uppercase)
series3 = list(string.digits)
series4 = list(string.punctuation)

genrated_token: str = os.getenv('BotToken')
api :str = os.getenv('ApiId')
bot = Client("pyrotube", bot_token=genrated_token,api_id=api)

@bot.on_message(filters.command(['Start']))
async def Welcome(bot, message: types.Message):
    user_name = message.from_user.first_name

    await bot.send_message(message.chat.id, text="I,M your Youtube downloader" f"{user_name}")

@bot.on_message(filters.command(['downlaod']))
@bot.on_message(filters.text)
async def YouTubeCommand(bot, message: types.Message):
    link = message.text
    if 'youtube.com' in link:
        try:
            youtube = YouTube(link)
            stream = youtube.streams.get_highest_resolution()
            stream.download()

            await bot.send_video(message.chat.id, video=open(stream.default_filename, 'rb'), text="Here's the video you requested!")
            os.remove(stream.default_filename)

        except Exception as Error:
            await bot.send_message(message.chat.id, text=f"An error occurred: {str(Error)}")
    else:
        await bot.send_message(message.chat.id, text="Please send a valid YouTube video URL.")


@bot.on_message(filters.command('password'))
@bot.on_message(filters.text)
async def password_generate_start(bot, message):
    await bot.send_message(message.chat.id, text="Password length should start from 6. Please enter the length:")


async def password_generate(bot, message):
    password_length: int = message.text

    if not password_length.isdigit():
        await bot.send_message(message.chat.id, text="Please enter a valid number for the password length.")

    elif password_length < 6:
        await bot.send_message(message.chat.id, text="The length of the password should be at least 6. Please try again.")

    random.shuffle(series1)
    random.shuffle(series2)
    random.shuffle(series3)
    random.shuffle(series4)

    part1 = round((password_length * 30)/100)
    part2 = round((password_length * 20)/100)

    password = []
    for character in range(part1):
        password.append(series1[character])
        password.append(series2[character])
    for character in range(part2):
        password.append(series3[character])
        password.append(series4[character])

    random.shuffle(password)
    password = "".join(password[0:])

    await bot.send_message(message.chat.id, text=password)

    register = message_handler(password_generate)
    await bot.add_handler(register)

print("runnig...")

bot.run()
