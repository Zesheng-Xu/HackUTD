import discord
from secrets import token
client = discord.Client()

serverDict = {
"UTDCS": "https://discord.gg/jmyWcPQU"
}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.invite '):
        serverName = message.content[len('.invite '):]
        await message.channel.send(serverDict[serverName])

client.run(token)



