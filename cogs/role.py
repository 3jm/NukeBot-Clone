import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, ButtonStyle
from nextcord.ui import Button, View

class role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    testing_guild_id = 1017999660603944960

    @nextcord.slash_command(guild_ids=[testing_guild_id], description="Give a role to a specified user")
    async def role(self, interaction: Interaction, role: nextcord.Role = SlashOption(name="role", description="Select a role", required=True), member: nextcord.Member = SlashOption(name="member", description="Mention a user", required=True)):
        if interaction.user.guild_permissions.manage_roles:
            if role in member.roles:
                async def button_callback(interaction: Interaction):
                    await interaction.response.defer()
                    await member.remove_roles(role)
                    em = nextcord.Embed(
                        description = f"{member.mention} has been removed from {role.mention}.",
                        color = 0x202225
                    )
                    await interaction.followup.send(embed = em, ephemeral=True)

                button = Button(style=ButtonStyle.red, label="Remove")
                button.callback = button_callback
                view = View()
                view.add_item(button)
                await interaction.response.send_message(f"{member.mention} already has the role {role.mention}.", view=view, ephemeral=True)
            else:
                await member.add_roles(role)
                em = nextcord.Embed(
                    description = f"{member.mention} has been given the role {role.mention}.",
                    color = 0x202225
                )
                await interaction.response.send_message(embed = em)
        else:
            await interaction.response.send_message("You don't have permission to use this command.")

    @role.error
    async def role_error(self, ctx, error):
        if isinstance(error, nextcord.errors.Forbidden):
            await ctx.send("I don't have permission to give that role.")

def setup(bot):
    bot.add_cog(role(bot))