import nextcord
from nextcord.ext import commands
from nextcord import Interaction, ButtonStyle
from nextcord.ui import Button, View

class nukeButton(Button):
    def __init__(self, id):
        super().__init__(style=ButtonStyle.red, label="Cancel")
        self.id = id

    async def callback(self, interaction: Interaction):
        if interaction.user.id != self.id:
            em = nextcord.Embed(
                description = "You are **not** the author of this command.",
                color = 0xFFFF00
            )
            await interaction.response.send_message(embed = em, ephemeral=True)
        else:
            await interaction.message.delete()

class Confirm(Button):
    def __init__(self, id):
        super().__init__(style=ButtonStyle.green, label="Confirm")
        self.id = id

    async def callback(self, interaction: Interaction):
        if interaction.user.id != self.id:
            em = nextcord.Embed(
                description = "You are **not** the author of this command.",
                color = 0xFFFF00
            )
            await interaction.response.send_message(embed = em, ephemeral=True)
        else:
            em = nextcord.Embed(
                description = "Nuking channel...",
                color = 0x202225
            )
            await interaction.response.send_message(embed = em, ephemeral=True)
            new_channel = await interaction.channel.clone()
            await interaction.channel.delete()
            await new_channel.edit(position=interaction.channel.position)
            await new_channel.send("This channel has been nuked.")

class nuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    testing_guild_id = 1017999660603944960

    @nextcord.slash_command(guild_ids=[testing_guild_id], description="Nuke a specified channel")
    @commands.has_permissions(manage_channels=True)
    async def nuke(self, interaction: Interaction):
        await interaction.response.defer()
        view = View()
        view.add_item(Confirm(interaction.user.id))
        view.add_item(nukeButton(interaction.user.id))
        em = nextcord.Embed(
            description="Are you sure you want to nuke this channel?\nThis will affect your servers activity progress.",
            color=0xFFFF00
        )
        await interaction.followup.send(embed=em, view=view)


def setup(bot):
    bot.add_cog(nuke(bot))
