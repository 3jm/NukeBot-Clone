import nextcord
from nextcord.ext import commands
from nextcord import Interaction

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    testing_guild_id = 1017999660603944960

    @nextcord.slash_command(guild_ids=[testing_guild_id], description="Shows the bot's latency")
    async def ping(self, interaction: Interaction):
        await interaction.response.defer()
        # send a embed with the latecny
        em = nextcord.Embed(
            # get the bots latency and websockets latency
            description = f"**Bot Latency:** {round(self.bot.latency * 1000)}ms",
            color = 0x202225
        )
        await interaction.followup.send(embed = em)

def setup(bot):
    bot.add_cog(ping(bot))