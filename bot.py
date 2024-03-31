from nextcord import Interaction, SlashOption
from nextcord.ext import commands

TESTING_GUILD_ID = 1224008327621513316  # Replace with your testing guild id

bot = commands.Bot()


# command will be global if guild_ids is not specified
@bot.slash_command(guild_ids=[TESTING_GUILD_ID], description="Ping command")
async def ping(interaction: Interaction):
    await interaction.response.send_message("Pong!")


@bot.slash_command(guild_ids=[TESTING_GUILD_ID], description="Repeats your message")
async def echo(interaction: Interaction, arg: str = SlashOption(description="Message")):
    await interaction.response.send_message(arg)


@bot.slash_command(guild_ids=[TESTING_GUILD_ID], description="Choose a number")
async def enter_a_number(
    interaction: Interaction,
    number: int = SlashOption(description="Your number", required=False),
):
    if not number:
        await interaction.response.send_message("No number was specified!", ephemeral=True)
    else:
        await interaction.response.send_message(f"You chose {number}!")



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
