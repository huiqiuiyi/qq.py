import qq
from qq.ext import commands
from config import appid, token
import logging

logging.basicConfig(level=logging.DEBUG)

intent = qq.Intents.default()
intent.guild_messages = True
intent.at_guild_messages = False
bot = commands.Bot(command_prefix="/", owner_id=114514, intents=intent)


@bot.command(name="组合")
async def test(ctx: commands.Context, one: str, two: str):
    await ctx.reply(one + two)


@bot.command(name="重复")
async def test(ctx: commands.Context, one: str):
    await ctx.reply(one)


if __name__ == '__main__':
    bot.run(token=f"{appid}.{token}")