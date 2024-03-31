from nextcord import Interaction, SlashOption
from nextcord.ext import commands

bot = commands.Bot()


# command will be global if guild_ids is not specified
@bot.slash_command(description="Ping command")
async def ping(interaction: Interaction):
    await interaction.response.send_message("Pong!")




@client.slash_command(name='Kick',description='Kick a member',guild_ids=[test_id])
@has_permissions(kick_members=True)
async def kick(ctx,member:nextcord.Member,*,reason = None):
    await member.kick(reason=reason)
    await ctx.send(f"user {member} has been kicked")

@kick.error
async def kick_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("you dont have permission to kick")



bot.run("MTIyNDAwMzU2NDUzNjMzNjQ0Ng.GByzHO.cPPb2hKY8g3F0MXFJ-8M8mUrno-phUrJRKsOC4")
