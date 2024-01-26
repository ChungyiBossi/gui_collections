from discord.ext import commands, tasks
import time
import types


class TaskBase(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()  # 開始執行<task_name>，使用前綴指令觸發
    async def start_task(self, ctx: commands.Context, task_name):
        await ctx.send(f"Coroutine Task-{task_name} Start.")
        try:
            if hasattr(self.__class__, task_name):
                eval(f"self.{task_name}.start()")
        except Exception as e:
            print('Find exception while start task: ', e)

    @commands.command()  # 停止執行<task_name>，使用前綴指令觸發
    async def stop_task(self, ctx: commands.Context, task_name):
        await ctx.send(f"Coroutine Task:{task_name} End.")
        try:
            if hasattr(self.__class__, task_name):
                eval(f"self.{task_name}.cancel()")
        except Exception as e:
            print('Find exception while stop task: ', e)


class TaskHi(TaskBase):
    def __init__(self, bot: commands.Bot):
        super().__init__(bot)
        self.channel_id = 1199280732439326750
        print(self.hi)

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
        self.start_time = time.time()
        await self.bot.wait_until_ready()

    @hi.after_loop  # 結束執行函式後的動作
    async def hi_after(self):
        print("Hi After.")


async def setup(bot: commands.Bot):
    await bot.add_cog(TaskHi(bot))
