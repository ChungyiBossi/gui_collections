import os
import json
import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():  # 當機器人完成啟動時
    slash = await bot.tree.sync()
    print(f"載入 {len(slash)} 個斜線指令")
    print(f"目前登入身份 --> {bot.user}")


@bot.command()  # 載入指令程式檔案
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} done.")


@bot.command()
async def unload(ctx, extension):  # 卸載指令檔案
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"UnLoaded {extension} done.")


@bot.command()  # 重新載入程式檔案
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    msg = f"Re-Loaded {extension} done."
    print(msg)
    await ctx.send(msg)


async def load_extensions():  # 一開始bot開機需載入全部程式檔案
    for filename in os.listdir("./cogs"):  # 讀取cogs資料夾下所有檔案
        if filename.endswith(".py"):  # 取得.py
            await bot.load_extension(f"cogs.{filename[:-3]}")  # 讀取extension


async def main():
    with open('./tokens.json', 'r') as token_file:
        content = token_file.read()
        tokens_data = json.loads(content)
    async with bot:
        print("Loading Extensions....")
        await load_extensions()
        await bot.start(tokens_data['tokens'])

# 確定執行此py檔才會執行
if __name__ == "__main__":
    asyncio.run(main())
