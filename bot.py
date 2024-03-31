from nextcord import Interaction, SlashOption
from nextcord.ext import commands

bot = commands.Bot()


# command will be global if guild_ids is not specified
@bot.slash_command(description="Ping command")
async def ping(interaction: Interaction):
    await interaction.response.send_message("Pong!")




bot.run("MTIyNDAwMzU2NDUzNjMzNjQ0Ng.GByzHO.cPPb2hKY8g3F0MXFJ-8M8mUrno-phUrJRKsOC4")
