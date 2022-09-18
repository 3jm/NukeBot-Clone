import nextcord, random, datetime
from datetime import timedelta
from nextcord.ext import commands
from nextcord import Interaction

class testmyluck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    testing_guild_id = 1017999660603944960

    yourluck = [1, 2]

    @nextcord.slash_command(guild_ids=[testing_guild_id], description="Test your luck")
    async def testmyluck(self, interaction: Interaction):
        await interaction.response.defer()
        if random.choice(self.yourluck) == 1:
            await interaction.followup.send(f"{interaction.user.mention} You got lucky and got away.. *for now*")
        else:
            if interaction.user.guild_permissions.manage_guild:
                await interaction.followup.send(f"{interaction.user.mention} Wasn't so lucky but got away with it because they are staff. smh...")
            else:
                await interaction.user.edit(timeout=datetime.timedelta(seconds=604800))
                await interaction.followup.send(f"{interaction.user.mention} Wasn't so lucky and got timed out for **1 Week**. LOL")

    @testmyluck.error
    async def ttestmyluck_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I am missing required permissions to do this. Please give me the `Timeout Members` permission.")

def setup(bot):
    bot.add_cog(testmyluck(bot))