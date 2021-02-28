import discord
import json
import time
from secrets import token
from makeChannels import makeChannelCategory
from makeRoles import generateRole
from myCalendar import myCalendar

# import startCalendar
client = discord.Client()
events = []

# temporary dictionary for testing
serverDict = {
    "UTDCS": "jmyWcPQU"
}
data = {}
with open("data.json", "r") as read_file:
    data = json.load(read_file)


# when the bot loads
@client.event
async def on_ready():
    print('We have logged in as {0}'.format(client.user))


# when a message is received
@client.event
async def on_message(message):
    # don't care about message sent by the bot
    if message.author == client.user:
        return
    # if message.content.startswith('.event '):
    #
    #     if ("CALENDAR" in message.channel.name.upper()):
    #
    #         category_name = message.channel.name.replace(" ", "").upper()
    #         print(category_name)
    #
    #         contents = message.content.split(" ")
    #         already_e = False
    #         if len(contents) != 5:
    #             await message.channel.send(
    #                 "Please enter in format of .event [class] [professor] [event_type] [m/d/y] ")
    #         else:
    #             cevent = myCalendar()
    #             cevent.devent(contents[1].strip(" ").replace(" ", "").upper(),
    #                           contents[2].strip(" ").replace(" ", "").upper(),
    #                           contents[3].strip(" ").replace(" ", "").upper(),
    #                           contents[4].strip(" ").replace(" ", "").upper())
    #             for e in events:
    #                 if e.equals(cevent):
    #                     already_e = True
    #             if not already_e and len(events) != 0:
    #                 await message.channel.send("Event already exists")
    #             else:
    #                 events.append(cevent)
    #         if message.content.startswith('.delete_event '):
    #             contents = message.content.split(" ")
    #             already_e = False
    #             if len(contents) != 5:
    #                 await message.channel.send(
    #                     "Please enter in format of .delete_event [class] [professor] [event_type] [m/d/y] ")
    #             else:
    #                 cevent = myCalendar()
    #                 cevent.devent(contents[1].strip(" ").replace(" ", "").upper(),
    #                               contents[2].strip(" ").replace(" ", "").upper(),
    #                               contents[3].strip(" ").replace(" ", "").upper(),
    #                               contents[4].strip(" ").replace(" ", "").upper())
    #                 for e in events:
    #                     if e.equals(cevent):
    #                         already_e = True
    #                         events.remove(e)
    #                 if not already_e and len(events) != 0:
    #                     await message.channel.send("No such event")
    #
    #         if message.content.startswith('.due '):
    #             contents = message.content.split(" ")
    #             class_name = message.channel.name
    #             count = 0
    #             print(".due received")
    #             if (len(contents) == 1):
    #                 for e in events:
    #                     # if temp_e.replace(" ","").upper() == temp_e.get_class().replace(" ","").upper():
    #                     t = str(time.localtime(time.time()))
    #                     temp = t.split(",")
    #                     month = temp[1][temp[1].rfind("=") + 1:]
    #                     day = temp[2][temp[2].rfind("=") + 1:]
    #                     year = temp[0][temp[0].rfind("=") + 1:]
    #
    #                     event_time = e.get_date().split("/")
    #                     m = event_time[0]
    #                     d = event_time[1]
    #                     y = event_time[2]
    #                     time_left = int(y) * 365 + int(m) * 30 + int(d) - (
    #                             int(year) * 365 + int(month) * 30 + int(day))
    #                     if e.get_class().upper() in category_name:
    #                         await message.channel.send(e.toString() + "\t" + str(time_left) + " days to due")
    #             elif (len(contents) == 2):
    #
    #                 contents[1] = contents[1].strip(" ").replace(" ", "").upper()
    #
    #                 for e in events:
    #                     if contents[1] == e.get_classes():
    #                         t = str(time.localtime(time.time()))
    #                         temp = t.split(",")
    #                         month = temp[1][temp[1].rfind("=") + 1:]
    #                         day = temp[2][temp[2].rfind("=") + 1:]
    #                         year = temp[0][temp[0].rfind("=") + 1:]
    #
    #                         event_time = e.get_date().split("/")
    #                         m = event_time[0]
    #                         d = event_time[1]
    #                         y = event_time[2]
    #                         time_left = int(y) * 365 + int(m) * 30 + int(d) - (
    #                                 int(year) * 365 + int(month) * 30 + int(day))
    #                         if e.get_class().upper() in category_name:
    #                             await message.channel.send(e.toString() + "\t" + str(time_left) + " days to due")
    #             elif (len(contents) == 3):
    #
    #                 contents[1] = contents[1].strip(" ").replace(" ", "").upper()
    #                 contents[2] = contents[2].strip(" ").replace(" ", "").upper()
    #
    #                 for e in events:
    #                     if contents[1] == e.get_class() and contents[2] == e.get_professor():
    #                         t = str(time.localtime(time.time()))
    #                         temp = t.split(",")
    #                         month = temp[1][temp[1].rfind("=") + 1:]
    #                         day = temp[2][temp[2].rfind("=") + 1:]
    #                         year = temp[0][temp[0].rfind("=") + 1:]
    #
    #                         event_time = e.get_date().split("/")
    #                         m = event_time[0]
    #                         d = event_time[1]
    #                         y = event_time[2]
    #                         time_left = int(y) * 365 + int(m) * 30 + int(d) - (
    #                                 int(year) * 365 + int(month) * 30 + int(day))
    #                         if e.get_class().upper() in category_name:
    #                             await message.channel.send(e.toString() + "\t" + str(time_left) + " days to due")
    #
    #             elif (len(contents) == 4):
    #                 contents[1] = contents[1].strip(" ").replace(" ", "").upper()
    #                 contents[2] = contents[2].strip(" ").replace(" ", "").upper()
    #                 contents[3] = contents[3].strip(" ").replace(" ", "").upper()
    #
    #                 for e in events:
    #                     if contents[1] == e.get_class() and contents[2] == e.get_professor() and contents[
    #                         3] == e.get_event():
    #                         t = str(time.localtime(time.time()))
    #                         temp = t.split(",")
    #                         month = temp[1][temp[1].rfind("=") + 1:]
    #                         day = temp[2][temp[2].rfind("=") + 1:]
    #                         year = temp[0][temp[0].rfind("=") + 1:]
    #
    #                         event_time = e.get_date().split("/")
    #                         m = event_time[0]
    #                         d = event_time[1]
    #                         y = event_time[2]
    #                         time_left = int(y) * 365 + int(m) * 30 + int(d) - (
    #                                 int(year) * 365 + int(month) * 30 + int(day))
    #                         if e.get_class().upper() in category_name:
    #                             await message.channel.send(
    #                                 e.toString() + "\t" + str(time_left) + " days to due")
    #             elif (len(contents) == 5):
    #                 contents[1] = [1].strip(" ").replace(" ", "").upper()
    #                 contents[2] = contents[2].strip(" ").replace(" ", "").upper()
    #                 contents[3] = contents[3].strip(" ").replace(" ", "").upper()
    #                 contents[4] = contents[4].strip(" ").replace(" ", "").upper()
    #                 await message.channel.send("Do the math yourself will ya?")
    #                 for e in events:
    #                     if contents[1] == e.get_class() and contents[2] == e.get_professor() and contents[
    #                         3] == e.get_event() and contents[4] == e.get_date():
    #                         t = str(time.localtime(time.time()))
    #                         temp = t.split(",")
    #                         month = temp[1][temp[1].rfind("=") + 1:]
    #                         day = temp[2][temp[2].rfind("=") + 1:]
    #                         year = temp[0][temp[0].rfind("=") + 1:]
    #
    #                         event_time = e.split("/")
    #                         m = event_time[0]
    #                         d = event_time[1]
    #                         y = event_time[2]
    #                         time_left = int(y) * 365 + int(m) * 30 + int(d) - (
    #                                 int(year) * 365 + int(month) * 30 + int(day))
    #                         if e.get_class().upper() in category_name:
    #                             await message.channel.send(
    #                                 e.toString() + "\t" + str(time_left) + " days to due")
    #     else:
    #         await message.channel.send("Please use calendar commands in calendar channels only")
    #only allow these commands in bot commands channel
    if message.channel.name == "bot-commands":
        #invite person to a server
        if message.content.startswith('.invite '):
            courseInfo = message.content[len('.invite '):]
            await message.channel.send('https://discord.gg/{0}'.format(serverDict[courseInfo]))

        #initialize guild for use
        #print(message.author.id, message.guild.owner_id)
        if message.content.startswith('.init'):  # and message.author.id == message.guild.owner_id:
            print("new server initializing")
            guild = message.guild
            for key in data:
                category = await makeChannelCategory(guild, message.content, data[key], key)

client.run(token)