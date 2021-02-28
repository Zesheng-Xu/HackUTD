import discord
async def makeCategory(guild, content):
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=True),
        guild.me: discord.PermissionOverwrite(read_messages=True)
    }
    className = content[len('.class '):]
    category = await guild.create_category(className, overwrites=overwrites)
    await guild.create_text_channel("general", overwrites=overwrites, category=category)

#make vc for every prof
#make text channel for every prof
#async def makeProfChannels(profName):
