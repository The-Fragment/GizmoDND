import discord
import time
client = discord.Client()
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Rolling for initiative...'))
    print("Ready to roll!")
    print("--------------")
    print (time.strftime("Time at start:\n"+"%H:%M:%S"))
    #await client.change_presence(status=discord.Status.dnd, activity=discord.ActivityType.watching('Star Wars')) -- Alternatives,
    # You've gotta lot of options with these

client.run('NzYzMjEyNzg0NzExMzY4NzE1.X30bSw.tp2tlQU4e8GdwvCGYtmHM1Xaalw')