import nextcord, json, cooldowns
from nextcord.ext import commands
from nextcord import Interaction, ButtonStyle
from nextcord.ui import Button, View
from cooldowns import CooldownBucket
from cooldowns import CallableOnCooldown

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
            self.view.stop()
            await interaction.response.send_message(embed = em, ephemeral=True)
            try:
                new_channel = await interaction.channel.clone()
                await interaction.channel.delete()
                await new_channel.edit(position=interaction.channel.position)
                await new_channel.send("This channel has been nuked.\nhttps://d3kxs6kpbh59hp.cloudfront.net/community/COMMUNITY/3ae0064c555042218c2a6d36afaa4a21/02d61729ea234503a70bc812639fdaa3_1629821918.gif")
            except Exception as e:
                await interaction.followup.send("I am not allowed to nuke this type of channel. Reverting changes.\n\nPossible reasons why I cannot nuke this channel:\n• It is a **community updates** channel\n• It is a **community rules** channel", ephemeral=True)
                await new_channel.delete()

class nuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    testing_guild_id = 1017999660603944960

    @nextcord.slash_command(guild_ids=[testing_guild_id], description="Nuke a specified channel")
    @cooldowns.cooldown(1,15, bucket=cooldowns.SlashBucket.author)
    async def nuke(self, interaction: Interaction):
        if interaction.user.guild_permissions.manage_channels:
            if interaction.channel.type == nextcord.ChannelType.news:
                await interaction.response.send_message("You can't nuke a announcement channel.", ephemeral=True)

            await interaction.response.defer()
            view = View()
            view.add_item(Confirm(interaction.user.id))
            view.add_item(nukeButton(interaction.user.id))

            async def on_timeout(self):
                for item in view.children:
                    item.disabled = True

            em = nextcord.Embed(
                description="Are you sure you want to nuke this channel?\nThis will affect your servers activity progress.",
                color=0xFFFF00
            )
            await interaction.followup.send(embed=em, view=view)
        else:
            await interaction.response.send_message("You are lacking the `MANAGE_CHANNELS` permission.", ephemeral=True)

    @nuke.error
    async def nuke_error(self, interaction: Interaction, error):
        if isinstance(error, CallableOnCooldown):
            await interaction.response.send_message(f"You are on cooldown for {error.retry_after} seconds.", ephemeral=True)


def setup(bot):
    bot.add_cog(nuke(bot))