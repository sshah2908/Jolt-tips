from discord import *
from discord import Embed as E 
import discord
from discord.ext import commands
import os

import asyncio
import random
import json
import requests
from requests import *
from discord.utils import get as g
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
#privk = os.environ['privkey']
#signed_txn = w3.eth.account.sign_transaction(dict(
#    nonce=w3.eth.get_transaction_count#('0xB6a2255f10F9018c4D444DEa9AC638E39fC473Fe'),
#    chainId=56,
#    gasPrice= w3.toWei('5', 'gwei'),
#    gas=70000,
#    to='0x73F170420F4400B6B7eC2Bc74bc71b3b2b51ab4D',
#    value=1000000000000000,
#    data=b'',
#  ),
#  privk,
#)
#hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
#print(hash.hex())
admins = [809456156149284884, 851224281752666123]
ABI = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
user_used = []
wrong = ":x:"
client = discord.Client
check = ":white_check_mark:"
bnb = "<:bnb:872528674119909417>"
BinanceUSD = "<:busd:899376406847430726>"
capt = "<:capt:872530205938442300>"
ShibaInu = "<:Shiba:899381818191675412>"
jolt = "<:jolt:898906673228443648>"
joltclassic = "<:joltclassic:896925976762650634>"
wallet_logo = "<:wallet:870769069274562591>"
globeToken = '<:GLB:902882424072048660>'
KitsuneToken = '<:kitsunetoken:906985153002369054>'
MorphineToken = "<:Morphine:926173196166778940>"
withdraw = "<:outbox_tray:>"
currencies = ['jlt','bnb','capt', 'jolt', 'joltclassic', 'jlc', 'busd', 'shiba', 'kitsune', 'glb', 'eth', 'matic', 'nano', 'st', 'slicktoken', 'btc', 'bitcoin', 'sina', 'jetoken', 'jet', "morphine", "mrp"]
blue = Color.blue()
red = Color.red() 
green = Color.green()
page_1_tokens = embed=E(title=f"Tokens Listed", description=f"Jolt Token\n{jolt} Jolt contract ```0xac19e03d269811a2d837109ff6582da1a4016e9d```\nCaptian Token\n{capt} Captian contract: ```0xdf5301b96ceccb9c2a61505b3a7577111056a4c5```\nBinance Token\n{bnb} BNB contract: ```0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c```\nJolt classic Token\n{joltclassic} Jolt Classic contract: ```0x59b31ab138f895330337d7fb41ed0d79ae8763e0```", color=blue) # 4 tokens on each 
# ---- 
page_2_tokens = embed=E(title=f"Tokens Listed", description=f"Binance USD Token\n{BinanceUSD} Binance USD contract: ```0xe9e7cea3dedca5984780bafc599bd69add087d56```\nShiba Inu\n{ShibaInu} Shiba Inu contract: ```0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce```\nKitsune Token\n{KitsuneToken} Kitsune contract: ```0x66aFC53B499701f963548A578F990e3c528e2048```\nGlobe token\n{globeToken} Globe contract: ```0xf46b841f9367f5ff559c8670617129452607e722```", color=blue)
client.token_pages = [page_1_tokens, page_2_tokens]



class Utils(commands.Cog):
  def __init__(self, client):
    self.client = client
    client=client


  @commands.command()
  async def team(self, ctx):
    embed = E(title=f"Jolt Wallet Team", description=f"**Lead Developer**: Cryptic#1000\n**Developers**: baby chrome#6969, 8H_HY#5724, Gravved#0012\n**Administrators**: rq7#4992, mediscan#8414", color=blue)
    embed.set_footer(text="Join the support server here https://discord.gg/nCtGsxfrAu")
    await ctx.send(embed=embed)




  @commands.command()
  async def requesting(self, ctx, URL=None):
    if ctx.message.author.id not in admins:
      await ctx.send("Missing Permissions!")
      return
    if URL is None:
      await ctx.send("You must specify A URL to send a requests to!")
      return
    r = requests.get(URL)
    await ctx.send(r.text)

  @commands.command(aliases=["addbot"])
  async def invite(self, ctx):
    Embed = E(title=f"Jolt Wallet", description=f"To invite me to your discord server, click [here](https://discord.com/api/oauth2/authorize?client_id=869390064172552192&permissions=8&scope=bot)", color=blue)
  #  Embed = E(title=f"Jolt Wallet", description=f"You cannot invite me to your discord server yet as I am not released yet!", color=blue)
    await ctx.send(embed=Embed)


 


  @commands.command(aliases=['TOS'])
  async def terms(self, ctx):
    embed = E(title="Terms and conditions <a:rules:907741809915084801>", description="These are the Terms and conditions to Jolt Wallet(Bot)!! Please read them carefully!!\nBy using any command on the bot, you agree to follow our TOS! Failing to follow them can lead to your account being blacklisted.\n\n**We are never responsible for lost or stolen funds.** We reserve the right to deny you of a refund if your money goes missing.\n\n**Tips are non-reversible and non-refundable.**\nIf you make an accidental tip, in no way can the Jolt team reverse that tip!\n\n**Fund security**\nYour balance's security is determined by the safety of your discord account.Never share your passoword with anyone! Enable 2FA to ensure full security.Your wallet is fully safe and tested on our side, we use the best technology to make your funds as safe as possible!\n\n**We reserve the right to blacklist your account**\nYour account is subject to blacklisting if you have scammed or taken part in suspicious activities. We can lock your account forever if needed.\n\n**Staff**\nJolt's staff are the finest and selected to give you a safe time. Their decisions are final. If you have a serious issue, contact any of the developers in the [support server](https://discord.gg/7QKXzJymZK)")
    await ctx.send(embed=embed)




  @commands.command(aliases = ['server','supportserver'])
  async def support(self, ctx):
    embed = E(title='Support server', description="Click [**me**](https://discord.gg/7QKXzJymZK) to join the support server!", color = blue)
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Utils(client))
  print("Utils Cog ready")