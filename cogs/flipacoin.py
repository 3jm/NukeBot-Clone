import nextcord, asyncio, random
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class flipacoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    testing_guild_id = 1017999660603944960

    @nextcord.slash_command(guild_ids=[testing_guild_id], description="Flip a coin")
    async def flipacoin(self, interaction: Interaction, call: str = SlashOption(name="call", choices=["Heads", "Tails"], description="Heads or tails?", required=True)):
        await interaction.response.defer()
        coin = random.choice(["heads", "tails"])
        em = nextcord.Embed(
            description = f"You called **{call}**, Flipping coin...",
            color = 0x202225
        )
        msg = await interaction.followup.send(embed = em)
        await asyncio.sleep(2)
        if coin == call.lower():
            em = nextcord.Embed(
                description = f"You called **{call}**, The coin landed on **{coin}**, You win!",
                color = 0x202225
            )
            await msg.edit(embed = em)
        else:
            em = nextcord.Embed(
                description = f"You called **{call}**, The coin landed on **{coin}**, You lose!",
                color = 0x202225
            )
            await msg.edit(embed = em)

def setup(bot):
    bot.add_cog(flipacoin(bot))