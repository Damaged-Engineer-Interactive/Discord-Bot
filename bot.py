from nextcord import Interaction, SlashOption, Member
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions,MissingPermissions
import nextcord
import datetime


 # Replace with your testing guild id

guild_ids = [1224008327621513316]

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!",intents=intents)


@bot.event
async def on_ready():
    await bot.change_presence(status=nextcord.Status.idle,activity=nextcord.Game("hard to get"))


# command will be global if guild_ids is not specified
@bot.slash_command(description="Ping command",guild_ids=guild_ids)
async def ping(interaction: Interaction):
    await interaction.response.send_message("Pong!")


@bot.slash_command(description='Kick a member',guild_ids=guild_ids)
@has_permissions(kick_members=True)
async def kick(ctx,member:nextcord.Member,*,reason = None):
    await member.kick(reason=reason)
    await ctx.send(f"user {member} has been kicked")

@kick.error
async def kick_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("you dont have permission to kick")

@bot.slash_command(description='ban a member',guild_ids= guild_ids )
@has_permissions(ban_members=True)
async def ban(ctx,member:nextcord.Member,*,reason = None):
    await member.ban(reason=reason)
    await ctx.send(f"user {member} has been banned")

@ban.error
async def ban_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("you dont have permission to ban")

@bot.slash_command(description='unban a member',guild_ids= guild_ids )
@has_permissions(ban_members=True)
async def unban(ctx,member:nextcord.User,*,reason = None):
    guild = ctx.guild
    await guild.unban(user = member)
    await ctx.send(f"user {member} has been unbanned")

@bot.slash_command(description='mute a member',guild_ids= guild_ids )
@has_permissions(mute_members=True)
async def mute(ctx,member:nextcord.Member,*,reason=None):
    await member.edit(mute=True,reason=reason)
    await ctx.send(f"{member} muted")

@bot.slash_command(description='unmute a member',guild_ids= guild_ids )
@has_permissions(mute_members=True)
async def unmute(ctx,member:nextcord.Member,*,reason=None):
    await member.edit(mute=False,reason=reason)
    await ctx.send(f"{member} unmuted")

@bot.slash_command(description='deafen a member',guild_ids= guild_ids )
@has_permissions(deafen_members=True)
async def deafen(ctx,member:nextcord.Member,*,reason=None):
    await member.edit(deafen=True,reason=reason)
    await ctx.send(f"{member} deafened")

@bot.slash_command(description='undeafen a member',guild_ids= guild_ids )
@has_permissions(deafen_members=True)
async def undeafen(ctx,member:nextcord.Member,*,reason=None):
    await member.edit(deafen=False,reason=reason)
    await ctx.send(f"{member} undeafened")

@bot.slash_command(description='enable slowmode',guild_ids= guild_ids )
@has_permissions(manage_channels=True)
async def slowmode(ctx,time,*,reason=None):
    await ctx.channel.edit(slowmode_delay=time,reason=reason)
    await ctx.send(f"slowmode enabled for {time} seconds")

@unban.error
async def unban_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("you dont have permission to unban")


@bot.slash_command(description='timeout a member',guild_ids= guild_ids)
@has_permissions(moderate_members=True)
async def timeout(ctx,member:nextcord.Member,time,*,reason=None):
    try:
        resume = datetime.timedelta(minutes=int(time))
        await member.edit(timeout=nextcord.utils.utcnow() + resume,reason=reason)
        await ctx.send(f"{member} timed out for {time} minutes")
    except nextcord.Forbidden:
        await ctx.send('you dont have permission to timeout members')


@bot.slash_command(description='removes timeout from a member',guild_ids= guild_ids)
@has_permissions(moderate_members=True)
async def removetimeout(ctx,member:nextcord.Member,*,reason=None):
    try:
        await member.edit(timeout=nextcord.utils.utcnow(),reason=reason)
        await ctx.send(f"removed {member} from timeout")
    except nextcord.Forbidden:
        await ctx.send('you dont have permission to remove timeout from members')


bot.run("MTIyNDAwMzU2NDUzNjMzNjQ0Ng.GByzHO.cPPb2hKY8g3F0MXFJ-8M8mUrno-phUrJRKsOC4")
