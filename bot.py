from nextcord import Interaction, SlashOption, Member
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions,MissingPermissions
import nextcord
import datetime


TESTING_GUILD_IDS = [1224008327621513316]  # Replace with your testing guild id


intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!",intents=intents)


@bot.event
async def on_ready():
    await bot.change_presence(status=nextcord.Status.idle,activity=nextcord.Game("hard to get"))


# command will be global if guild_ids is not specified
@bot.slash_command(description="Ping command",guild_ids=TESTING_GUILD_IDS)
async def ping(interaction: Interaction):
    await interaction.response.send_message("Pong!")


@bot.slash_command(description='Kick a member',guild_ids=TESTING_GUILD_IDS)
@has_permissions(kick_members=True)
async def kick(ctx,member:nextcord.Member,*,reason = None):
    await member.kick(reason=reason)
    await ctx.send(f"user {member} has been kicked")

@kick.error
async def kick_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("you dont have permission to kick")

@bot.slash_command(description='ban a member',guild_ids= [1224008327621513316] )
@has_permissions(ban_members=True)
async def ban(ctx,member:nextcord.Member,*,reason = None):
    await member.ban(reason=reason)
    await ctx.send(f"user {member} has been banned")

@ban.error
async def ban_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("you dont have permission to ban")

@bot.slash_command(description='unban a member',guild_ids= [1224008327621513316] )
@has_permissions(ban_members=True)
async def unban(ctx,member:nextcord.User,*,reason = None):
    guild = ctx.guild
    await guild.unban(user = member)
    await ctx.send(f"user {member} has been unbanned")

@unban.error
async def unban_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("you dont have permission to unban")


@bot.slash_command(description='timeout a member',guild_ids= [1224008327621513316])
@has_permissions(moderate_members=True)
async def timeout(ctx,member:nextcord.Member,time,*,reason=None):
    try:
        resume = datetime.timedelta(minutes=int(time))
        await member.edit(timeout=nextcord.utils.utcnow() + resume,reason=reason)
        await ctx.send(f"{member} timed out for {time} minutes")
    except nextcord.Forbidden:
        await ctx.send('you dont have permission to timeout members')


@bot.slash_command(description='removes timeout from a member',guild_ids= [1224008327621513316])
@has_permissions(moderate_members=True)
async def removetimeout(ctx,member:nextcord.Member,*,reason=None):
    try:
        await member.edit(timeout=nextcord.utils.utcnow(),reason=reason)
        await ctx.send(f"removed {member} from timeout")
    except nextcord.Forbidden:
        await ctx.send('you dont have permission to remove timeout from members')


bot.run("MTIyNDAwMzU2NDUzNjMzNjQ0Ng.GByzHO.cPPb2hKY8g3F0MXFJ-8M8mUrno-phUrJRKsOC4")
