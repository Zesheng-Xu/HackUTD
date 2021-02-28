import discord
async def generateRole(guild,courseInfo):
    await guild.create_role(name=courseInfo)


