import discord
from discord.ext import commands, tasks
import random

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
client = commands.Bot(command_prefix="!", intents=intents)
allowed_role = "➤ Customer"

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    change_status.start()

@tasks.loop(minutes=1)
async def change_status():
    activity = discord.Activity(type=discord.ActivityType.watching, name="AstraShield #1")
    await client.change_presence(activity=activity)


@client.slash_command(name="keygen", description="Generiert einen Lizenzschlüssel und sendet den Download-Link.")
async def keygen(ctx):
    if not discord.utils.get(ctx.author.roles, name=allowed_role):
        await ctx.send("Du hast keine Berechtigung, diesen Befehl zu verwenden.")
        return
    key = generate_key()
    embed = discord.Embed(
        title="License Key",
        description=f"Hier ist dein Lizenzschlüssel: {key}\n\nKlicke hier um den Download zu starten. \n\nhttps://cdn.discordapp.com/attachments/1043130836331020309/1090254210135761026/REDME.lua",
        color=discord.Color.blue(),
    )
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed)
    await ctx.respond(content="Der Lizenzschlüssel wurde dir per DM geschickt.", ephemeral=True)

def generate_key():
    key_length = 12
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    key = "AstraShield"
    for i in range(key_length):
        key += random.choice(characters)
    return key

client.run("BOT")
