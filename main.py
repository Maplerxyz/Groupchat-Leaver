import json
import discord
import asyncio
import sys,time,random

typing_speed = 90 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')

with open('config.json', 'r') as config:
    get = json.load(config)
token = get['token']
if token == None:
    print("ERROR> You forgot to fill in a token! Go to the config.json file and fill in the token field with your token, or else this program can't run")
    sys.exit()
if token == "PUT YOUR TOKEN HERE":
    print("ERROR> You forgot to fill in a token! Go to the config.json file and fill in the token field with your token, or else this program can't run")
    sys.exit()
client = discord.Client(self_bot=True)

@client.event
async def on_ready():
    print(f"GroupChannel leaver is now activating on {client.user}")
    slow_type(f"Made by https://github.com/maplerxyz")
    await asyncio.sleep(2)
    for gc in client.private_channels:
        if isinstance(gc, discord.GroupChannel):
            try:
                await gc.leave()
                print(f'Successful: {gc.name}')
            except:
                print(f'Failed: {gc.name}')
    print(f"GroupChannel leaver has finished!")

client.run(token, bot=False)
