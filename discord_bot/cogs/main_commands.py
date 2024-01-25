import discord
from discord.ext import commands


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


async def setup(bot: commands.Bot):  # Cog 載入 Bot 中
    await bot.add_cog(MainCommands(bot))
