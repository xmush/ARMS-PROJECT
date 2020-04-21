import os
import random

import discord, requests
from dotenv import load_dotenv
from discord.ext.commands import Bot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
# bot = Bot("!")

@client.event
aslync def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    

    # brooklyn_99_quotes = [
    #     'I\'m the human form of the 💯 emoji.',
    #     'Bingpot!',
    #     (
    #         'Cool. Cool cool cool cool cool cool cool, '
    #         'no doubt no doubt no doubt no doubt.'
    #     ),
    # ]

    if message.content == 'zodiac!':
        name1 = input("masukan nama anda: ")
        bod1 = input("dd-mm-yyyy: ")
        name2 = input("masukan nama pasangan: ")
        bod2 = input("dd-mm-yyyy: ")
        rq = requests.get('http://0.0.0.0:5000/mine?name1='+name1+'&bod1='+bod1+'&name2='+name2+'&bod2='+bod2+'')
        RQ = rq.json()['response']['mental'][0]
        # ,rq.json()['partner_traits']['mental'][0]] 
        response = RQ
        await message.channel.send(response)




# def check(ctx):
#     return lambda m: m.author == ctx.author and m.channel == ctx.channel

# async def get_input_of_type(func, ctx):
#     while True:
#         try:
#             msg = await bot.wait_for('message', check=check(ctx))
#             return func(msg.content)
#         except ValueError:
#             continue

# @bot.command()
# async def calc(ctx):
#     await ctx.send("What is the first number?")
#     firstnum = await get_input_of_type(int, ctx)
#     await ctx.send("What is the second number?")
#     secondnum = await get_input_of_type(int, ctx)
#     await ctx.send(f"{firstnum} + {secondnum} = {firstnum+secondnum}")

client.run(TOKEN)