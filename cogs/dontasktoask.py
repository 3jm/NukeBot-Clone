import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class dontasktoask(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    testing_guild_id = 1017999660603944960

    @nextcord.slash_command(guild_ids=[testing_guild_id], description="Advices to not ask to ask but to ask instead")
    async def dontasktoask(self, interaction: Interaction, user: nextcord.Member = SlashOption(name="user", description="The user to ping", required=False)):
        await interaction.response.defer()
        if user is None:
            await interaction.followup.send("https://dontasktoask.com/")
        else:
            await interaction.followup.send(f"{user.mention} https://dontasktoask.com/")

def setup(bot):
    bot.add_cog(dontasktoask(bot))