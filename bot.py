import discord
import json
from secrets import token
from makeChannels import makeChannelCategory
from makeRoles import generateRole
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
    print('We have logged in as {0}'.format(client.user))

#when a message is received
@client.event
async def on_message(message):
    #don't care about message sent by the bot
    if message.author == client.user:
        return
    #command: invite person to a server
    
    if message.content.startswith('.calendar '):
        await message.channel.send('echo!')
    if message.channel.name == "bot-commands":
        if message.content.startswith('.invite '):
            courseInfo = message.content[len('.invite '):]
       	    await message.channel.send('https://discord.gg/{0}'.format(serverDict[courseInfo]))
            generateRole(message.guild, courseInfo)
        #make a category (and populate server)
        if message.content.startswith('.class'):
            guild = message.guild
            for key in data:
                await makeChannelCategory(guild, message.content, data[key], key)

client.run(token)
