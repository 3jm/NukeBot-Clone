import nextcord, random
from nextcord.ext import commands
from nextcord import Interaction

arr = []
for i in range(0, 100):
    arr.append(i)

class howgay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    testing_guild_id = 1017999660603944960

    @nextcord.slash_command(guild_ids=[testing_guild_id], description="How gay are you")
    async def howgay(self, interaction: Interaction):
        await interaction.response.defer()
        youaregay = random.choice(arr)
        em = nextcord.Embed(
            description=f"You are `{youaregay}%` gay",
            color = 0x202225
        )
        await interaction.followup.send(embed = em)

def setup(bot):
    bot.add_cog(howgay(bot))