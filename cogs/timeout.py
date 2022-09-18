import nextcord, datetime
from datetime import timedelta
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    testing_guild_id = 1017999660603944960

    timeoptions = [
        "60 Seconds",
        "5 Minutes",
        "10 Minutes",
        "1 Hour",
        "1 Day",
        "1 Week"
    ]

    # create a command that will timeout a user
    @nextcord.slash_command(guild_ids=[testing_guild_id], description="Timeout a specified user")
    # have the user specify the person, the time and reason
    async def timeout(self, interaction: Interaction, member: nextcord.Member = SlashOption(name="member", description="Mention a user", required=True), time: str = SlashOption(name="time", description="The time to timeout the user for", required=True, choices=timeoptions), reason: str = SlashOption(name="reason", description="The reason for the timeout", required=True)):
        if interaction.user.guild_permissions.manage_messages:
            if member == self.bot.user:
                await interaction.response.send_message("You cannot timeout the bot.", ephemeral=True)
                return
            if member.guild_permissions.manage_messages:
                await interaction.response.send_message("You cannot timeout a staff member.", ephemeral=True)
                return
            if member.guild_permissions.administrator:
                await interaction.response.send_message("You cannot timeout an admin.", ephemeral=True)
                return

            await interaction.response.defer()

            if time == "60 Seconds":
                newtime = 60
            elif time == "5 Minutes":
                newtime = 300
            elif newtime == "10 Minutes":
                newtime = 600
            elif newtime == "1 Hour":
                newtime = 3600
            elif newtime == "1 Day":
                newtime = 86400
            elif newtime == "1 Week":
                newtime = 604800

            await member.edit(timeout=datetime.timedelta(seconds=newtime), reason=reason)
            em = nextcord.Embed(
                description = f"{member.mention} has been timed out for `{reason}` for `{time}`.",
                color = 0x202225
            )
            await interaction.followup.send(embed = em)
        else:
            await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)

    @nextcord.slash_command(guild_ids=[testing_guild_id], description="Untimeout a specified user")
    async def untimeout(self, interaction: Interaction, member: nextcord.Member = SlashOption(name="member", description="Mention a user", required=True)):
        if interaction.user.guild_permissions.manage_messages:
            await interaction.response.defer()
            await member.edit(timeout=None)
            em = nextcord.Embed(
                description = f"{member.mention} has been untimedout.",
                color = 0x202225
            )
            await interaction.followup.send(embed = em)
        else:
            await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)

    @timeout.error
    async def timeout_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I don't have permission to timeout users.")

    @untimeout.error
    async def untimeout_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I don't have permission to untimeout users.")

def setup(bot):
    bot.add_cog(timeout(bot))