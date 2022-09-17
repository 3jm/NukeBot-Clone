import nextcord, datetime
from nextcord.ext import commands
from nextcord import Interaction

class about(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    testing_guild_id = 1017999660603944960

    start_time = datetime.datetime.now()

    @nextcord.slash_command(guild_ids=[testing_guild_id], description="Displays informations about the bot")
    async def about(self, interaction: Interaction):
        # get the uptime
        current_time = datetime.datetime.now()
        difference = current_time - self.start_time
        uptime = str(difference).split(".")[0]
        await interaction.response.defer(ephemeral=True)
        em = nextcord.Embed(
            title = "__About__",
            description = f"Current server's premium status: true\n**Owner**: Blind#6637\n**Servercount**: {len(self.bot.guilds)}\n**Users**: {len(set(self.bot.get_all_members()))}\n**Shards**: {self.bot.shard_count}\n**Created**: 9/15/2022\n**Language**: Python\n**API**: [Nextcord v2.2.0](https://docs.nextcord.dev/en/stable/)\n**Uptime**: {uptime}",
            color = 0x202225
        )
        em.set_thumbnail(url=f'{self.bot.user.avatar.url}')
        await interaction.followup.send(embed = em, ephemeral=True)

def setup(bot):
    bot.add_cog(about(bot))