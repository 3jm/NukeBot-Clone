import logging as log
import nextcord, requests, json, os, time, asyncio, aiohttp, colorama, random, sys, pymongo, base64
from platform import python_version
from nextcord.ext import commands, tasks
from nextcord import Interaction, SlashOption, ButtonStyle, Webhook, Member
from nextcord.abc import GuildChannel
from nextcord.ui import Button, View, Select
from aiohttp import request
from aiohttp import ClientSession
from colorama import Fore, Back, Style
from captcha.image import ImageCaptcha
from pymongo import MongoClient

class dontasktoask(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    testing_guild_id = 1017999660603944960

    @nextcord.slash_command(guild_ids=[testing_guild_id], description="Advices to not ask to ask but to ask instead")
    async def dontasktoask(self, interaction: Interaction, user: nextcord.Member = SlashOption(name="user", description="The user to ping", required=False)):
        await interaction.response.defer()
        if user is None:
            await interaction.followup.send("https://dontasktoask.com/")
        else:
            await interaction.followup.send(f"{user.mention} https://dontasktoask.com/")

def setup(bot):
    bot.add_cog(dontasktoask(bot))