import discord
import requests
from discord.ext import commands


def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"图片已保存为 {filename}")
    else:
        print("无法下载图片")


class MainCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()     # 前綴指令
    async def Hello(self, ctx: commands.Context):
        await ctx.send("Hello, world!")

    @commands.Cog.listener()     # 關鍵字觸發
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        if message.content.lower() == "hello":
            await message.channel.send("Hello, world!")

        if message.attachments:
            # 检查附件是否是图片类型
            for attachment in message.attachments:
                if attachment.content_type.startswith('image'):
                    print(f"Message contains image: {attachment.url}")
                    download_image(attachment.url, f'{message.id}.jpg')
                    await message.channel.send("This message contains an image.")
                    break
        else:
            print("Message does not contain any image attachments.")


async def setup(bot: commands.Bot):  # Cog 載入 Bot 中
    await bot.add_cog(MainCommands(bot))
