from nextcord import Interaction, SlashOption, Member
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions,MissingPermissions
import nextcord

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!",intents=intents)

# command will be global if guild_ids is not specified
@bot.slash_command(description="Ping command")
async def ping(interaction: Interaction):
    await interaction.response.send_message("Pong!")




@bot.slash_command(description='Kick a member',guild_ids= [1224008327621513316] )
@has_permissions(kick_members=True)
async def kick(ctx,member:nextcord.Member,*,reason = None):
    await member.kick(reason=reason)
    await ctx.send(f"user {member} has been kicked")

@kick.error
async def kick_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("you dont have permission to kick")

bot.run("MTIyNDAwMzU2NDUzNjMzNjQ0Ng.GByzHO.cPPb2hKY8g3F0MXFJ-8M8mUrno-phUrJRKsOC4")
