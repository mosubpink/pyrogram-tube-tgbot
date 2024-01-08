import os, random, string
from pytube import YouTube
from dotenv import load_dotenv
from pyrogram import Client, types, filters

load_dotenv(dotenv_path='.env')

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

print("runnig...")

bot.run()