from nextcord import Interaction
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions,MissingPermissions
import nextcord
import datetime
import json
import requests


 # Replace with your testing guild id

guild_ids = [1224008327621513316]

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents)


@bot.event
async def on_ready():
    await bot.change_presence(status=nextcord.Status.idle,activity=nextcord.Game("hard to get"))


# command will be global if guild_ids is not specified
@bot.slash_command(description="Ping command",guild_ids=guild_ids)
async def ping(interaction: Interaction):
    await interaction.response.send_message("Pong!")


@bot.slash_command(description='Kick a member',guild_ids=guild_ids)
@has_permissions(kick_members=True)
async def kick(interaction: Interaction,member:nextcord.Member,*,reason = None):
    await member.kick(reason=reason)
    await interaction.send(f"user {member} has been kicked")

@kick.error
async def kick_error(interaction: Interaction,error):
    if isinstance(error,commands.MissingPermissions):
        await interaction.send("you dont have permission to kick")

@bot.slash_command(description='ban a member',guild_ids= guild_ids )
@has_permissions(ban_members=True)
async def ban(interaction: Interaction,member:nextcord.Member,*,reason = None):
    await member.ban(reason=reason)
    await interaction.send(f"user {member} has been banned")

@ban.error
async def ban_error(interaction: Interaction,error):
    if isinstance(error,commands.MissingPermissions):
        await interaction.send("you dont have permission to ban")

@bot.slash_command(description='unban a member',guild_ids= guild_ids )
@has_permissions(ban_members=True)
async def unban(interaction: Interaction,member:nextcord.User,*,reason = None):
    guild = interaction.guild
    await guild.unban(user = member)
    await interaction.send(f"user {member} has been unbanned")

@bot.slash_command(description='mute a member from voice channels',guild_ids= guild_ids )
@has_permissions(mute_members=True)
async def mute_voice(interaction: Interaction,member:nextcord.Member,*,reason=None):
    await member.edit(mute=True,reason=reason)
    await interaction.send(f"{member} voice muted")

@bot.slash_command(description='unmute a member from voice channels',guild_ids= guild_ids )
@has_permissions(mute_members=True)
async def unmute_voice(interaction: Interaction,member:nextcord.Member,*,reason=None):
    await member.edit(mute=False,reason=reason)
    await interaction.send(f"{member} voice unmuted")

@bot.slash_command(description='deafen a member',guild_ids= guild_ids )
@has_permissions(deafen_members=True)
async def deafen(interaction: Interaction,member:nextcord.Member,*,reason=None):
    await member.edit(deafen=True,reason=reason)
    await interaction.send(f"{member} deafened")

@bot.slash_command(description='undeafen a member',guild_ids= guild_ids )
@has_permissions(deafen_members=True)
async def undeafen(interaction: Interaction,member:nextcord.Member,*,reason=None):
    await member.edit(deafen=False,reason=reason)
    await interaction.send(f"{member} undeafened")

@bot.slash_command(description='enable slowmode',guild_ids= guild_ids )
@has_permissions(manage_channels=True)
async def slowmode(interaction: Interaction,time,*,reason=None):
    await interaction.channel.edit(slowmode_delay=time,reason=reason)
    await interaction.send(f"slowmode enabled for {time} seconds")

@unban.error
async def unban_error(interaction: Interaction,error):
    if isinstance(error,commands.MissingPermissions):
        await interaction.send("you dont have permission to unban")


@bot.slash_command(description='timeout a member',guild_ids= guild_ids)
@has_permissions(moderate_members=True)
async def timeout(interaction: Interaction,member:nextcord.Member,time,*,reason=None):
    try:
        resume = datetime.timedelta(minutes=int(time))
        await member.edit(timeout=nextcord.utils.utcnow() + resume,reason=reason)
        await interaction.send(f"{member} timed out for {time} minutes")
    except nextcord.Forbidden:
        await interaction.send('you dont have permission to timeout members')


@bot.slash_command(description='removes timeout from a member',guild_ids= guild_ids)
@has_permissions(moderate_members=True)
async def removetimeout(interaction: Interaction,member:nextcord.Member,*,reason=None):
    try:
        await member.edit(timeout=nextcord.utils.utcnow(),reason=reason)
        await interaction.send(f"removed {member} from timeout")
    except nextcord.Forbidden:
        await interaction.send('you dont have permission to remove timeout from members')

@bot.slash_command(description="mutes a member from texting",guild_ids=guild_ids)
@has_permissions(mute_members=True)
async def mute_text(interaction:Interaction,member:nextcord.Member,*,reason=None):
    role = nextcord.utils.get(interaction.guild.roles,name="Muted")
    guild = interaction.guild
    if role not in guild.roles:
        perm = nextcord.Permissions(send_messages=False)
        guild.create_role(name="Muted",permissions=perm)
    await member.add_roles(role,reason=reason)
    await interaction.send(f'{member} was muted from text channels')

@bot.slash_command(description="unmutes a member from texting",guild_ids=guild_ids)
@has_permissions(mute_members=True)
async def unmute_text(interaction:Interaction,member:nextcord.Member,*,reason=None):
    role = nextcord.utils.get(interaction.guild.roles,name="Muted")
    await member.remove_roles(role,reason=reason)
    await interaction.send(f'{member} was unmuted from text channels')

@bot.slash_command(description="tell a joke",guild_ids=guild_ids)
async def joke(interaction:Interaction):
    data = requests.get(r"https://official-joke-api.appspot.com/random_joke")
    tt = json.loads(data.text)
    await interaction.send(f"{tt['setup']}\n{tt['punchline']}")


bot.run("MTIyNDAwMzU2NDUzNjMzNjQ0Ng.Gek1Bp.fgRcYwYI5WPh7vPAMiDPcZKPSOgDSLVMi6R5I0")
