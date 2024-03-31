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



bot.run("MTIyNDAwMzU2NDUzNjMzNjQ0Ng.GByzHO.cPPb2hKY8g3F0MXFJ-8M8mUrno-phUrJRKsOC4")
