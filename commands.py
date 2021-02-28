@client.event
async def command():
    if message.channel.name == "bot-commands" and message.content.startswith('.invite '):
        serverName = message.content[len('.invite '):]
        await message.channel.send('https://discord.gg/{0}'.format(serverDict[serverName]))
    
