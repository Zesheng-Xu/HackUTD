import discord
from makeRoles import generateRole

async def makeChannelCategory(guild, content, profNames, className):

    category = await guild.create_category(className)
    #class_role = await generateRole(guild,category,className)
    #define permission overrite
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        #class_role: discord.PermissionOverwrite(read_messages=True)
    }

    await makeProfChannels(guild, category, profNames)
    await guild.create_voice_channel((className + " VC"), overwrites=overwrites, category=category, position=0)
    await guild.create_text_channel((className + "-calendar"), overwrites=overwrites, category=category, position=1)
    await guild.create_text_channel("general", overwrites=overwrites, category=category, position=1)
    return category

#make text channel for every prof
async def makeProfChannels(guild, category, course):
    #define permission overrite
    
    for professor in course:
        #professor_role = await generateRole(guild, category, professor)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            #professor_role: discord.PermissionOverwrite(read_messages=True)
        }
        await guild.create_text_channel(professor, overwrites=overwrites, category=category)

