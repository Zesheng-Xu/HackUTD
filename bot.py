import discord
import json
from secrets import token
from makeServer import makeCategory
client = discord.Client()

#temporary dictionary for testing
serverDict = {
    "UTDCS": "jmyWcPQU"
}
data = {}
with open("data.json", "r") as read_file:
        data = json.load(read_file)

#when the bot loads
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#when a message is received
@client.event
async def on_message(message):
    #don't care about message sent by the bot
    if message.author == client.user:
        return
    #command: invite person to a server
    if message.content.startswith('.invite '):
        serverName = message.content[len('.invite '):]
        await message.channel.send('https://discord.gg/{0}'.format(serverDict[serverName]))
    #make a category (and populate server)
    if message.content.startswith('.class '):
        guild = message.guild
        print(data)
        await makeCategory(guild, message.content, data["CS 2340"])

client.run(token)