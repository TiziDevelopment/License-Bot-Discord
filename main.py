import discord #line:1:import discord
from discord .ext import commands ,tasks #line:2:from discord.ext import commands, tasks
import random #line:3:import random
intents =discord .Intents .default ()#line:5:intents = discord.Intents.default()
intents .messages =True #line:6:intents.messages = True
intents .guilds =True #line:7:intents.guilds = True
client =commands .Bot (command_prefix ="!",intents =intents )#line:8:client = commands.Bot(command_prefix="!", intents=intents)
allowed_role ="➤ Customer"#line:9:allowed_role = "➤ Customer"
@client .event #line:11:@client.event
async def on_ready ():#line:12:async def on_ready():
    print (f"Logged in as {client.user}")#line:13:print(f"Logged in as {client.user}")
    change_status .start ()#line:14:change_status.start()
@tasks .loop (minutes =1 )#line:16:@tasks.loop(minutes=1)
async def change_status ():#line:17:async def change_status():
    OOO0O0O00000O0OOO =discord .Activity (type =discord .ActivityType .watching ,name ="AstraShield #1")#line:18:activity = discord.Activity(type=discord.ActivityType.watching, name="AstraShield #1")
    await client .change_presence (activity =OOO0O0O00000O0OOO )#line:19:await client.change_presence(activity=activity)
@client .slash_command (name ="keygen",description ="Generiert einen Lizenzschlüssel und sendet den Download-Link.")#line:22:@client.slash_command(name="keygen", description="Generiert einen Lizenzschlüssel und sendet den Download-Link.")
async def keygen (O0OOOOO0000OOO0OO ):#line:23:async def keygen(ctx):
    if not discord .utils .get (O0OOOOO0000OOO0OO .author .roles ,name =allowed_role ):#line:24:if not discord.utils.get(ctx.author.roles, name=allowed_role):
        await O0OOOOO0000OOO0OO .send ("Du hast keine Berechtigung, diesen Befehl zu verwenden.")#line:25:await ctx.send("Du hast keine Berechtigung, diesen Befehl zu verwenden.")
        return #line:26:return
    O00O0O0OO000O0OOO =generate_key ()#line:27:key = generate_key()
    OO0O00O0O0O000O00 =discord .Embed (title ="License Key",description =f"Hier ist dein Lizenzschlüssel: {O00O0O0OO000O0OOO}\n\nKlicke hier um den Download zu starten. \n\nhttps://cdn.discordapp.com/attachments/1043130836331020309/1090254210135761026/REDME.lua",color =discord .Color .blue (),)#line:32:)
    O000OO0O0000OOO00 =await O0OOOOO0000OOO0OO .author .create_dm ()#line:33:dm_channel = await ctx.author.create_dm()
    await O000OO0O0000OOO00 .send (embed =OO0O00O0O0O000O00 )#line:34:await dm_channel.send(embed=embed)
    await O0OOOOO0000OOO0OO .respond (content ="Der Lizenzschlüssel wurde dir per DM geschickt.",ephemeral =True )#line:35:await ctx.respond(content="Der Lizenzschlüssel wurde dir per DM geschickt.", ephemeral=True)
def generate_key ():#line:37:def generate_key():
    O00O0O00O0OOO0O0O =12 #line:38:key_length = 12
    O0O00O0000O00O0OO ="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"#line:39:characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    OOO000OO0O0OOOOOO ="AstraShield"#line:40:key = "AstraShield"
    for OOOOOO0O0O0OO00O0 in range (O00O0O00O0OOO0O0O ):#line:41:for i in range(key_length):
        OOO000OO0O0OOOOOO +=random .choice (O0O00O0000O00O0OO )#line:42:key += random.choice(characters)
    return OOO000OO0O0OOOOOO #line:43:return key
client .run ("MTAxODg0OTkwMjMyMDY4NTExNg.G0v2FL.q_SxnnTbVMVqewJK64yhQm6bIae4tQTUkK-rGo")#line:45:client.run("MTAxODg0OTkwMjMyMDY4NTExNg.G0v2FL.q_SxnnTbVMVqewJK64yhQm6bIae4tQTUkK-rGo")
