import discord
async def makeChannelCategory(guild, content, profNames, className):
    #define permission overrite
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=True),
        guild.me: discord.PermissionOverwrite(read_messages=True)
    }
    category = await guild.create_category(className, overwrites=overwrites)
    await makeProfChannels(guild, category, profNames)
    await guild.create_voice_channel((className + " VC"), overwrites=overwrites, category=category, position=0)
    await guild.create_text_channel("general", overwrites=overwrites, category=category, position=1)

#make vc for every prof
#make text channel for every prof
async def makeProfChannels(guild, category, course):
    #define permission overrite
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True)
    }
    for professor in course:
        await guild.create_text_channel(professor, overwrites=overwrites, category=category)

