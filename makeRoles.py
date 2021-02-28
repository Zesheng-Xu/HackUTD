import discord
async def generateRole(guild,category,name):
    default_role = guild.default_role
    role = await guild.create_role(name=name)
    overwrites = {
        default_role: discord.PermissionOverwrite(read_messages=False),
        #role: discord.PermissionOverwrite(read_messages=True)
        }
    await category.set_permissions(role, read_messages=True, send_messages=True)