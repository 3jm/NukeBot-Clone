import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    testing_guild_id = 1017999660603944960

    @nextcord.slash_command(guild_ids=[testing_guild_id], description="	Ban a specified user")
    async def kick(self, interaction: Interaction, reason, member: nextcord.Member = SlashOption(name="member", description="Mention a user", required=True)):
        if interaction.user.guild_permissions.kick_members:
            await interaction.response.defer()
            await member.kick(reason=reason)
            em = nextcord.Embed(
                description = f"{member.mention} has been kicked for `{reason}`.",
                color = 0x202225
            )
            await interaction.followup.send(embed = em)
        else:
            await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)


def setup(bot):
    bot.add_cog(kick(bot))