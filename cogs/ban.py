import logging as log
import nextcord, requests, json, os, time, asyncio, aiohttp, colorama, random, sys, pymongo, base64
from platform import python_version
from nextcord.ext import commands, tasks, application_checks
from nextcord import Interaction, SlashOption, ButtonStyle, Webhook, Member
from nextcord.abc import GuildChannel
from nextcord.ui import Button, View, Select
from aiohttp import request
from aiohttp import ClientSession
from colorama import Fore, Back, Style
from captcha.image import ImageCaptcha
from pymongo import MongoClient

class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    testing_guild_id = 1017999660603944960

    @nextcord.slash_command(guild_ids=[testing_guild_id], description="	Ban a specified user")
    @application_checks.has_permissions(ban_members=True)
    async def ban(self, interaction: Interaction, reason, member: nextcord.Member = SlashOption(name="member", description="Mention a user", required=True)):
        await interaction.response.defer()
        try:
            await member.ban(reason=reason)
            em = nextcord.Embed(
                description = f"{member.mention} has been banned for `{reason}`.",
                color = 0x202225
            )
            await interaction.followup.send(embed = em)
        except:
            em = nextcord.Embed(
                description = f"You do not have the `Ban users` permission (or) `Administrator`.",
                color = 0x202225
            )
            await interaction.followup.send(embed = em)


def setup(bot):
    bot.add_cog(ban(bot))