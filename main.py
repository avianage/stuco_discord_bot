import discord
from discord.ext import commands

import os

client = commands.Bot(command_prefix="$")


@client.event
async def on_ready():
    print('We have logged as {0.user}'.format(client))


client.run(os.getenv('TOKEN'))
