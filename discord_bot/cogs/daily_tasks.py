from discord.ext import commands, tasks
import time


class TaskBase(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.channel_id = 1199280732439326750

    @commands.command()  # 開始執行函式：hi，使用前綴指令觸發
    async def start_hello(self, ctx: commands.Context):
        await ctx.send("Hi Loop Start.")
        self.hi.start()
        self.start_time = time.time()  # 要放在hi.start()後面才行

    @commands.command()  # 開始執行函式：hi，使用前綴指令觸發
    async def stop_hello(self, ctx: commands.Context):
        await ctx.send("Hi Loop End.")
        self.hi.cancel()

    @tasks.loop(seconds=3)  # 定義要執行的循環函式
    async def hi(self):
        channel = self.bot.get_channel(self.channel_id)
        execution_time = int(time.time() - self.start_time)
        msg = f"{execution_time} sec: Hello, world!"
        print(msg)
        await channel.send(msg)

    @hi.before_loop  # 執行函式前的動作
    async def hi_before(self):
        print("Hi Before.")
        # 等待機器人上線完成
        await self.bot.wait_until_ready()

    @hi.after_loop  # 結束執行函式後的動作
    async def hi_after(self):
        print("Hi After.")


async def setup(bot: commands.Bot):
    await bot.add_cog(TaskBase(bot))
