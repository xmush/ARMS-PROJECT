import requests, json, os
from flask import Blueprint, jsonify, make_response
from flask_restful import Api, reqparse, Resource, marshal
from blueprints import app
import discord, random
# from flask_jwt_extended import jwt_required

bp_discord = Blueprint('discord', __name__)
api = Api(bp_discord)

TOKEN = app.config['DISCORD_TOKEN']
GUILD = app.config['DISCORD_CONFIG']

class RunTheDiscord(Resource) :

    def __init__(self) :
        pass

    def get(self) :
        
        client = discord.Client()

        @client.event
        async def on_ready():
            print(f'{client.user.name} has connected to Discord!')

        @client.event
        async def on_member_join(member):
            await member.create_dm()
            await member.dm_channel.send(
                f'Hi {member.name}, welcome to my Discord server!'
            )

        pesan = []
        @client.event
        async def on_message(message):
            if message.author == client.user:
                return
            
            if message.content == 'doc':
                response = 'Dokumentasi disini'
                await message.channel.send(response)
            elif message.content == 'quit' :
                await message.channel.send(pesan)
                await client.close()
            elif message.content == 'start' or len(pesan) > 0:
                if len(pesan) == 0 :
                    await message.channel.send('Your name : ')
                elif len(pesan) == 1 :
                    await message.channel.send('Your BOD : ')
                elif len(pesan) == 2 :
                    await message.channel.send('Partner name  : ')
                elif len(pesan) == 3 :
                    await message.channel.send('Partner BOD : ')
                else :
                    await message.channel.send('Waiiit..')
            else :
                response = message.content
                pesan.append(response)
                await message.channel.send(response)
            # elif message.content == ''

        client.run(TOKEN)

api.add_resource(RunTheDiscord, '')
# app.add_resource (RunTheDiscord, '')