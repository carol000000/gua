# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
import random
import asyncio




# intents
intents = discord.Intents.default()
# client
client = discord.Client(intents=intents)



intents = discord.Intents.default()
intents.message_content = True
gua = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="!",intents=intents)


@gua.event
async def on_ready():
    print(f'We have logged in as {gua.user}')
    CHANNEL_ID = 1476227328370540797
    try:
        
        channel = await gua.fetch_channel(CHANNEL_ID)
        await channel.send("<@1149703872424726558> 機器人開啟")
        print("成功發送訊息！")
    except Exception as e:
        print(f"出錯了：{e}")

@gua.event
async def on_message(message):
    if message.author == gua.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('呱'):
        await message.channel.send('呱呱在拉屎')

    if message.content.startswith('ping'):
        await message.channel.send('pong')
##-------------------------------------------------------------------------------------------------------------------------------------------------------
    if message.content.startswith("早安"):
        f = random.randint(0,2)
        if f == 0:
            await message.channel.send(f"早安{message.author.mention} 要玩'猜數字'嗎?")
        if f == 1:
            await message.channel.send(f"早安{message.author.mention} 祝你有美好的一天")
        if f == 2:
            await message.channel.send(f"早安{message.author.mention} 試試看輸入'運勢'")

    if message.content.startswith("午安"):
        g = random.randint(0,2)
        if g == 0:
            await message.channel.send(f"午安{message.author.mention} 要玩'猜數字'嗎?")
        if g == 1:
            await message.channel.send(f"午安{message.author.mention} 午餐想吃啥？")
        if g == 2:
            await message.channel.send(f"午安{message.author.mention} 要不要輸入'運勢'")

    if message.content.startswith("晚安"):
        f = random.randint(0,2)
        if f == 0:
            await message.channel.send(f"晚安{message.author.mention} 要通霄嗎？")
        if f == 1:
            await message.channel.send(f"晚安{message.author.mention} 祝你一覺到天亮")
        if f == 2:
            await message.channel.send(f"晚安{message.author.mention} 拉屎好讚(呱呱正在拉屎中)")
##---------------------------------------------------------------------------------------------------------------------------------------------------------
    if message.content.startswith("運勢"):
        a = random.randint(0,2)
        if a == 0:
            await message.channel.send("吉")
        if a == 1:
            await message.channel.send("普")
        if a == 2:
            await message.channel.send("凶")


##---------------------------------------------------------------------------------------------------------------------------------------------------------
    if message.content.startswith("猜數字"):
        b = random.randint(1,100)
        gua_count =0
        await message.channel.send(f"{message.author.mention}1~100")
        def check(m):
            return(m.author==message.author and m.channel== message.channel and m.content.isdigit())

        
        while True:
            
            try:
                gua_message=await gua.wait_for("message",check=check,timeout=30.0)
            except:
                await message.channel.send(f"{message.author.mention}超時結束")
                break
            user_boon = int(gua_message.content)
            gua_count +=1
            if user_boon>b:
                await message.channel.send(f"{message.author.mention}太大")
            elif user_boon<b:
                await message.channel.send(f"{message.author.mention}太小")
            else:
                await message.channel.send(f"{message.author.mention}猜對了 答案是{b} 你猜了{gua_count}次")
                break
##-------------------------------------------------------------------------------------------------------------------------------------------------------
    if message.content.startswith("幹"):
        await message.channel.send(f"{message.author.mention}罵髒話")


            



gua.run("")
