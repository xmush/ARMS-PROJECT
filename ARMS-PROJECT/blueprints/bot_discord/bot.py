import os
import random

import discord, requests
from dotenv import load_dotenv
from discord.ext.commands import Bot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
bot = Bot("!")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        print(f'Hi {member.name}, welcome to my Discord server!'
    ))

# def dicttomsg(dict1) :
#     s= ''
#     for index, key in enumerate(dict1):
#         s += key+'\n'
#         if type(dict1[key]) == type({}) :
#             for ind, k in enumerate(dict1[key]) :
#                 s += str(k)+'\n'
#                 if type(dict1[key][k]) == type([]) :
                    
#                     for item in dict1[key][k] :
#                         x = str(item.index)+item.replace("\n", '')
#                         s += item+'\n'
#                     s+='\n'
#                 continue
#     s += str(dict1[key])+'\n\n'
#     return s

@client.event
async def on_message(message):
    if message.content ==('bot!'):
        response = "Bot Command! \n mengetahui zodiac \n format = zodiac<spasi>nama<spasi>dd-mm-yyyy<spasi>nama<spasi>dd-mm-yyyy"
        await message.channel.send(response)  
    if message.content.startswith('zodiac '):
        vals = message.content.split(" ")
        name1 = str(vals[1])
        bod1 = str(vals[2])
        name2 = str(vals[3])
        bod2 = str(vals[4])
        rq = requests.get('http://0.0.0.0:5000/mine?name1='+name1+'&bod1='+bod1+'&name2='+name2+'&bod2='+bod2+'')
        RQ = rq.json()
        # response = RQ
        a = str(name1)
        b = str(name2)
        kotak = ''
        boy = ":boy: YourZodiac : **%s** \n" % (RQ[a])
        girl = ":girl: YourPartnerZodiac : **%s** \n" % (RQ[b])
        zod = ":boy: ZodiacPartnerSuggest : **%s** \n" % (RQ['partner_recommend_zodiac'])
        com = "Compability : **%s** \n :heart:" % (RQ['compatibility_status'])
        kotak = kotak + boy + girl + zod + com
        await message.channel.send(kotak)


client.run(TOKEN)