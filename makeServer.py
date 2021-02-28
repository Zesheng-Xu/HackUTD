import discord
async def makeCategory(guild, content, profNames):
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=True),
        guild.me: discord.PermissionOverwrite(read_messages=True)
    }
    className = content[len('.class '):]
    category = await guild.create_category(className, overwrites=overwrites)
    await makeProfChannels(guild, category, profNames)
    await guild.create_voice_channel((className + " VC"), overwrites=overwrites, category=category, position=0)
    await guild.create_text_channel("general", overwrites=overwrites, category=category, position=1)

#make vc for every prof
#make text channel for every prof
async def makeProfChannels(guild, category, profNames):
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True)
    }
    for prof in profNames:
        await guild.create_text_channel(prof, overwrites=overwrites, category=category)

