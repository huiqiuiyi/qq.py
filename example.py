import qq
from config import appid, token
import logging

logging.basicConfig(level=logging.DEBUG)

client = qq.Client()


@client.event
async def on_message(message: qq.message):
    print(message.content)
    if"鼠鼠是不是傻子" in message.content:
        await message.reply("不是")
    if"苟或是不是傻子" in message.content:
        await message.reply("是")


@client.event
async def on_ready():
    print("使用机器人登陆成功。")


if __name__ == '__main__':
    client.run(token=f"{appid}.{token}")
