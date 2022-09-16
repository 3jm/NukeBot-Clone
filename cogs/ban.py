import nextcord
from nextcord.ext import commands, application_checks
from nextcord import Interaction, SlashOption

class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    testing_guild_id = 1017999660603944960

    @nextcord.slash_command(guild_ids=[testing_guild_id], description="	Ban a specified user")
    @application_checks.has_permissions(ban_members=True)
    async def ban(self, interaction: Interaction, reason, member: nextcord.Member = SlashOption(name="member", description="Mention a user", required=True)):
        await interaction.response.defer()
        if interaction.user.guild_permissions.ban_members:
            await member.ban(reason=reason)
            em = nextcord.Embed(
                description = f"{member.mention} has been banned for `{reason}`.",
                color = 0x202225
            )
            await interaction.followup.send(embed = em)
        else:
            em = nextcord.Embed(
                description = "You don't have permission to use this command.",
                color = 0xF6548D
            )
            await interaction.followup.send(embed = em)


def setup(bot):
    bot.add_cog(ban(bot))