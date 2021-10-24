import discord
import requests
import json
import asyncio
import random
import os
from decouple import config


#Seting envi variables


client = discord.Client()

gerais = [
  'brasil',
  'MemesBrasil',
  'cellbits',
  'G0ularte',
  'circojeca',
  'dankmemes',
  'eu_nvr',
]


@client.event
async def on_ready():
    print('Logado!!!')
    print('Nome:', client.user.name)
    print('ID:', client.user.id)
    print('Servidores:', len(client.guilds))
    print('Usuarios:', len(client.users))
    print('------')


@client.event
async def on_message(message):
   
    if message.content.startswith('!meme'):
        dados = requests.get(f'https://meme-api.herokuapp.com/gimme/{random.choice(gerais)}')
        meme = json.loads(dados.text)
        embed = discord.Embed(
          title = meme['title'], 
          url = meme['url'],  
          #ups = meme['ups'], 
          #description = '*Apoie o projeto mandando sujestão!!* :trident:',
          description = meme['subreddit'],
          colour = discord.Colour.red()  
        )  
        embed.set_author(name='Sunaa', icon_url='https://cdn.discordapp.com/attachments/637851829396570134/875176423386669086/image5.jpg')
        embed.set_image(url=meme['url'])  
        embed.set_footer(text='~ Sunaa,')
        await message.channel.send(embed=embed)


    if message.content.startswith('!addmeme'):
      comu = message.content
      comu = comu.split(' ')
      gerais.append(comu[1])
      print(gerais)

token = config('BOT_TOKEN')
client.run(token)


#embed.set_thumbnail(url='')
#embed.set_footer(text='teste')
#embed.set_footer(text='teste{}'.format(memeUpvotes)) 
#embed.add_field(name='Nome do field', value='Valor da field',inline=False)
#embed.add_field(name='Nome do field', value='Valor da field',inline=True)

