#© Copyright Notice All rights reserved Cryptic 2021-2024


from discord import *
from webserver import keep_alive
import decimal
from discord import Embed as E 
import discord
from discord.ext import commands
import os
from replit import db
import re
import typing
import psutil
import sys
from datetime import datetime
import time 
from discord.ext import tasks
import platform
import logging
import discord
import requests
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
#    to='0xD0c08922adEDE10ff42dE72686DEf62c298708c8',
#    value=1000000000000000,
#    data=b'',
#  ),
#  privk,
#)
#hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
#print(hash.hex())
intents = discord.Intents().all()
pending_trxs = 0
admins = [809456156149284884,851224281752666123, 690678234165149706, 919225654912892978]
my_secret = os.environ['bottoken']
ABI = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'

def opentipstats():
  with open("dbs/tipstatssent.json") as f:
    tip_stats_sent = json.load(f)
  return tip_stats_sent
def savetipstats(tipstats):
  with open("dbs/tipstatssent.json", "w+") as f:
    json.dump(tipstats, f)
def opentipstatsre():
  with open("dbs/tipstatsre.json") as f:
    tip_stats_re = json.load(f)
  return tip_stats_re
def savetipstatsre(tip_stats_re):
  with open("dbs/tipstatsre.json", "w+") as f:
    json.dump(tip_stats_re, f)
def openpromo():
  with open(f"dbs/promo.json") as f:
    opromo = json.load(f)
  return opromo
def savepromo(opromo):
  with open (f"dbs/promo.json", "w+") as f:
    json.dump(opromo, f)
def opencodes():
  with open("dbs/Linkcodes.json") as f:
    codes = json.load(f)
  return codes
def savecodes(codes):
  with open (f"dbs/Linkcodes.json") as f:
    json.dump(codes, f)

def openpacks():
  with open (f"dbs/packs.json") as f:
    opacks = json.load(f) 
  return opacks
def savepacks(opacks):
  with open (f"dbs/packs.json", "w+") as f:
    json.dump(opacks, f)
def opencollection():
  with open (f"dbs/collection.json") as f:
    ocollection = json.load(f) 
  return ocollection
def savecollection(ocollection):
  with open (f"dbs/collection.json", "w+") as f:
    json.dump(ocollection, f)
def openblacklist():
  with open (f"dbs/blacklist.json") as f:
    inventory = json.load(f)
  return inventory
def saveblacklist(inventory):
  with open(f"dbs/blacklist.json", "w+") as f:
    json.dump(inventory, f)

#shall i get rid of cogs den? k wait
def openkillbot():
  with open (f"dbs/killbot.json") as f:
    inventory = json.load(f)
  return inventory
def savekillbot(inventory):
  with open(f"dbs/killbot.json", "w+") as f:
    json.dump(inventory, f)

def openstore():
  with open (f"dbs/store.json") as f:
    store = json.load(f)
  return store
def savestore(store):
  with open(f"dbs/store.json", "w+") as f:
    json.dump(store, f)

def opendb(): #Open db
  with open(f"dbs/inventory.json") as f:
    inventory = json.load(f)
  return inventory

def savedb(inventory): #Save db changes
  with open(f"dbs/inventory.json", "w+") as f:
    json.dump(inventory, f)

def openwhitelist(): #Open db
  with open(f"dbs/whitelistedbots.json") as f:
    whitelist = json.load(f)
  return whitelist

def savewhitelist(whitelist): #Save db changes
  with open(f"dbs/whitelistedbots.json", "w+") as f:
    json.dump(whitelist, f)
user_used = []
#step 1 put the price of the token here! If this token is not listed on coingecko just make a variable with the amount!
bnbURL = "https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=usd"  
captURL = "https://api.coingecko.com/api/v3/simple/price?ids=captain&vs_currencies=usd"
busdURL = "https://api.coingecko.com/api/v3/simple/price?ids=busd&vs_currencies=usd"
shibaURL = "https://api.coingecko.com/api/v3/simple/price?ids=shiba-inu&vs_currencies=usd"
ethURL = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'
maticURL = 'https://api.coingecko.com/api/v3/simple/price?ids=matic-network&vs_currencies=usd'
globeURL = 'https://api.coinpaprika.com/v1/ticker/glb-globe-token'
bitcoinURL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
nanoURL = 'https://api.coingecko.com/api/v3/simple/price?ids=nano&vs_currencies=usd'
litecoinURl = 'https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd'
eosURL = 'https://api.coingecko.com/api/v3/simple/price?ids=eos&vs_currencies=usd'
xdaiURL = 'https://api.coingecko.com/api/v3/simple/price?ids=xdai&vs_currencies=usd'
dashURL = 'https://api.coingecko.com/api/v3/simple/price?ids=dash&vs_currencies=usd'
slickURL = "https://api.coinpaprika.com/v1/ticker/st-slicktoken"
jetokenURL = "https://api.coingecko.com/api/v3/simple/price?ids=jetoken&vs_currencies=usd"
#--------------------------
nasaURL = "https://api.nasa.gov/planetary/apod?api_key=oJ6ESoeSJFyn9Bdf4gURYFjGjkJiqhz8zghBElDo"
nasa_location = "https://api.nasa.gov/planetary/earth/imagery?lon=-95.33&lat=29.98&date=2018-01-01&dim=0.15&api_key=oJ6ESoeSJFyn9Bdf4gURYFjGjkJiqhz8zghBElDo"

Nasa_stats = requests.get(nasaURL)
json_nasa_stats = Nasa_stats.json()
daily_pic_nasa = json_nasa_stats["url"]
stats_capt = requests.get(captURL)
json_stats_capt = stats_capt.json()
captPrice = float(json_stats_capt["captain"]["usd"])
stats_bnb = requests.get(bnbURL)
json_stats_bnb = stats_bnb.json()
bnbPrice = float(json_stats_bnb["binancecoin"]["usd"])
stats_busd = requests.get(busdURL)
json_stats_busd = stats_busd.json()
busdPrice = float(json_stats_busd["busd"]["usd"])
stats_jetoken = requests.get(jetokenURL)
json_stats_jetoken = stats_jetoken.json()
jetokenPrice = float(json_stats_jetoken["jetoken"]["usd"])
stats_shiba = requests.get(shibaURL)
json_stats_shiba = stats_shiba.json()
shibaPrice = float(json_stats_shiba["shiba-inu"]["usd"])
stats_eth = requests.get(ethURL)
json_stats_eth = stats_eth.json()
ethPrice = float(json_stats_eth["ethereum"]["usd"])
stats_matic = requests.get(maticURL)
json_stats_matic = stats_matic.json()
maticPrice = float(json_stats_matic["matic-network"]["usd"])
stats_globe = requests.get(globeURL)
json_stats_globe = stats_globe.json()
try:
  glbPrice = float(json_stats_globe["price_usd"])
except:
  glbPrice = 0.0000450379
stats_slick = requests.get(slickURL)
json_stats_slick = stats_slick.json()
try:
  stPrice = float(json_stats_slick["price_usd"])
except:
  stPrice = 0.00215
  pass
stats_bitcoin = requests.get(bitcoinURL)
json_stats_bitcoin = stats_bitcoin.json()
bitcoinPrice = float(json_stats_bitcoin["bitcoin"]["usd"])
stats_nano = requests.get(nanoURL)
json_stats_nano = stats_nano.json()
nanoPrice = float(json_stats_nano["nano"]["usd"])
stats_litecoin = requests.get(litecoinURl)
json_stats_litecoin = stats_litecoin.json()
ltcPrice = float(json_stats_litecoin["litecoin"]["usd"])
stats_eos = requests.get(eosURL)
json_stats_eos = stats_eos.json()
eosPrice = float(json_stats_eos["eos"]["usd"])
stats_xdai = requests.get(xdaiURL)
json_stats_xdai = stats_xdai.json()
xdaiPrice = float(json_stats_xdai["xdai"]["usd"])
stats_dash = requests.get(dashURL)
json_stats_dash = stats_dash.json()
dashPrice = float(json_stats_dash["dash"]["usd"])
stPrice = 0.00215
jltPrice = 0.00000000000171352
jlcPrice = 0.000411820
sinaPrice = 0.00104823
morphinePrice = 0.0180927

TRX_lock = False
def get_prefix(client, message): ##first we define get_prefix
    with open('dbs/prefixes.json', 'r') as f: ##we open and read the prefixes.json, assuming it's in the same file
        prefixes = json.load(f) #load the json as prefixes
    if isinstance(message.channel, discord.channel.DMChannel):
       return "."
    else:
      return prefixes[str(message.guild.id)]
prefix = '.'
class Client(commands.Bot):
  def __init__(self):
    super().__init__(command_prefix=(get_prefix),case_insensitive=True, intents=intents)
client=Client() 
# step 2 Add emoji here (make sure bot is in the server that has the emoji!)
wrong = "❌"
check = "✅"
animatedx = '<a:x_:909099008570568704>'
bnb = "<:BNB:901427365652078593>"
capt = "<:capt:909021032587862019>"
ShibaInu = "<:Shiba:901427958193987604>"
captcontract = "0xdf5301b96ceccb9c2a61505b3a7577111056a4c5"
joltcontract = "0xac19e03d269811a2d837109ff6582da1a4016e9d"
joltclassiccontract = "0x59b31ab138f895330337d7fb41ed0d79ae8763e0"
bnbcontract = "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"
busdcontract = "0xe9e7cea3dedca5984780bafc599bd69add087d56"
shibainucontract = "0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce"
kitsunecontract = "0x66aFC53B499701f963548A578F990e3c528e2048"
globecontract = "0xf46b841f9367f5ff559c8670617129452607e722"
jetokencontract = "0x0f005dfe97c5041e538b7075915b2ee706677c26"
morphinecontract = "0xb8608f270497764a10c28bfe75454f68b31ba2b1"

jolt = "<:Jolt:901432195690954842>"
BinanceUSD = "<:BUSD:901427439597658123>"
joltclassic = "<:joltclassic:901427719114485821>"
wallet_logo = "<:wallet:870769069274562591>"
KitsuneToken = '<:kitsunetoken:906985153002369054>'
globeToken = '<:GLB:902882424072048660>'
ethToken = '<:ETH:901432745648091176>'
st = '<:ST:912438336344453130>'
btc = '<:BTC:901432737859239936>'
MorphineToken = "<:Morphine:926173196166778940>"
jetokenToken = '<:jetoken:920064270262222878>'
dragon = '🐉'
nano = '<:nano:919755954826911825>'
Polygon = '<:MATIC:909479683815530506>'
withdraw = "<:outbox_tray:>"
warning = "<:warning:>"
loading = "<a:loading:905550477511503892>"
JoltPack = "<:joltpack:905970655185481769>"
moderator = ['820022196629012481', '513311255021223957']
currencies = ['jlt','bnb','capt', 'jolt', 'joltclassic', 'jlc', 'busd', 'shiba', 'kitsune', 'glb', 'eth', 'matic', 'nano', 'st', 'slicktoken', 'btc', 'bitcoin', 'sina', 'jetoken', 'jet', "morphine", "mrp"]
mod = '<:moderator:861547951192408064>'
bombreaction = '💣'
rureaction = '🇷🇺'
@client.event
async def on_message(message):
  whitelist=openwhitelist()
  prefix = get_prefix(client, message)
  if message.content.startswith(prefix):
    ID = str(message.author.id)
    if message.author.bot:
      if ID not in whitelist:
        return
      else:
        ctx = await client.get_context(message)
        await client.invoke(ctx)
    else:
      ctx = await client.get_context(message)
      await client.invoke(ctx)
  elif client.user.mentioned_in(message) and message.mention_everyone is False:
        with open('dbs/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefix = prefixes[str(message.guild.id)]
        guild = message.guild
        embed = Embed(
            title=f"Prefix",
            description=
            f"My prefix for **{guild}** is **{prefix}**",
            color=green)
        await message.channel.send(embed=embed)
  else:
    pass


@client.command()
async def call(ctx):
  await ctx.send("Connecting to a server... Please wait.")
  await asyncio.sleep(1)
  servers = []
  for guild in client.guilds:
    servers.append((guild.id))
  rand_idx = int(random.random() * len(servers))
  random_server = servers[rand_idx]
  random_server = int(random_server)
  while random_server == ctx.guild.id:
    rand_idx = int(random.random() * len(servers))
    random_server = servers[rand_idx]
  guild = client.get_guild(random_server)
  check = False
  for channel in guild.channels:
    if channel.name == "phone":
      messages1 = 0
      await channel.send(f"Connected to {ctx.guild}!\nYou only have 20 messages before your session ends!")  
      await ctx.send(f"Connected to {guild}!!\nYou only have 20 messages before your session ends!")
      check = True
      while messages1 < 20:
          def check(m):
            return  m.channel == channel or ctx.channel
          msg = await client.wait_for("message", check=check)
          if msg.channel == ctx.channel:
            await channel.send(msg.content)
          else:
            await ctx.send(msg.content)
          messages1 += 1
    else:
      pass

  while check == False:
    rand_idx = int(random.random() * len(servers))
    random_server = servers[rand_idx]
    random_server = int(random_server)
    while random_server == ctx.guild.id:
      rand_idx = int(random.random() * len(servers))
      random_server = servers[rand_idx]
    guild = client.get_guild(random_server)
    for channel in guild.channels:
      if channel.name == "phone":
        messages1 = 0
        await channel.send(f"Connected to {ctx.guild}!\nYou only have 20 messages before your session ends!")  
        await ctx.send(f"Connected to {guild}!!\nYou only have 20 messages before your session ends!")
        check = True
        while messages1 < 20:
          def check(m):
            return  m.channel == channel or ctx.channel
          msg = await client.wait_for("message", check=check)
          if msg.channel == ctx.channel:
            await channel.send(msg.content)
          else:
            await ctx.send(msg.content)
          messages1 += 1
      else:
        pass
@client.event
async def on_guild_join(guild): #when the@client joins the guild
    embed=discord.Embed(title="<:joltclassic:896925976762650634>**========*Thanks For Adding Me!* ========**<:joltclassic:896925976762650634>", description=f"Thanks for adding me to {guild.name}\n\nUse the **.help** command to get started!", color=blue)
    try:
      await guild.text_channels[7].send(embed=embed)
    except:
      await guild.text_channels[1].send(embed=embed)
    with open('dbs/prefixes.json', 'r') as f: #read the prefix.json file
        prefixes = json.load(f) #load the json file

    prefixes[str(guild.id)] = '.'#default prefix

    with open('dbs/prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
        json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater

@client.event
async def on_guild_remove(guild): #when the@client is removed from the guild
    with open('dbs/prefixes.json', 'r') as f: #read the file
        prefixes = json.load(f)

    prefixes.pop(str(guild.id)) #find the guild.id that@client was removed from

    with open('dbs/prefixes.json', 'w') as f: #deletes the guild.id as well as its prefix
        json.dump(prefixes, f, indent=4)


@client.command()
async def addbug(ctx):
  with open('dbs/bugs.json', 'r') as f: #read the file
      bugs = json.load(f)
  if ctx.author.id in admins:
    channel = client.get_channel(925746965365526588)
    bugs["869390064172552192"] += 1
    with open('dbs/bugs.json', 'w') as f: 
        json.dump(bugs, f)
    bugss = bugs["869390064172552192"]
    channel2 = str(bugss)
    await channel.edit(name = channel2)
    await ctx.send(f"Added 1 bug caught by users!\nTotal: {bugs}")
  else:
    await ctx.send("You cannot use this command!")
@client.command(pass_context=True)
@commands.has_permissions(administrator=True) #ensure that only administrators can use this command
async def changeprefix(ctx, prefix):
    with open('dbs/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('dbs/prefixes.json', 'w') as f: #writes the new prefix into the .json
        json.dump(prefixes, f, indent=4)
    embed = Embed(
        title=f"Prefix",
        description=
        f"Successfully changed {ctx.guild}'s prefix to **{prefix}**",
        color=green)
    await ctx.send(embed=embed)




@client.command()
async def whitelist(ctx, ID:str):
  if ctx.author.id not in admins:
    return
  else:
    whitelist=openwhitelist()
    if ID not in whitelist:
      whitelist[ID] = {}
      savewhitelist(whitelist)
      await ctx.send(f"Added <@{ID}> as a whitelisted bot!")
    else:
      await ctx.send(f"{ID} Is already a whitelisted bot!")
blue = Color.blue()
red = Color.red() 
green = Color.green()
depositlogschannel = client.get_channel(905190880850358333)
withdrawlogschannel = client.get_channel(906681382225448982)
TRX_lock = False
def getliveprices():
  global captPrice
  global bnbPrice
  global busdPrice
  global shibaPrice
  global ethPrice
  global maticPrice
  global glbPrice
  global stPrice
  global bitcoinPrice
  global nanoPrice
  global ltcPrice
  global eosPrice
  global xdaiPrice
  global dashPrice
  global jetokenPrice
  global morphinePrice
  # CaPzJ4AvP3FyqQdlv9TnQ5lsxXXSpsrY1CQUyuXDC4wBVX3WotvNm4U6DktdMNTH

  headers = {
    'x-api-key': "CaPzJ4AvP3FyqQdlv9TnQ5lsxXXSpsrY1CQUyuXDC4wBVX3WotvNm4U6DktdMNTH"
  }
  try:
    bsc = f"https://deep-index.moralis.io/api/v2/erc20/{captcontract}/price?chain=bsc"
    response = requests.request("GET", bsc, headers=headers)
    resp = response.json()
    captPrice = resp["usdPrice"]
  except:
    pass
  try:
    bsc = f"https://deep-index.moralis.io/api/v2/erc20/{bnbcontract}/price?chain=bsc"
    response = requests.request("GET", bsc, headers=headers)
    resp = response.json()
    bnbPrice = resp["usdPrice"]
  except:
    pass
  try:
    bsc = f"https://deep-index.moralis.io/api/v2/erc20/{busdcontract}/price?chain=bsc"
    response = requests.request("GET", bsc, headers=headers)
    resp = response.json()
    busdPrice = resp["usdPrice"]
  except:
    pass
  try:
    bsc = f"https://deep-index.moralis.io/api/v2/erc20/{shibainucontract}/price?chain=bsc"
    response = requests.request("GET", bsc, headers=headers)
    resp = response.json()
    shibaPrice = resp["usdPrice"]
  except:
    pass
  try:
    stats_eth = requests.get(ethURL)
    json_stats_eth = stats_eth.json()
    ethPrice = float(json_stats_eth["ethereum"]["usd"])
  except:
    pass
  try:
    stats_matic = requests.get(maticURL)
    json_stats_matic = stats_matic.json()
    maticPrice = float(json_stats_matic["matic-network"]["usd"])
  except:
    pass
  try:
    response = requests.request("GET", bsc, headers=headers)
    resp = response.json()
    glbPrice = resp["usdPrice"]
  except:
    pass
  try:
    stats_slick = requests.get(slickURL)
    json_stats_slick = stats_slick.json()
    stPrice = float(json_stats_slick["price_usd"])
  except:
    pass
  try:
    stats_bitcoin = requests.get(bitcoinURL)
    json_stats_bitcoin = stats_bitcoin.json()
    bitcoinPrice = float(json_stats_bitcoin["bitcoin"]["usd"])
  except:
    pass
  try:
    stats_nano = requests.get(nanoURL)
    json_stats_nano = stats_nano.json()
    nanoPrice = float(json_stats_nano["nano"]["usd"])
  except:
    pass
  try:
    stats_litecoin = requests.get(litecoinURl)
    json_stats_litecoin = stats_litecoin.json()
    ltcPrice = float(json_stats_litecoin["litecoin"]["usd"])
  except:
    pass
  try:
    stats_eos = requests.get(eosURL)
    json_stats_eos = stats_eos.json()
    eosPrice = float(json_stats_eos["eos"]["usd"])
  except:
    pass
  try:
    stats_xdai = requests.get(xdaiURL)
    json_stats_xdai = stats_xdai.json()
    xdaiPrice = float(json_stats_xdai["xdai"]["usd"])
  except:
    pass
  try:
    stats_dash = requests.get(dashURL)
    json_stats_dash = stats_dash.json()
    dashPrice = float(json_stats_dash["dash"]["usd"])
  except:
    pass
  try:
    bsc = f"https://deep-index.moralis.io/api/v2/erc20/{jetokencontract}/price?chain=bsc"
    response = requests.request("GET", bsc, headers=headers)
    resp = response.json()
    jetokenPrice = resp["usdPrice"]
  except:
    pass
  try:
    bsc = f"https://deep-index.moralis.io/api/v2/erc20/{morphinecontract}/price?chain=bsc"
    response = requests.request("GET", bsc, headers=headers)
    resp = response.json()
    morphinePrice = resp["usdPrice"]
  except:
    pass
  

def createaccount(ID):
  inventory = opendb()
  if ID not in inventory:
    inventory[ID] = {}
    inventory[ID]["bnb"] = {}
    inventory[ID]["bnb"]["emoji"] = bnb
    inventory[ID]["bnb"]["amt"] = 0.00
    inventory[ID]["bnb"]["name"] = "Binance Coin"
    inventory[ID]["bnb"]["symbol"] = "BNB"
    inventory[ID]["capt"] = {}
    inventory[ID]["capt"]["emoji"] = capt
    inventory[ID]["capt"]["amt"] = 0.00
    inventory[ID]["capt"]["name"] = "Captain Token"
    inventory[ID]["capt"]["symbol"] = "CAPT"
    inventory[ID]["jlt"] = {}
    inventory[ID]["jlt"]["emoji"] = jolt
    inventory[ID]["jlt"]["amt"] = 0.00
    inventory[ID]["jlt"]["name"] = "Jolt"
    inventory[ID]["jlt"]["symbol"] = "JLT"
    inventory[ID]["jlc"] = {}
    inventory[ID]["jlc"]["emoji"] = joltclassic
    inventory[ID]["jlc"]["amt"] = 0.00
    inventory[ID]["jlc"]["name"] = "Jolt Classic"
    inventory[ID]["jlc"]["symbol"] = "JLC"
    inventory[ID]["busd"] = {}
    inventory[ID]["busd"]["emoji"] = BinanceUSD
    inventory[ID]["busd"]["amt"] = 0.00
    inventory[ID]["busd"]["name"] = "Binance USD"
    inventory[ID]["busd"]["symbol"] = "BUSD"
    inventory[ID]["Shiba"] = {}
    inventory[ID]["Shiba"]["emoji"] = ShibaInu
    inventory[ID]["Shiba"]["amt"] = 0.00
    inventory[ID]["Shiba"]["name"] = "Shiba Inu"
    inventory[ID]["Shiba"]["symbol"] = "SHIB"
    inventory[ID]["sina"] = {}
    inventory[ID]["sina"]["emoji"] = KitsuneToken
    inventory[ID]["sina"]["amt"] = 0.00
    inventory[ID]["sina"]["name"] = "sina"
    inventory[ID]["sina"]["symbol"] = "KITSUNE"
    inventory[ID]["glb"] = {}
    inventory[ID]["glb"]["emoji"] = globeToken
    inventory[ID]["glb"]["amt"] = 0.00
    inventory[ID]["glb"]["name"] = "glb"
    inventory[ID]["glb"]["symbol"] = 'GLOBE'
    inventory[ID]["eth"] = {}
    inventory[ID]["eth"]["emoji"] = ethToken
    inventory[ID]["eth"]["amt"] = 0.00
    inventory[ID]["eth"]["name"] = "eth"
    inventory[ID]["eth"]["symbol"] = 'ethereum'
    inventory[ID]["matic"] = {}
    inventory[ID]["matic"]["emoji"] = Polygon
    inventory[ID]["matic"]["amt"] = 0.00
    inventory[ID]["matic"]["name"] = "Polygon"
    inventory[ID]["matic"]["symbol"] = "MATIC"
    inventory[ID]["nano"] = {}
    inventory[ID]["nano"]["emoji"] = nano
    inventory[ID]["nano"]["amt"] = 0.00
    inventory[ID]["nano"]["name"] = "Nano"
    inventory[ID]["nano"]["symbol"] = "nano"
    inventory[ID]["st"] = {}
    inventory[ID]["st"]["emoji"] = st
    inventory[ID]["st"]["amt"] = 0.00
    inventory[ID]["st"]["name"] = "SlickToken"
    inventory[ID]["st"]["symbol"] = "ST"
    inventory[ID]["btc"] = {}
    inventory[ID]["btc"]["emoji"] = btc
    inventory[ID]["btc"]["amt"] = 0.000000
    inventory[ID]["btc"]["name"] = "Bitcoin"
    inventory[ID]["btc"]["symbol"] = "BTC"
    inventory[ID]["jet"] = {}
    inventory[ID]["jet"]["emoji"] = jetokenToken
    inventory[ID]["jet"]["amt"] = 0.00
    inventory[ID]["jet"]["name"] = "Jetoken"
    inventory[ID]["jet"]["symbol"] = "JET"
    inventory[ID]["mrp"] = {}
    inventory[ID]["mrp"]["emoji"] = MorphineToken
    inventory[ID]["mrp"]["amt"] = 0.00
    inventory[ID]["mrp"]["name"] = "Morphine"
    inventory[ID]["mrp"]["symbol"] = "MRP"

    savedb(inventory)  
  coll = opencollection()
  if ID not in coll:
    coll[ID] = {}
    coll[ID]["pack"] = {}
    coll[ID]["pack"]["amt"] = 0
    savecollection(coll)
  tip_stats_re = opentipstatsre()
  if ID not in tip_stats_re:
    tip_stats_re[ID] = {}
    tip_stats_re[ID]["amt"] = 0.0
    savetipstatsre(tip_stats_re)
  


client.remove_command('help')

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    seconds = error.retry_after
    seconds_in_day = 60 * 60 * 24
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60

    days = seconds // seconds_in_day
    hours = (seconds - (days * seconds_in_day)) // seconds_in_hour
    minutes = (seconds - (days * seconds_in_day) -
               (hours * seconds_in_hour)) // seconds_in_minute
    stri = ""
    if days == 0.0 and seconds == 0:
      stri = f"{int(hours)} hours and {int(minutes)} minutes"
    elif days == 0.0 and hours == 0.0 and seconds == 0:
      stri = f"{int(minutes)} minutes"
    elif days == 0.0 and hours == 0.0 and minutes == 0:
      stri = f"{int(seconds)} seconds"
    else:
      stri = f"{int(days)} days, {int(hours)} hours and {int(minutes)} minutes"
    cd = Embed(
        title=f"Command On Cooldown!",
        description=
        f"This command is on cooldown, please try again in **{stri}**",
        color=discord.Color.red())
    cd.set_thumbnail(
        url=
        "https://media.tenor.com/images/9b5567482abeaf407fcd53c4d64f331c/tenor.gif"
    )
    await ctx.send(embed=cd)
  else:
    
    await ctx.send(embed=Embed(title=f"{wrong} Something went wrong!", description=f"Something went wrong!\nError: {error}", color=Color.red()))
    user_used.append(ctx.message.author)
    if ctx.message.author in user_used:
      pass
    else:
      faucet.reset_cooldown(ctx)

client.launch_time = datetime.utcnow()







@client.group()
async def report(ctx):
  if 'deposit' in ctx.message.content:
    return
  elif 'withdraw' in ctx.message.content:
    return
  else:
    Embed = E(title=f"Report help", description=f"{ctx.author.mention}, You must include what you want to report!!\nIt must be `.report deposit` or `.report withdraw`!!", color=red)
    await ctx.send(embed=Embed)

@report.command()
async def deposit(ctx):
  getliveprices()
  if isinstance(ctx.channel, discord.channel.DMChannel):
    Embed = E(title=f"Report Missing deposit!", description=f"{ctx.author.mention}, Please send the currency of the missing deposit!", color=blue)
    await ctx.send(embed=Embed)
    def check(m) -> bool:
      return m.author == ctx.author and m.channel == ctx.channel
    msg = await client.wait_for("message", check=check)
    if msg.content not in currencies:
      embed = E(title=f"{wrong} Error", description=f"The currency you entered is not a supported currency on the bot!", color=red)
      await ctx.send(embed=embed)
      return
    else:
      currency = msg.content
      embed = E(title=f"Explorer link.", description=f"Please send the Explorer link of {currency}\nNote:It **must** be a link or your report will be ignored!", color=blue)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author and m.channel == ctx.channel
      msg = await client.wait_for("message", check=check)
      explorer = msg.content
      embed = E(title=f"Additional comments", description=f"Do you have any additional comments for the developers? Please send them now.\nIf not, type **none**", color=blue)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author and m.channel == ctx.channel
      msg = await client.wait_for("message", check=check)
      embed = E(title=f"Report sent!", description=f"Your report has been sent!!\nDetails:Missing deposit\nCurrency:{currency}\n[Explorer link]({explorer})\nComments:{msg.content}", color=green)
      await ctx.send(embed=embed)
      dchannel = client.get_channel(909935939520983121)
      embed = E(title=f"Missing Transaction reported!!", description=f"User:{ctx.author}\nID:{ctx.author.id}\nDetails:Missing deposit\nCurrency:{currency}\n[Explorer link]({explorer})\nComments:{msg.content}", color=blue)
      await ctx.send("**Note: If you recive no reply from the bot by 2 days, your report was denyed!**")
      membed = await dchannel.send(embed=embed)
      await membed.add_reaction(emoji='✅')
      await asyncio.sleep(1)
      def check(reaction, user):
        return str(reaction) == ('✅')
      await client.wait_for("reaction_add", check=check)
      await ctx.send("Your report for your missing deposit report has been accepted, **Note that it may take the developers up to 1 hour to refund it to your balance!**")
      embed = E(title=f"ACCEPTED MISSING TRANSACTION", description=f"User:{ctx.author}\nID:{ctx.author.id}\nDetails:Missing deposit\nCurrency:{currency}\n[Explorer link]({explorer})\nComments:{msg.content}\n**ACCEPTED MISSING TRANSACTION**", color=blue)
      await membed.edit(embed=embed)
      return
  else:
    embed = E(title=f"{wrong} Error", description=f"This command only works in DMs!", color=red)
    await ctx.send(embed=embed)


@client.group()
async def modmail(ctx):
  if 'respond' in ctx.message.content:
    return
  channel = client.get_channel(910256986879295528)
  if isinstance(ctx.channel, discord.channel.DMChannel):
    Embed = E(title=f"Mod mail!", description=f"{ctx.author.mention}, You are connected with Mod-mail, please type your issue and a moderator will be with you shortly!\n**MAKE SURE YOU SEND YOUR ISSUE IN 1 MESSAGE OR IT WILL BE IGNORED!**", color=blue)
    await ctx.send(embed=Embed)
    def check(m) -> bool:
      return m.author == ctx.author and m.channel == ctx.channel
    msg = await client.wait_for("message", check=check)
    Embed = E(title=f"Mod-mail", description=f"Message sent to the moderators!!", color=blue)
    await ctx.send(embed=Embed)
    Embed = E(title=f"NEW MESSAGE", description=f"New message from {ctx.author} ID: {ctx.author.id}\nMessage:```{msg.content}```", color=blue)
    await channel.send(embed=Embed)
  else:
    embed = E(title=f"{wrong} Error", description=f"This command only works in DMs!", color=red)
    await ctx.send(embed=embed)


@client.command(aliases=['reply'])
async def respond(ctx, ID):
  ID = int(ID)
  member = client.get_user(ID)
  if ctx.author.id in admins:
    Embed = E(title=f"Mod mail!", description=f"{ctx.author.mention}, Please send the message you want to send to {member}!", color=blue)
    b = await ctx.send(embed=Embed)
    def check(m) -> bool:
      return m.author == ctx.author and m.channel == ctx.channel
    msg = await client.wait_for("message", check=check)
    if msg.content.lower() == 'cancel':
      await ctx.send("Mod-Mail Cancelled!")
    else:
      await ctx.send(f"{ctx.author.mention}, Message sent!!\nMessage:**{msg.content}**")
      await member.send(f"**New message** from Moderator:**{ctx.author}**\nMessage:**{msg.content}**")
      await asyncio.sleep(1)
      await b.delete()
      await msg.delete()
      await ctx.message.delete()


@report.command()
async def withdraw(ctx):
  getliveprices()
  databasebackup()
  if isinstance(ctx.channel, discord.channel.DMChannel):
    Embed = E(title=f"Report Missing withdrawal!", description=f"{ctx.author.mention}, Please send the currency of the missing withdrawal!", color=blue)
    await ctx.send(embed=Embed)
    def check(m) -> bool:
      return m.author == ctx.author and m.channel == ctx.channel
    msg = await client.wait_for("message", check=check)
    if msg.content not in currencies:
      embed = E(title=f"{wrong} Error", description=f"The currency you entered is not a supported currency on the bot!", color=red)
      await ctx.send(embed=embed)
      return
    else:
      currency = msg.content
      embed = E(title=f"Explorer link.", description=f"Please send the Explorer link of {currency}\nNote:It **must** be a link or your report will be ignored!", color=blue)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author and m.channel == ctx.channel
      msg = await client.wait_for("message", check=check)
      explorer = msg.content
      embed = E(title=f"Additional comments", description=f"Do you have any additional comments for the developers? Please send them now.\nIf not, type **none**", color=blue)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author and m.channel == ctx.channel
      msg = await client.wait_for("message", check=check)
      dchannel = client.get_channel(909935939520983121)
      embed = E(title=f"Missing Transaction reported!!", description=f"User:{ctx.author}\nID:{ctx.author.id}\nDetails:Missing Withdraw\nCurrency:{currency}\n[Explorer link]({explorer})\nComments:{msg.content}", color=blue)
      await ctx.send(embed=embed)
      await ctx.send("**Note: If you recive no reply from the bot by 2 days, your report was denyed!**")
      membed = await dchannel.send(embed=embed)
      await membed.add_reaction(emoji='✅')
      await asyncio.sleep(1)
      loop = 0
      while loop < 84400:
        loop += 1
      def check(reaction, user):
        return str(reaction) == ('✅')
      await client.wait_for("reaction_add", check=check)
      await ctx.send("Your report for your missing Withdraw report has been accepted, **Note that it may take the developers up to 1 hour to refund it to your balance!**")
      embed = E(title=f"ACCEPTED MISSING TRANSACTION", description=f"User:{ctx.author}\nID:{ctx.author.id}\nDetails:Missing Withdraw\nCurrency:{currency}\n[Explorer link]({explorer})\nComments:{msg.content}\n**ACCEPTED MISSING TRANSACTION**", color=blue)
      await membed.edit(embed=embed)
      return
  else:
    embed = E(title=f"{wrong} Error", description=f"This command only works in DMs!", color=red)
    await ctx.send(embed=embed)
@client.command()
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    embed = E(title='Uptime', description = f'My uptime is:\n{days}d\n{hours}h\n{minutes}m', color=green)
    await ctx.send(embed=embed)


@client.command()
async def locate(ctx, long=None, lat=None):
  if long == None:
    await ctx.send("Usage Error!\n\nPlease provide a longitude!")
    return
  if lat == None:
    await ctx.send("Usage Error!\n\nPlease provide a latitude!")
    return
  else:
    try:
      long = float(long)
      lat = float(lat)
    except:
      await ctx.send("Usage Error!\n\nUsage\n```.locate [longitude] [latitude]```")
    try:
      nasa_location = requests.get(f"https://api.nasa.gov/planetary/earth/assets?lon={long}&lat={lat}&date=2014-02-01&dim=0.15&api_key=oJ6ESoeSJFyn9Bdf4gURYFjGjkJiqhz8zghBElDo")
    except Exception as e:
      await ctx.send("Something went wrong while trying to fetch the location!")
      return
    else:
      nasa_location = nasa_location.json()
      try:
        nasa_location = nasa_location["url"]
      except Exception as e:
        embed=E(title=f"Data Not Found For Cordinates!", description=f"No satellite imagery could be found on the cordinates you provided!", color=red)
        await ctx.send(embed=embed)
        return
      embed = E(title=f"{loading} Fetching Image from API", color=blue)
      msg = await ctx.send(embed=embed)
      await asyncio.sleep(random.randint(5, 15))
      embed = E(title=f"{loading} Image Fetched Loading Image!")
      await msg.edit(embed=embed)
      embed = E(title=f"Fetched Location", description=f"longitude: {long}\nlatitude: {lat}", color=blue)
      embed.set_footer(text="Fetched using NASA's API")
      embed.set_image(url=nasa_location)
      await asyncio.sleep(random.randint(3, 10))
      await msg.edit(embed=embed)
      return

@client.command()
async def quiz(ctx, amount=None, currency=None, diffuculty: int=2):
  if isinstance(ctx.channel, discord.channel.DMChannel):
    embed = E(title=f"{wrong} Error", description=f"You can only use this command in a server!!", color=red)
    await ctx.send(embed=embed)
    return
  databasebackup()
  if int(diffuculty) == 1:
    diffuculty = "easy"
  elif int(diffuculty) == 2: 
    diffuculty = "medium"
  elif int(diffuculty) == 3:
    diffuculty = "hard"
  elif diffuculty == None:
    embed = E(title=f"{wrong} Usage Error!", description=f"{ctx.message.author.mention}, you must choose a correct diffuculty (example below)\n\n```.quiz 1 bnb [diffuculty]```\n\n1 -> Easy\n\n2 -> medium\n\n3 -> hard")
    await ctx.send(embed=embed)
    return
  if amount == None:
    embed=E(title=f"{wrong} Usage Error", description=f"No amount provided!\nUsage\n```.quiz [amount] [currency] (diffuculty) <-- optional parameter```")
    await ctx.send(embed=embed)
    return
  if currency == None:
    embed=E(title=f"{wrong} Usage Error!", description=f"No Currency Provided!\nUsage\n```.quiz [amount] [currency] (diffuculty) <-- optional parameter```")
    await ctx.send(embed=embed)
    return
  if TRX_lock == True:
    embed = E(title=f"{wrong} Bot preparing for maintenance!", description=f"{ctx.message.author.mention}, This bot is in preperation to restart all further transactions from here on will be blocked untill the bot is restarted! This is a feature we added so we can insure our users that their data will not be lost!", color=red) # migrate the phrasedrop command to the main file I dont think it migrated
    await ctx.send(embed=embed) # it doesnt work tho? Whoops I meant packet #that did migrate#oop nvm its broken
    return
  if currency.lower() == "st" or currency.lower() == "slicktoken":
    await ctx.send("ST is no longer supported on this bot!")
    return
  id = str(ctx.message.author.id)
  blacklist = openblacklist()
  if id in blacklist:
    b_status = blacklist[id]["blacklisted"]["status"]
    if b_status == True:
      print(f"{ctx.message.author}, ({ctx.message.author.id}) tried to quiz people! BLACKLISTED USER!!!")
      embed = E(title=f"{wrong} Account Blacklisted!", description=f"Your account is locked and under review by administrators! For more info you can join the support server (https://discord.gg/nCtGsxfrAu) or you can run the **.team** command to get the full list of all the moderaters contact information!", color=red)
      await ctx.send(embed=embed)
      return
  if currency.lower() == "jolt":
    currency = "jlt"
  elif currency.lower() == "globe":
    currency = "glb"
  elif currency.lower() == "ethereum":
    currency = "eth"
  elif currency.lower() == 'slicktoken':
    currency = 'st'
  elif currency.lower() == 'bitcoin':
    currency = 'btc'
  elif currency.lower() == "jetoken":
    currency = "jet"
  elif currency.lower() == "morphine":
    currency = "mrp"
  dollar_sign = "$"
  
  if dollar_sign in str(amount):
    amount = convertusdtocurrency(amount, currency)

  ID = str(ctx.message.author.id)
  inventory = opendb()
  if ID not in inventory:
    createaccount(ID)
  if currency not in currencies:
    embed = E(title=f"{wrong} Currency Not Found!", description=f"{ctx.message.author.mention}, this currency is not listed on this bot!", color=red)
    await ctx.send(embed=embed)
    return
  amount = str(amount)
  if amount.lower() == "all":
    amount = inventory[id][currency.lower()]['amt']
    amount = amount
  amount = float(amount)
  dollaramt = convertcurrencytousd(amount, currency)
  if float(dollaramt) < 0.0:
    embed = E(title=f"{wrong} Amount Too Low!", descripiton=f"You must drop at least **$0.0001 of {currency.upper()}!**")
    await ctx.send(embed=embed)
    return
  inventory = opendb()
  ID=str(ctx.message.author.id)
  user_balance = inventory[ID][str(currency.lower())]['amt']
  if user_balance < amount:
    embed=E(title=f"{wrong} Not Enough Money!", descripiton=f"{ctx.message.author.mention}, you do not have enough money to complete this transaction!", color=red)
    await ctx.send(embed=embed)
    return
  else:
    inventory = opendb()
    inventory[ID][str(currency.lower())]['amt'] -= amount
    savedb(inventory)
  request_question = requests.get(f"https://opentdb.com/api.php?amount=1&difficulty={diffuculty}&type=multiple")
  quiz_json = request_question.json()
  category = quiz_json["results"][0]["category"]
  difficulty = quiz_json["results"][0]["difficulty"]
  question = quiz_json["results"][0]["question"]
  answer = quiz_json["results"][0]["correct_answer"]
  nerd = ":nerd:"
  sad = "<:pepecry:914600243738316810>"
  try:
    question = question.replace('&quot;', "")
    question = question.replace("&#039;", "")
    question = question.replace("&rsquo;", "'")
    category = category.replace(":", "")
    answer = answer.replace(".", "")
  except Exception as e:
    return
  embed = E(title=f"{nerd} Quiz Drop!", description=f"{ctx.message.author.mention}, has dropped **{amount} {currency.upper()}** Answer the Question Correctly to win the prize!\n\n The Question is **{question}**\n\ndifficulty: **{difficulty.upper()}**\ncategory: **{category}**\n", color=blue)
  embed.set_footer(text="Be first to Answer the question!")
  msg = await ctx.send(embed=embed)
  def check(winner):
    return winner.channel == ctx.message.channel and winner.id != client.user.id
  while True:
    try:
      mssg = await client.wait_for('message', check=check, timeout=1)
      if TRX_lock == True:
        embed = E(title=f"{wrong} Bot preparing for maintenance!", description=f"This Quiz Drop has been refunded since the bot was scheduled for maitenence!", color=red)
        inventory = opendb()
        inventory[ID][str(currency.lower())]['amt'] += amount
        savedb(inventory)
        await msg.edit(embed=embed)
        return
      users_answer = mssg.content.lower()
      if str(users_answer) in str(answer.lower()):
        ID = mssg.author.id
        if ID == 869390064172552192:
          pass
        else:
          inventory = opendb()
          if ID not in inventory:
            createaccount(str(ID))
          inventory = opendb()
          inventory[str(ID)][str(currency.lower())]['amt'] += amount
          savedb(inventory)
          embed = E(title=f"Quiz Drop Answered!", description=f"<@{ID}> has answered the quiz drop of **{amount} {currency.upper()}** correctly!", color=blue)
          embed.set_footer(text="This Quiz Drop has Already Been collected!")
          await msg.edit(embed=embed)
          break

    except asyncio.TimeoutError:
      pass




  
  

  
@client.command()
async def leave(ctx, ID:str):
  if ctx.author.id in admins:
    to_leave = client.get_guild(int(ID))
    await to_leave.leave()
    await ctx.send(f"Left {to_leave} successfully!")
  else:
    await ctx.send("You do not have the permissions to do that!")



  
@client.command()
async def servers(ctx):
  devinfo = []
  enter = '\n'
  display_servers_page1 = []
  display_servers_page2 = []
  display_servers_page3 = []
  add_me = 0
  for guild in client.guilds:
    display_servers_page1.append(f"*{guild.name}* - **{guild.member_count} Members**")
    devinfo.append(f"{guild.name} - {guild.id} - {guild.owner}")




  tpages = 3
  e = discord.Embed(title=f"Additional server info (top 10)", description=f"{enter.join(ch for ch in devinfo)}", colour=discord.Colour.dark_blue())
  await ctx.author.send(embed=e)
  page1 = discord.Embed(title=f"Servers (1/{tpages})", description=f"{enter.join(ch for ch in display_servers_page1)}", colour=discord.Colour.dark_blue())
  page2 = discord.Embed(title=f"Servers (2/{tpages})", description=f"{enter.join(ch for ch in display_servers_page2)}", colour=discord.Colour.dark_blue())
  page3 = discord.Embed(title=f"Servers (3/{tpages})", description=f"{enter.join(ch for ch in display_servers_page3)}", colour=discord.Colour.dark_blue())
  msg = await ctx.send(embed=page1)
  if add_me > 10:
    await msg.add_reaction("⬅️")
    await msg.add_reaction("➡️")
    page=1
    emojis = ["⬅️", "➡️"]
    def check(reaction, user):
        return user == ctx.author and reaction.emoji in emojis and reaction.message == msg
    while True:
          r, u = await client.wait_for('reaction_add', check=check)
          await msg.remove_reaction(r.emoji, u)
          if r.emoji == "➡️":
            if page == 1:
              await msg.edit(embed=page2)
              page+=1
            elif page == 2:
              await msg.edit(embed=page3)
              page+=1
            elif page == 3:
              pass
          elif r.emoji == "⬅️":
            if page == 1:
              pass
            elif page == 2:
              await msg.edit(embed=page1)
              page-=1
            elif page == 3:
              await msg.edit(embed=page2)
              page-=1
          
        
      

    
    


    
    pass  

    

@client.command()
async def mint(ctx, amount: int):
  ID = str(ctx.message.author.id)
  if ctx.message.author.id not in admins:
    return
  packs = openpacks()
  try:
    packs["supply"] += amount
    savepacks(packs)
  except Exception as e:
    embed = E(title=f"{wrong} Mint Error", description=f"An error occured when you tried to mint {amount} packs!\nError: {e}", color=red)
    await ctx.send(embed=embed)
    return
  coll = opencollection()
  if ID not in coll:
    coll[ID] = {}
    coll[ID]["pack"] = {}
    coll[ID]["pack"]["amt"] = 0 
    savecollection(coll) 
  totalsupply = packs["supply"]
  coll = opencollection()
  coll[ID]["pack"]["amt"] += amount
  savecollection(coll) 
  embed = E(title=f"{check} Minted {amount} packs!", description=f"You have minted {amount} packs, you should now see them in your collection!\nTotal Supply: {totalsupply}", color=green)
  await ctx.send(embed=embed)
  return
  
@client.command()
async def nasapic(ctx):
  try:
    Nasa_stats = requests.get(nasaURL)
    json_nasa_stats = Nasa_stats.json()
    daily_pic_nasa = json_nasa_stats["url"]
  except Exception as e:
    pass
  info_pic_nasa = json_nasa_stats["explanation"]
  embed = E(title=f"Daily Space Picture!", description=f"**Image Description**\n\n{info_pic_nasa}\n\n**Fetched using NASA's API**", color=blue)
  embed.set_image(url=daily_pic_nasa)
  await ctx.send(embed=embed)
@client.command()
async def tsupply(ctx):
  packs = openpacks()
  totalsupply = packs["supply"]
  embed = E(title=f"{JoltPack}   Total Supply", description=f"There are {totalsupply} Unopened Jolt Packs in circulation!", color=blue)
  await ctx.send(embed=embed)
  return


  
@client.command()
async def packs(ctx):
  ID = str(ctx.message.author.id)
  coll = opencollection()
  if ID not in coll:
    coll[ID] = {}
    coll[ID]["pack"] = {}
    coll[ID]["pack"]["amt"] = 0
    savecollection(coll)
  packs = coll[ID]["pack"]["amt"]
  embed = E(title=f"{JoltPack}  Jolt Packs", description=f"{ctx.message.author.mention}, your Pack balance is {packs}", color=discord.Colour(0x2596be))
  await ctx.send(embed=embed)
  return
developer_badge = "<:dev:900563593253253160>"
partner_badge = "<a:partnered:942502024220651570>"
moderator_badge = "<:SrModerator:942502490530807808>"
verified_badge = "<a:verified:942502885651021884>"

@client.command()
async def badges(ctx):
  ID = str(ctx.message.author.id)


@client.command(aliases=["userdash"])
async def dashboard():
  pass

def Create(user): #Create inventory
  ID = str(user.id)
  coll = opencollection()
  coll[ID] = {}
  coll[ID]["pack"] = {}
  coll[ID]["pack"]["amt"] = 0
  savecollection(coll)
def databasebackup():
  with open ("dbs/inventory.json") as f:
    lines = f.readlines()
    f.close()

  with open ("databasebackup.txt", "w+") as f:
    f.truncate(0)
    lines = str(lines)
    f.write(lines)
    f.close()



    
def baclist(user):
  
  ID = str(user.id)
  blacklist = openblacklist()
  blacklist[ID] = {}
  blacklist[ID]["blacklisted"] = {}
  blacklist[ID]["blacklisted"]["status"] = False
  saveblacklist(blacklist)

@client.event
async def on_ready():
  databasebackup()
  status.start()
  dbbase.start()
  print(f"Logged in as {client.user}!")
  servers = len(client.guilds)
  members = 0
  for guild in client.guilds:
    members += guild.member_count - 1
  await client.change_presence(activity = discord.Activity(
    type = discord.ActivityType.watching,
    name = f'{servers} servers and {members} users'
  ))

@tasks.loop(hours=5)
async def status():
  databasebackup()
  servers = len(client.guilds)
  members = 0
  for guild in client.guilds:
    members += guild.member_count - 1
  await client.change_presence(activity = discord.Activity(
    type = discord.ActivityType.watching,
    name = f'{servers} servers and {members} users'
  ))

@tasks.loop(seconds=900)
async def dbbase():
  databasebackup()
  channel = client.get_channel(942182366145835108)
  b=(time.strftime("%H:%M:%S"))
  await channel.send(f'Database Backup!\nTime:{b}', file=discord.File("databasebackup.txt"))



pages = 3
page_1_tokens = embed=E(title=f"Tokens Listed (1/{pages})", description=f"Jolt Token\n{jolt} Jolt contract ```0xac19e03d269811a2d837109ff6582da1a4016e9d```\nCaptian Token\n{capt} Captian contract: ```0xdf5301b96ceccb9c2a61505b3a7577111056a4c5```\nBinance Token\n{bnb} BNB contract: ```0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c```\nJolt classic Token\n{joltclassic} Jolt Classic contract: ```0x59b31ab138f895330337d7fb41ed0d79ae8763e0```", color=blue) # 4 tokens on each 
# ---- 
page_2_tokens = embed=E(title=f"Tokens Listed (2/{pages})", description=f"Binance USD Token\n{BinanceUSD} Binance USD contract: ```0xe9e7cea3dedca5984780bafc599bd69add087d56```\nShiba Inu\n{ShibaInu} Shiba Inu contract: ```0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce```\nKitsune Token\n{KitsuneToken} Kitsune contract: ```0x66aFC53B499701f963548A578F990e3c528e2048```\nGlobe token\n{globeToken} Globe contract: ```0xf46b841f9367f5ff559c8670617129452607e722```", color=blue)

page_3_tokens = embed=E(title=f"Tokens Listed (3/{pages})", description=f"Bitcoin\n{btc} Bitcoin Information [here](https://www.coingecko.com/en/coins/bitcoin)\nJetoken\n{jetokenToken} Jetoken contract: ```0x0f005dfe97c5041e538b7075915b2ee706677c26```\nMophine Token\n{MorphineToken}\n```0xb8608f270497764a10c28bfe75454f68b31ba2b1```", color=blue)




@client.command()
async def tokens(ctx):
    msg = await ctx.send(embed=page_1_tokens)
    await msg.add_reaction("⬅️")
    await msg.add_reaction("➡️")
    page=1
    emojis = ["⬅️", "➡️"]
    def check(reaction, user):
        return user == ctx.author and reaction.emoji in emojis and reaction.message == msg
    while True:
          r, u = await client.wait_for('reaction_add', check=check)
          await msg.remove_reaction(r.emoji, u)
          if r.emoji == "➡️":
            if page == 1:
              await msg.edit(embed=page_2_tokens)
              page+=1
            elif page == 2:
              await msg.edit(embed=page_3_tokens)
              page+=1
            elif page == 3:
              pass
          elif r.emoji == "⬅️":
            if page == 1:
              pass
            elif page == 2:
              await msg.edit(embed=page_1_tokens)
              page-=1
            elif page == 3:
              await msg.edit(embed=page_2_tokens)
              page-=1
          
        
      

    
    


    
    pass  




@client.command()
async def info(ctx):
  msg = await ctx.send(f"Please wait, this may take a while.")
  guilds = 0
  members = 0
  for guild in client.guilds:
    guilds += 1
    for member in guild.members:
      members += 1
  await msg.edit(content = f"{guilds} guilds and {members} members")




@client.command()
async def createcode(ctx):
  if isinstance(ctx.channel, discord.channel.DMChannel):
    ID=str(ctx.message.author.id)
    promocode = openpromo()
    if ID in promocode:
      promoc = promocode[ID]["promocode"]["Value"]
      embed = E(title=f"You already have a promocode!", description=f"You already created a promocode type **.vault** to see your codes stats!\n\nCode\n **{promoc.upper()}**", color=blue)
      await ctx.send(embed=embed)
      return
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    Letter_1 = random.choice(alpha)
    Letter_2 = random.choice(alpha)
    Letter_3 = random.choice(alpha)
    Letter_4 = random.choice(alpha)
    Letter_5 = random.choice(alpha)
    Letter_6 = random.choice(alpha)
    promo = (f'{Letter_1}{Letter_2}{Letter_3}{Letter_4}{Letter_5}{Letter_6}')
    while promo in promocode:
      Letter_1 = random.choice(alpha)
      Letter_2 = random.choice(alpha)
      Letter_3 = random.choice(alpha)
      Letter_4 = random.choice(alpha)
      Letter_5 = random.choice(alpha)
      Letter_6 = random.choice(alpha)
      promo = (f'{Letter_1}{Letter_2}{Letter_3}{Letter_4}{Letter_5}{Letter_6}')
    if ID not in promocode:
      codes = opencodes()
      codes["promocodes"] = {promo}
      
      savecodes(codes)
      promocode = openpromo()
      promocode[ID] = {} # oh I think I kno
      promocode[ID]["promocode"] = {} 
      promocode[ID]["promocode"]["Value"] = promo
      promocode[ID]["promocode"]["Uses"] = 0 # ok finish it  k
      promocode[ID]["promocode"]["Vault"] = 0.00
      promocode[ID]["promocode"]["Deposits"] = 0
      promocode[ID]["promocode"]["Withdraws"] = 0 #yh it dont work
      savepromo(promocode)
      promoc = promocode[ID]["promocode"]["Value"]
      embed = E(title=f"Promocode Created!", description=f"Your promocode is **{promoc.upper()}**\n\nYou can check your promocode stats by doing ```.vault```", color=blue)
      await ctx.send(embed=embed)
      return
  else:
    embed=E(title=f"{wrong} This can only be used in direct messages!", description=f"You can only use this command in direct messages with the bot!", color=red)
    await ctx.send(embed=embed)
    return
@client.command()
async def use(ctx, promocode=None):
  if promocode == None:
    embed = E(title=f"{wrong} No promocode provided", description=f"Looks like you used this command wrong!\n\nCommand Usage\n\n```.use [promocode]```", color=red)
    await ctx.send(embed=embed)
    return
  promocodedb = openpromo()
  if promocode not in promocodedb:
    embed = E(title=f"{wrong} Promocode not found!", descripton=f"The promocode you wanted to use does not seem to be in the database!", color=red)
    await ctx.send(embed=embed)
    return

  else:
    for code in search_code:
      if str(code) != str(promocode):
        pass
      else:
        code += 1
    embed = E(title=f"{check} Using code!", descripton=f"You are using the promocode: **{code}**",color=green)
    await ctx.send(embed=embed)


    


@client.command()
async def phrasedrop(ctx, amount=None, currency=None, duration: str='1m',*, phrase=None):
  ttimee = duration
  await ctx.message.delete()
  if amount == None:
    embed = E(title=f"{wrong} Usage Error", description=f"{ctx.message.author.mention}, You must include an amount!\n\n**Usage:**```.phrasedrop [amount] [currency] [duration] [phrase]```", color=red)
    await ctx.send(embed=embed)
    return
  elif currency == None:
    embed = E(title=f"{wrong} Usage Error", description=f"{ctx.message.author.mention}, You must include a phrase!\n\n**Usage:**```.phrasedrop [amount] [currency] [duration] [phrase]```", color=red)
    await ctx.send(embed=embed)
    return
  elif phrase == None:
    embed = E(title=f"{wrong} Usage Error", description=f"{ctx.message.author.mention}, You must include a phrase!\n\n**Usage:**```.phrasedrop [amount] [currency] [duration] [phrase]```", color=red)
    await ctx.send(embed=embed)
    return
  if currency.lower() == "jlt":
    a_bal = 'jlt' 
    currency = "jlt"
  elif currency.lower() == 'bnb':
    a_bal = 'bnb'
    currency = "bnb"
  elif currency.lower() == 'capt':
    a_bal = 'capt'
    currency = "capt"
  elif currency.lower() == 'jlc':
    a_bal = 'jlc'
    currency = "jlc"
  elif currency.lower() == 'busd':
    a_bal = 'busd'
    currency = "busd"
  elif currency.lower() == "morphine" or currency.lower() == "mrp":
    a_bal = 'mrp'
    currency = 'mrp'
  elif currency.lower() == 'shiba' or currency.lower() == "shib":
    a_bal = 'Shiba'
    currency = "Shiba"
  elif currency.lower() == 'sina':
    a_bal = 'sina'
    currency = "sina"
  elif currency.lower() == 'globe' or currency.lower() == "glb":
    a_bal = 'glb'
    currency = "glb"
  elif currency.lower() == 'eth':
    a_bal = 'eth'
    currency = "eth"
  elif currency.lower() == 'slicktoken' or currency.lower() == "st":
    a_bal = 'st'
    currency = "st"
  elif currency.lower() == 'bitcoin' or currency.lower() == "btc":
    a_bal = 'btc'
    currency = "btc"
  elif currency.lower() == "jetoken":
    currency = "jet"
  else:
    embed = E(title=f"{wrong} Currency Not Found!", description=f"{ctx.message.author.mention}, this currency is not listed on this bot!", color=red)
    await ctx.send(embed=embed)
    return
  if currency.lower() == "st" or currency.lower() == "slicktoken":
    await ctx.send("ST is no longer supported on this bot!")
    return
  dollar_sign = "$"
  if dollar_sign in str(amount):
    amount = convertusdtocurrency(amount, currency)
  amount = str(amount)
  if amount.lower() == "all":
    amount = float(amount)
    inventory = opendb() 
    drop_id=str(ctx.message.author.id)
    amount = inventory[drop_id][a_bal]['amt']
  amount = float(amount)
  drop_id=str(ctx.message.author.id)

  sad = ":cry:"
  global pending_trxs
  global TRX_lock
  ID = str(ctx.message.author.id)
  inventory = opendb()
  if ID not in inventory:
    createaccount(ID)
  if TRX_lock == True:
    embed = E(title=f"{wrong} Bot preparing for maintenance!", description=f"{ctx.message.author.mention}, This bot is in preperation to restart all further transactions from here on will be blocked untill the bot is restarted! This is a feature we added so we can insure our users that their data will not be lost!", color=red)
    await ctx.send(embed=embed)
    return
  inventory = opendb()
  id = str(ctx.message.author.id)
  blacklist = openblacklist()
  if id in blacklist:
    b_status = blacklist[id]["blacklisted"]["status"]
    if b_status == True: 
      print(f"{ctx.message.author}, ({ctx.message.author.id}) tried to withdraw! BLACKLISTED USER!!!")
      embed = E(title=f"{wrong} Account Blacklisted!", description=f"Your account is locked and under review by administrators! For more info you can join the support server (https://discord.gg/nCtGsxfrAu) or you can run the **.team** command to get the full list of all the moderaters contact information!", color=red)
      await ctx.send(embed=embed)
      return
  if currency == None:                                          
    embed = E(title=f"{wrong}, You must pick a currency to airdrop!", description=f"{ctx.message.author.mention}, You did not specify a currency to airdrop!", color=red)
    await ctx.send(embed=embed) # it works now you can test it
    return
  if amount == None:
    embed = E(title=f"{wrong} You must specify an amount!", description=f"{ctx.message.author.mention}, You must specify the amount of {currency} you want to drop!", color=red)
    await ctx.send(embed=embed)
    return #my hand r rlly sticky from this drumstick, brb, its a sweet dont take it out of context. halloween
  if duration == None:
    embed = E(title=f"{wrong} You must specify the time you want the airdrop to run for!", description=f"Please provide a duration!", color=red)
    await ctx.send(embed=embed)
    return
  
  if currency == "jolt":
    currency = "jlt"
  elif currency == "globe":
    currency = "glb"
  elif currency == "ethereum":
    currency = "eth"
  elif currency == "bitcoin":
    currency = "btc"
  elif currency == "morphine":
    currency = "mrp"
  
  dollar_sign = "$"
  if currency not in currencies:
    embed = E(title=f"{wrong} Currency Not Found!", description=f"{ctx.message.author.mention}, this currency is not listed on this bot!", color=red)
    await ctx.send(embed=embed)
    return
  # --- 

  if True:
    amount = float(amount)
  if currency.lower() == "jolt":
      dollaramt = (round(float(float(amount) * jltPrice), 6))
      amount = float(amount)
  elif currency.lower() == "joltclassic":
      dollaramt = (round(float(float(amount) * jlcPrice), 2))
      amount = float(amount)
  elif currency.lower() == "jlc":
      dollaramt = (round(float(float(amount) * jlcPrice), 2))
      amount = float(amount)
  elif currency.lower() == "bnb":
      dollaramt = (round(float(float(amount) * bnbPrice), 2))
      amount = float(amount)
  elif currency.lower() == "capt":
      dollaramt = (round(float(float(amount) * captPrice), 2))
      amount = float(amount)
  elif currency.lower() == "jlt":
      dollaramt = (round(float(float(amount) * jltPrice), 6))
      amount = float(amount)
  elif currency.lower() == "busd":
      dollaramt = (round(float(float(amount) * busdPrice), 2))
      amount = float(amount)
  elif currency.lower() == "shiba":
      dollaramt = (round(float(float(amount) * shibaPrice), 2))
      amount = float(amount)
  elif currency.lower() == "kitsune":
      dollaramt = (round(float(float(amount) * sinaPrice), 2))
      amount = float(amount)
  elif currency.lower() == "glb":
      dollaramt = (round(float(float(amount) * glbPrice), 2))
      amount = float(amount)
  elif currency.lower() == "eth":
      dollaramt = (round(float(float(amount) * ethPrice), 2))
      amount = float(amount)
  elif currency.lower() == "matic":
      dollaramt = (round(float(float(amount) * maticPrice), 2))
      amount = float(amount)
  elif currency.lower() == "nano":
      dollaramt = (round(float(float(amount) * nanoPrice), 2))
      amount = float(amount)
  elif currency.lower() == "st":
      dollaramt = (round(float(float(amount) * stPrice), 2))
      amount = float(amount)
  elif currency.lower() == "btc":
      dollaramt = (round(float(float(amount) * bitcoinPrice), 2))
      amount = float(amount)
  elif currency.lower() == "jet":
      dollaramt = (round(float(float(amount) * jetokenPrice), 2))
      amount = float(amount)
  elif currency.lower() == "mrp":
      dollaramt = (round(float(float(amount) * morphinePrice), 2))
      amount = float(amount)
  time = conv(duration)
 
  if int(time) > 259200:
    embed = E(title=f"{wrong} Time Error", description=f"you cannot set a Phrasedrop to be longer than 72 hours!", color=red)
    await ctx.send(embed=embed)
    return
  if int(time) == 0:
    time = 3600
  
 
  if inventory[drop_id][currency.lower()]['amt'] < float(amount):
    embed = E(title=f"{wrong} Insufficient Funds", description=f"{ctx.message.author.mention}, You do not have enough **{currency.lower()}** to complete this transaction!", color=red)
    await ctx.send(embed=embed)
    return
  
  
  try:
    inventory[drop_id][str(currency)]['amt'] -= float(amount)
    savedb(inventory)
    pending_trxs += 1
  except Exception as e:
    await ctx.send(e)
    pending_trxs -= 1
    return
    

  

  if dollaramt < 0.0:
    embed = E(title=f"{wrong} Amount Too Low!", description=f"{ctx.message.author.mention}, You must airdrop at least 0.00001$ **{currency.lower()}**!")
    await ctx.send(embed=embed)
    pending_trxs -= 1
    return
  
  embed = E(title=f"Phrasedrop", description=f"{ctx.message.author.mention}, Started a Phrasedrop of {round(amount, 6)} {currency.upper()} (~${dollaramt})\n\n**Type the message `{phrase}` to collect the prize!**\nEnding in {ttimee.lower()}!", color=green)
  embed.set_footer(text=f"You must type the **exact** message including spaces(caps do not matter)")
  msg = await ctx.send(embed=embed)
  nil = 0
  def check(winner):
    return winner.channel == ctx.channel
 
  winners = []
  pool = 0
  while time > nil:
    try:
      mssg = await client.wait_for('message', timeout=1, check=check)
    except Exception:
      mssg = ""
      pass
    try:
      inventory = opendb()
      if mssg.content.lower() == phrase:
        ID = str(mssg.author.id) 
        author = str(ctx.author.id)
        if ID == author:
          pass
        elif ID not in winners:
          if ID not in inventory:
            createaccount(ID)
          pool += 1
          winners.append(mssg.author.id)
    except Exception:
      pass
    time -= 1
    if TRX_lock == True:
      embed = E(title=f"Phrasedrop Refunded", description=f"This phrasedrop was refunded to {ctx.message.author.mention} because the bot was scheduled for maintenance!", color=red)
      await msg.edit(embed=embed)
      member = ctx.message.author
      channel = await member.create_dm()
      embed = E(title=f"Phrasedrop Refunded", description=f"{ctx.message.author.mention}, your phrasedrop of **{round(amount, 6)} {currency}** has been refunded since the bot was scheduled for maintenance!", color=blue)
      await channel.send(embed=embed)
      inventory = opendb()
      inventory[drop_id][str(currency)]['amt'] += amount
      savedb(inventory)
      pending_trxs -= 1
      return
  rewarded = []

  if pool == 0: 
    embed = E(title=f"{sad} Phrasedrop Ended!", description=f"This Phrasedrop of **{round(amount, 6)} {currency.upper()}** has ended!\n\nNobody Replied with the phrase!")
    await msg.edit(embed=embed)
    inventory = opendb()
    inventory[drop_id][str(currency)]['amt'] += amount
    savedb(inventory)

    pending_trxs -= 1
    return
  total_share = float(amount) / float(pool)
  checkifint = int(total_share)
  if total_share == checkifint:
    pass
  else:
    total_share = round(total_share, 8)
  print(total_share)

  if str(ctx.author.id) in winners:
    winners.remove(str(ctx.author.id))
  if True:
    indexposition = 0
    for winner in winners:
      
      ID = winners[indexposition]
      ID = str(ID)
      indexposition += 1
      inventory = opendb()
      author = str(ctx.author.id)
      if ID not in inventory:
        if ID not in rewarded:
          rewarded.append(ID)
          inventory = opendb()
          inventory[ID][a_bal]["amt"] += total_share
          savedb(inventory)
      else:
        if ID not in rewarded:
          ID = str(ID)
          author = str(ctx.author.id)
          rewarded.append(ID)
          inventory = opendb()
          author = str(ctx.author.id)
          if ID == author:
            pass
          inventory = opendb()
          inventory[ID][a_bal]["amt"] += total_share
          savedb(inventory)
    reward_people = re.sub(r'(\d+)', r'<@\1>', str(rewarded))

    reward_people = reward_people.strip("[]") 
    reward_people = reward_people.replace(",", "")
    reward_people = reward_people.replace("'", "")
    embed = E(title=f"This Phrasedrop has Ended!", description=f"This Phrasedrop of **{amount} {currency}** has ended!\n\nCollected By: {reward_people}\n\nRewarded {total_share} each!")
    await msg.edit(embed=embed)
    pending_trxs -= 1
    return



  
def convertnotation(number, decpoint):
  try:
    number = float(number)
  except:
    return
  round_here = ("{:." + str(decpoint) + "f}")
  result_float = round_here.format(number)
  return result_float



@client.command()
async def convertme(ctx):
  number_to_convert = 7.09106702831109e+32
  after_convert = convertnotation(number_to_convert, 6)
  await ctx.send(f"Before: {number_to_convert}\nAfter: {after_convert}")

@client.command()
async def airdrop(ctx, amount=None, currency=None, duration: str='1m'):
  databasebackup()
  global pending_trxs 
  global TRX_lock
  ID = str(ctx.message.author.id)
  if isinstance(ctx.channel, discord.channel.DMChannel):
    embed = E(title=f"{wrong} Error", description=f"You can only use this command in a server!!", color=red)
    await ctx.send(embed=embed)
    return
  inventory = opendb()
  if ID not in inventory:
    createaccount(ID)
  if TRX_lock == True:
    embed = E(title=f"{wrong} Bot preparing for maintenance!", description=f"{ctx.message.author.mention}, This bot is in preperation to restart all further transactions from here on will be blocked untill the bot is restarted! This is a feature we added so we can insure our users that their data will not be lost!", color=red) # migrate the phrasedrop command to the main file I dont think it migrated
    await ctx.send(embed=embed) # it doesnt work tho? Whoops I meant packet #that did migrate#oop nvm its broken
    return
  if currency.lower() == "st" or currency.lower() == "slicktoken":
    await ctx.send("ST is no longer supported on this bot!")
    return
  inventory = opendb()
  id = str(ctx.message.author.id)
  blacklist = openblacklist()
  if id in blacklist:
    b_status = blacklist[id]["blacklisted"]["status"]
    if b_status == True:
      print(f"{ctx.message.author}, ({ctx.message.author.id}) tried to withdraw! BLACKLISTED USER!!!")
      embed = E(title=f"{wrong} Account Blacklisted!", description=f"Your account is locked and under review by administrators! For more info you can join the support server (https://discord.gg/nCtGsxfrAu) or you can run the **.team** command to get the full list of all the moderaters contact information!", color=red)
      await ctx.send(embed=embed)
      return
  if currency == None:                                          
    embed = E(title=f"{wrong}, You must pick a currency to airdrop!", description=f"{ctx.message.author.mention}, You did not specify a currency to airdrop!", color=red)
    await ctx.send(embed=embed) # it works now you can test it
    return
  if amount == None:
    embed = E(title=f"{wrong} You must specify an amount!", description=f"{ctx.message.author.mention}, You must specify the amount of {currency} you want to drop!", color=red)
    await ctx.send(embed=embed)
    return #my hand r rlly sticky from this drumstick, brb, its a sweet dont take it out of context. halloween
  if duration == None:
    embed = E(title=f"{wrong} You must specify the time you want the airdrop to run for!", description=f"Please provide a duration!", color=red)
    await ctx.send(embed=embed)
    return
  drop_id=str(ctx.author.id)
  if currency.lower() == "jolt":
    currency = "jlt"
  elif currency.lower() == "globe":
    currency = "glb"
  elif currency.lower() == "ethereum":
    currency = "eth"
  elif currency.lower() == 'slicktoken':
    currency = 'st'
  elif currency.lower() == 'bitcoin':
    currency = 'btc'
  elif currency.lower() == "jetoken":
    currency = "jet"
  elif currency.lower() == "morphine":
    currency = "mrp"
  if currency not in currencies:
    embed = E(title=f"{wrong} Currency Not Found!", description=f"{ctx.message.author.mention}, this currency is not listed on this bot!", color=red)
    await ctx.send(embed=embed)
    return
  if str(amount) == "all":
    amount = inventory[drop_id][currency.lower()]['amt']
    amount = amount
  if "$" in str(amount):
    amount = convertusdtocurrency(amount, currency)
    am = (round(amount, 6))
  else:
    amount = float(amount)
    am = (round(amount, 6))
  if currency.lower() == "jolt":
      dollaramt = (round(float(float(amount) * jltPrice), 6))
      amount = float(amount)
  elif currency.lower() == "joltclassic":
      dollaramt = (round(float(float(amount) * jlcPrice), 6))
      amount = float(amount)
  elif currency.lower() == "jlc":
      dollaramt = (round(float(float(amount) * jlcPrice), 6))
      amount = float(amount)
  elif currency.lower() == "bnb":
      dollaramt = (round(float(float(amount) * bnbPrice), 6))
      amount = float(amount)
  elif currency.lower() == "capt":
      dollaramt = (round(float(float(amount) * captPrice), 6))
      amount = float(amount)
  elif currency.lower() == "jlt":
      dollaramt = (round(float(float(amount) * jltPrice), 6))
      amount = float(amount)
  elif currency.lower() == "busd":
      dollaramt = (round(float(float(amount) * busdPrice), 6))
      amount = float(amount)
  elif currency.lower() == "shiba":
      dollaramt = (round(float(float(amount) * shibaPrice), 6))
      amount = float(amount)
  elif currency.lower() == "kitsune":
      dollaramt = (round(float(float(amount) * sinaPrice), 6))
      amount = float(amount)
  elif currency.lower() == "glb":
      dollaramt = (round(float(float(amount) * glbPrice), 6))
      amount = float(amount)
  elif currency.lower() == "eth":
      dollaramt = (round(float(float(amount) * ethPrice), 6))
      amount = float(amount)
  elif currency.lower() == "matic":
      dollaramt = (round(float(float(amount) * maticPrice), 6))
      amount = float(amount)
  elif currency.lower() == "nano":
      dollaramt = (round(float(float(amount) * nanoPrice), 6))
      amount = float(amount)
  elif currency.lower() == "st":
      dollaramt = (round(float(float(amount) * stPrice), 6))
      amount = float(amount)
  elif currency.lower() == "btc":
      dollaramt = (round(float(float(amount) * bitcoinPrice), 6))
      amount = float(amount)
  elif currency.lower() == "jet":
      dollaramt = (round(float(float(amount) * jetokenPrice), 6))
      amount = float(amount)
  elif currency.lower() == "mrp":
      dollaramt = (round(float(float(amount) * morphinePrice), 6))
      amount = float(amount)
  time = conv(duration)
 
  if int(time) > 259200:
    embed = E(title=f"{wrong} Time Error", description=f"you cannot set a airdrop to be longer than 72 hours!", color=red)
    await ctx.send(embed=embed)
    return
  if int(time) == 0:
    time = 3600
 
  if inventory[drop_id][currency.lower()]['amt'] < float(amount):
    embed = E(title=f"{wrong} Insufficient Funds", description=f"{ctx.message.author.mention}, You do not have enough **{currency.lower()}** to complete this transaction!", color=red)
    await ctx.send(embed=embed)
    return
  
  
  try:
    inventory[drop_id][str(currency)]['amt'] -= float(amount)
    savedb(inventory)
    pending_trxs += 1
  except Exception as e:
    await ctx.send(e)
    return
    

  
 

  
  emojis = ["✅", "😃", "🤣", "😊", "🥰", "😇", "😍", "😘"]
  emoji = random.choice(emojis)
  rabbit = ":airplane:"
  sad = ":cry:"
  if currency in currencies:
    if currency.lower() == "jlt":
      a_bal = 'jlt'
    elif currency.lower() == 'bnb':
      a_bal = 'bnb'
    elif currency.lower() == 'capt':
      a_bal = 'capt'
    elif currency.lower() == 'jlc':
      a_bal = 'jlc'
    elif currency.lower() == 'busd':
      a_bal = 'busd'
    elif currency.lower() == 'shiba':
      a_bal = 'Shiba'
    elif currency.lower() == 'sina':
      a_bal = 'sina'
    elif currency.lower() == 'glb':
      a_bal = 'glb'
    elif currency.lower() == 'matic':
      a_bal = 'matic'
    elif currency.lower() == 'nano':
      a_bal = 'nano'
    elif currency.lower() == 'st':
      a_bal = 'st'
    elif currency.lower() == 'btc':
      a_bal = 'btc'
    elif currency.lower() == 'mrp':
      a_bal = 'mrp'
  if dollaramt < 0.00001:
    embed = E(title=f"{wrong} Amount Too Low!", description=f"{ctx.message.author.mention}, You must airdrop at least 0.00001$ **{currency.lower()}**!")
    await ctx.send(embed=embed)
    pending_trxs -= 1
    return
  embed = E(title=f"{rabbit} Airdrop", description=f"{ctx.message.author.mention}, Dropped {round(amount, 6)} {currency.upper()} **(~${dollaramt:.6f})**\n\n**React with the {emoji} emoji to grab the prize!**", color=green)
  embed.set_footer(text=f"Ending in {time} seconds!")
  msg = await ctx.send(embed=embed)
  await msg.add_reaction(emoji)
  nil = 0

  while time > nil:
    await asyncio.sleep(1)
    time -= 1
    if TRX_lock == True:
      embed = E(title=f"{sad} Airdrop Refunded", description=f"This airdrop was refunded to {ctx.message.author.mention} because the bot was scheduled for maintenance!", color=red)
      await msg.edit(embed=embed)
      member = ctx.message.author
      channel = await member.create_dm()
      embed = E(title=f"Airdrop Refunded", description=f"{ctx.message.author.mention}, your airdrop of **{round(amount, 6)} {currency}** has been refunded since the bot was scheduled for maintenance!", color=blue)
      await channel.send(embed=embed)
      inventory = opendb()
      inventory[drop_id][str(currency)]['amt'] += amount
      savedb(inventory)
      pending_trxs -= 1
      return
  new_msg = await ctx.channel.fetch_message(msg.id)
  users = await new_msg.reactions[0].users().flatten()
  winners = []


  try:
    for user in users:
      if int(user.id) == 869390064172552192:
        pass
      elif int(user.id) == 909016596180246540:
        pass
      elif user.id == ctx.message.author.id:
        pass  
      elif user not in winners:
          winners.append(str(user.id))
  except:
    pass
  pool = 0
  indexposition = 0
  for wn in winners:
    indexposition += 1
  if indexposition == 0:
    embed = E(title=f"{sad} Nobody reacted to this airdrop", description=f"This airdrop of **{round(amount, 6)} {currency} ** has ended!", color=red)
    inventory = opendb()
    inventory[drop_id][str(currency)]['amt'] += float(amount)
    savedb(inventory)
    pending_trxs -= 1
    await msg.edit(embed=embed)
    return
  reward_ids = []
  for winner in winners:
    if winner not in reward_ids:
      pool += 1
      reward_ids.append(winner)
    else:
      pass
  amount = float(amount)
  amt_add =  amount
  pool = int(pool)
  full_share = amount / pool
  full_share = float(full_share)
  if (full_share * pool) > amount:
      embed = E(title=f"{sad} Airdrop Refunded", description=f"This airdrop was refunded to {ctx.message.author.mention} because the bot was scheduled for maintenance!", color=red)
      await msg.edit(embed=embed)
      member = ctx.message.author
      channel = await member.create_dm()
      embed = E(title=f"Airdrop Refunded", description=f"{ctx.message.author.mention}, your airdrop of **{round(amount, 6)} {currency}** has been refunded since the bot came across a rounding error, please report this to a developer!", color=blue)
      await channel.send(embed=embed)
      inventory = opendb()
      inventory[drop_id][str(currency)]['amt'] += amount
      savedb(inventory)
      pending_trxs -= 1
      return
  full_share = decimal.Decimal(full_share)
  if currency.lower() == "jolt":
    dollaramte = (round(float(float(full_share) * jltPrice), 6))
  elif currency.lower() == "joltclassic":
    dollaramte = (round(float(float(full_share) * jlcPrice), 6))
  elif currency.lower() == "jlc":
    dollaramte = (round(float(float(full_share) * jlcPrice), 6))
  elif currency.lower() == "bnb":
    dollaramte = (round(float(float(full_share) * bnbPrice), 6))
  elif currency.lower() == "capt":
    dollaramte = (round(float(float(full_share) * captPrice), 6))
  elif currency.lower() == "jlt":
    dollaramte = (round(float(float(full_share) * jltPrice), 6))
  elif currency.lower() == "busd":
    dollaramte = (round(float(float(full_share) * busdPrice), 6))
  elif currency.lower() == "shiba":
    dollaramte = (round(float(float(full_share) * shibaPrice), 6))
  elif currency.lower() == "kitsune":
    dollaramte = (round(float(float(full_share) * sinaPrice), 6))
  elif currency.lower() == "glb":
    dollaramte = (round(float(float(full_share) * glbPrice), 6))
  elif currency.lower() == "eth":
    dollaramte = (round(float(float(full_share) * ethPrice), 6))
  elif currency.lower() == "matic":
    dollaramte = (round(float(float(full_share) * maticPrice), 6))
  elif currency.lower() == "nano":
    dollaramte = (round(float(float(full_share) * nanoPrice), 6))
  elif currency.lower() == "st":
    dollaramte = (round(float(float(full_share) * stPrice), 6))
  elif currency.lower() == "btc":
    dollaramte = (round(float(float(full_share) * bitcoinPrice), 6))
  elif currency.lower() == "jet":
    dollaramte = (round(float(float(full_share) * jetokenPrice), 6))
  elif currency.lower() == "mrp":
    dollaramte = (round(float(float(full_share) * morphinePrice), 6))
  reward_people = re.sub(r'(\d+)', r'<@\1>', str(reward_ids))
  reward_people = reward_people.strip("[]") 
  reward_people = reward_people.strip("''")
  reward_people = reward_people.replace(",", "")
  reward_people = reward_people.replace("'", "")
   # '
  embed = E(title=f"{sad} Airdrop Has Ended!", description=f"This airdrop has ended!\n\nCollected By {reward_people}\n\nReward: ${dollaramte:.6f} each", color=blue)
  embed.set_footer(text='Ended:')
  await msg.edit(embed=embed)
  reward_ids = str(reward_ids)
  winner = str(winner)
  rewarded = []
  indexposition = 0

  for winner in winners: 
    ID = str(winner)
    inventory = opendb()
    if ID not in inventory:
      createaccount(ID)
      if ID not in rewarded:
        inventory = opendb()
        inventory[ID][a_bal]["amt"] += float(full_share)
        savedb(inventory)
        rewarded.append(ID)
    else:
      if ID not in rewarded:
        inventory = opendb()
        inventory[ID][a_bal]['amt'] += float(full_share)
        savedb(inventory)
        rewarded.append(ID)
  pending_trxs -= 1
  return



@client.command()
async def ping(ctx):
  embed = E(title='Latency', description=f'Pong! 🏓\nLatency: {round(client.latency * 1000)}ms', color=green)
  await ctx.reply(embed=embed)


@client.command()
async def bstatus(ctx, ID):
  if ctx.message.author.id not in admins:
    return
  blacklist = openblacklist()
  status = blacklist[ID]["blacklisted"]["status"]
  await ctx.send(f"{ID}'s blacklist status is {status}")

@client.group()
async def create(ctx):
  user = ctx.author
  ID = str(user.id)
  inventory = opendb()
  if ID not in inventory:
    createaccount(ID)
    Embed = E(title=f"{check} Account Created", description=f"{ctx.author.mention} Your account has been created.", color=green, timestamp=ctx.message.created_at)
  else:
    Embed = E(title=f"{wrong} You Already Have An Account", description=f"{ctx.author.mention} You already have an account.", color=red)
  await ctx.send(embed=Embed)





@client.group(invoke_without_command=True)
async def disable(ctx):
  if ctx.author.id in admins:
    await ctx.send("Please provide a valid wallet command to disable!")
  else:
      embed = E(title=f"Error", description=f"That is not a valid command!", color=blue)
      await membed.edit(embed=embed)


global disablewithdraws
global disabledeposits
disablewithdraws = False
disabledeposits = False
@disable.command()
async def withdraws(ctx):
  global disablewithdraws
  if ctx.author.id in admins:
    await ctx.send("Disabled withdraws!\nPlease note that they will automatically be enabled when the bot is restarted!")
    disablewithdraws = True

@disable.command()
async def deposits(ctx):
  global disabledeposits
  if ctx.author.id in admins:
    await ctx.send("Disabled depsoits!\nPlease note that they will automatically be enabled when the bot is restarted!")
    disabledeposits = True

@client.command()
async def withdraw(ctx, command=None):
  getliveprices()
  databasebackup()
  walletl = '<:wallet:901189994578841671>'
  b_balance = w3.eth.get_balance("0xD0c08922adEDE10ff42dE72686DEf62c298708c8")
  b_balance = b_balance / 1000000000000000000
  if command == None:
    embed = E(title=f"{wrong} Withdraw", description=f"You must provide a curency to withdraw!", color=red)
    await ctx.reply(embed=embed)
    return
  if float(b_balance) < 0.0009:
    embed = E(title=f"{wrong} withdraws are suspended!", description=f"We are currently experincing some diffuculties with our systems please contact support for more information!", color=red)
    await ctx.send(embed=embed)
    return
  if TRX_lock == True:
    embed = E(title=f"{wrong} Bot preparing for maintenance!", description=f"{ctx.message.author.mention}, This bot is in preperation to restart all further transactions from here on will be blocked untill the bot is restarted! This is a feature we added so we can insure our users that their data will not be lost!", color=red)
    await ctx.send(embed=embed)
    return
  if disablewithdraws == True:
    embed = E(title=f"{wrong} Withdraw", description=f"{ctx.message.author.mention}, the withdraw command is currently under maintainance!", color=red)
    await ctx.send(embed=embed)
    return
  withdrawlogchannel = client.get_channel(905190880850358333)


  #step 5 add withdraws
  if isinstance(ctx.channel, discord.channel.DMChannel):
    id = str(ctx.message.author.id)
    blacklist = openblacklist()
    if id in blacklist:
      b_status = blacklist[id]["blacklisted"]["status"]
      if b_status == True:
        print(f"{ctx.message.author}, ({ctx.message.author.id}) tried to withdraw! BLACKLISTED USER!!!")
        embed = E(title=f"{wrong} Account Blacklisted!", description=f"Your account is locked and under review by administrators! For more info you can join the support server (https://discord.gg/nCtGsxfrAu) or you can run the **.team** command to get the full list of all the moderaters contact information!", color=red)
        await ctx.send(embed=embed)
        return
    inventory = opendb()
    if True:
      gas_fee = "$0.29"
      gas = convertdollarsign(gas_fee, command)


        
    if command.lower() == "jolt" or command.lower() == "jlt":
      #we dont need it to create and account.....
      embed = E(title=f"{walletl} Withdraw Jolt", description=f"Enter the address you want to send the jolt to!", color=blue)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check, timeout=60)
        wal = '0x'
        if wal not in msg.content:
          embed = E(title=f"{wrong} Wallet Error", description=f"The wallet you entered is not valid, please make sure that the wallet you entered is a binance smart chain wallet!", color=red)
          await ctx.send(embed=embed)
          return
        elif len(msg.content) != 42:
          embed = E(title=f"{wrong} Wallet Error", description=f"The wallet you entered is not valid, please make sure that the wallet you entered is a binance smart chain wallet!", color=red)
          await ctx.send(embed=embed)
          return
        wallet = msg.content
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with your wallet address please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      else:
        pass
      embed = E(title="Withdraw Amount", description=f"Please enter the amount of Jolt you want to withdraw!", color=blue)
      await ctx.send(embed=embed)
      def check1(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check1,timeout=60)
        amt_withdrawed = int(msg.content)
        amount = msg.content
        amt = msg.content
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with the amount you want to withdraw please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      if inventory[id]['jlt']['amt'] >= float(amt):
            pass
            
      else:
            embed = E(title=f"{wrong} Fund Error!", description=f"{ctx.message.author.mention}, you do not have enough funds to complete this transaction!", color=red)
            await ctx.send(embed=embed)
            return
      embed = E(title="Confirm Withdraw", description=f"A gas fee will be deducted from your deposit!\nAre you sure you want to confirm this transaction?\n\nAddress: `{wallet}`", color=green)
      embed.add_field(name=f"Withdrawal amount", value=amt_withdrawed)
      embed.add_field(name=f"Fee", value=gas)
      fee = amt_withdrawed + gas
      embed.add_field(name=f'Total', value=fee, inline=False)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check, timeout=60)
        
        if msg.content.lower() == 'no':
          embed = E(title=f"{wrong} Command cancelled", description=f"The withdrawal has been cancelled", color=red)
          await ctx.send(embed=embed)
          return
        elif msg.content.lower() == 'yes':
          
          if inventory[id]['jlt']['amt'] >= float(fee):
            inventory[id]['jlt']['amt'] -= fee
            savedb(inventory)
            
          else:
            embed = E(title=f"{wrong} Fund Error!", description=f"{ctx.message.author.mention}, you do not have enough funds to complete this transaction!", color=red)
            await ctx.send(embed=embed)
            return
        else:
          embed = E(title=f"{wrong} Command cancelled", description=f"The withdrawal has been cancelled", color=red)
          await ctx.send(embed=embed)
          return
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with your answer please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      databasebackup()
      privk = os.environ['privkey']
      contract = w3.eth.contract(w3.toChecksumAddress('0xac19e03d269811a2d837109ff6582da1a4016e9d'), abi=ABI)
      myWallet = "0xD0c08922adEDE10ff42dE72686DEf62c298708c8"
      nonce = w3.eth.get_transaction_count(myWallet)
      amt_withdrawed = int(amt_withdrawed)
      amt_withdrawed = amt_withdrawed * 1000000000000000000
      jolt_txn = contract.functions.transfer(
        wallet,
        amt_withdrawed
      ).buildTransaction({
        'chainId': 56,
        'gas': 70000,
        'gasPrice': w3.toWei('5', 'gwei'),
        'nonce': nonce,
      })     
      
      signed_txn = w3.eth.account.sign_transaction(jolt_txn,private_key=privk)
      hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
      txhashsite = "https://bscscan.com/tx/" + hash.hex()
      embed = E(title=f"Transaction Complete!", description=f"{ctx.message.author.mention}, you have withdrawed {amount} {command} to **{wallet}**!\nTransaction Hash: {txhashsite}", color=green)
      await ctx.send(embed=embed)
      embed = E(title=f"Jolt Withdraw by {ctx.message.author}", description=f"Withdraw Logs\nUserID: {ctx.message.author.id}\nAmount withdrawed: {amt}\nFee Taken: {gas} Jolt\nTotal: {fee}", color=blue)
      withdrawlogchannel.send(embed=embed)
    elif command.lower() == "bnb":
      #we dont need it to create and account.....
      embed = E(title=f"{walletl} Withdraw bnb", description=f"Enter the address you want to send the bnb to!", color=blue)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check, timeout=60)
        wal = '0x'
        
        if wal not in msg.content:
          embed = E(title=f"{wrong} Wallet Error", description=f"The wallet you entered is not valid, please make sure that the wallet you entered is a binance smart chain wallet!", color=red)
          await ctx.send(embed=embed)
          return
        elif len(msg.content) != 42:
          embed = E(title=f"{wrong} Wallet Error", description=f"The wallet you entered is not valid, please make sure that the wallet you entered is a binance smart chain wallet!", color=red)
          await ctx.send(embed=embed)
          return
        wallet = msg.content
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with your wallet address please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      else:
        pass
      embed = E(title="Withdraw Amount", description=f"Please enter the amount of bnb you want to withdraw!", color=blue)
      await ctx.send(embed=embed)
      def check1(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check1,timeout=60)
        amount = float(msg.content)
        amt_withdrawed = amount * 1000000000000000000
        amt_withdrawed = int(amt_withdrawed)
        amt = float(msg.content)

      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with the amount you want to withdraw please rerun the command!", color=red) 
        await ctx.send(embed=embed)
        return
      if amt < 0.0005:
        embed = E(title="Withdraw Error", description=f"You must withdraw at least 0.0005 bnb!", color=red)
        await ctx.send(embed=embed)
        return
      total = amt + gas
      if inventory[id]['bnb']['amt'] >= float(amt):
            pass
            
      else:
            embed = E(title=f"{wrong} Fund Error!", description=f"{ctx.message.author.mention}, you do not have enough funds to complete this transaction!", color=red)
            await ctx.send(embed=embed)
            return
      embed = E(title="Confirm Withdraw", description=f"A network fee will be deducted from your deposit\nAre you sure you want to continue?\n\nAddress:`{wallet}`", color=green)
      embed.add_field(name=f"Withdrawal amount", value=amount)
      embed.add_field(name=f"Fee", value=gas)
      embed.add_field(name=f'Total', value=total, inline=False)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check, timeout=60)
        
        if msg.content.lower() == 'no':
          embed = E(title=f"{wrong} Command cancelled", description=f"The withdrawal has been cancelled", color=red)
          await ctx.send(embed=embed)
          return
        elif msg.content.lower() == 'yes':
          
          if inventory[id]['bnb']['amt'] >= float(total):
            inventory[id]['bnb']['amt'] -= total
            savedb(inventory)
          else:
            embed = E(title=f"{wrong} Fund Error!", description=f"{ctx.message.author.mention}, you do not have enough funds to complete this transaction!", color=red)
            await ctx.send(embed=embed)
            return
        else:
          embed = E(title=f"{wrong} Command cancelled", description=f"The withdrawal has been cancelled", color=red)
          await ctx.send(embed=embed)
          return
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with your answer please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      
      else:
          databasebackup()
          privk = os.environ['privkey']
          myWallet = "0xD0c08922adEDE10ff42dE72686DEf62c298708c8"
          #this is annoying
          await asyncio.sleep(1)

          signed_txn = w3.eth.account.sign_transaction(dict(
            nonce=w3.eth.get_transaction_count(myWallet),
              chainId=56,
              gasPrice= w3.toWei('5', 'gwei'),
              gas=70000,
              to=wallet,
              value=amt_withdrawed, 
              data=b'',
              ),
            privk,
          )
          hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
          txhashsite = "https://bscscan.com/tx/" + hash.hex()
          embed = E(title=f"Transaction Complete!", description=f"{ctx.message.author.mention}, you have withdrawed {amount} {command} to **{wallet}**!\nTransaction Hash: {txhashsite}", color=green)
          await ctx.send(embed=embed)
          embed = E(title=f"Bnb Withdraw by {ctx.message.author}", description=f"Withdraw Logs\nUserID: {ctx.message.author.id}\nAmount withdrawed: {amt}\nFee Taken: {gas} bnb\nTotal: {fee}", color=blue)


          await withdrawlogchannel.send(embed=embed)

    elif command.lower() == "globe" or command.lower() == "glb":
      embed = E(title=f"{walletl} Withdraw Globe!", description=f"Enter the address you want to send the globe to!", color=blue)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check, timeout=60)
        wal = '0x'
        
        if wal not in msg.content:
          embed = E(title=f"{wrong} Wallet Error", description=f"The wallet you entered is not valid, please make sure that the wallet you entered is a binance smart chain wallet!", color=red)
          await ctx.send(embed=embed)
          return
        elif len(msg.content) != 42:
          embed = E(title=f"{wrong} Wallet Error", description=f"The wallet you entered is not valid, please make sure that the wallet you entered is a binance smart chain wallet!", color=red)
          await ctx.send(embed=embed)
          return
        wallet = msg.content
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with your wallet address please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      else:
        pass
      embed = E(title="Withdraw Amount", description=f"Please enter the amount of Globe you want to withdraw!", color=blue)
      await ctx.send(embed=embed)
      def check1(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check1,timeout=60)
        amt = msg.content
        amt_withdrawed = msg.content
        amount = msg.content
        amount = float(amount)
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with the amount you want to withdraw please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      if inventory[id]['glb']['amt'] >= float(amt):
            pass
            
      else:
            embed = E(title=f"{wrong} Fund Error!", description=f"{ctx.message.author.mention}, you do not have enough funds to complete this transaction!", color=red)
            await ctx.send(embed=embed)
            return
      embed = E(title="Confirm Withdraw", description=f"A gas fee will be deducted from your deposit!\nAre you sure you want to confirm this transaction?\n\nAddress: `{wallet}`", color=green)
      embed.add_field(name=f"Withdrawal amount", value=amount)
      embed.add_field(name=f"Fee", value=f'{gas} GLOBE')
      fee = amount + gas
      embed.add_field(name=f'Total', value=fee, inline=False)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check, timeout=60)
        
        if msg.content.lower() == 'no':
          embed = E(title=f"{wrong} Command cancelled", description=f"The withdrawal has been cancelled", color=red)
          await ctx.send(embed=embed)
          return
        elif msg.content.lower() == 'yes':
          
          if inventory[id]['glb']['amt'] >= float(fee):
            inventory[id]['glb']['amt'] -= fee
            savedb(inventory)
          else:
            embed = E(title=f"{wrong} Fund Error!", description=f"{ctx.message.author.mention}, you do not have enough funds to complete this transaction!", color=red)
            await ctx.send(embed=embed)
            return
        else:
          embed = E(title=f"{wrong} Command cancelled", description=f"The withdrawal has been cancelled", color=red)
          await ctx.send(embed=embed)
          return
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with your answer please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      databasebackup()
      privk = os.environ['privkey']
      contract = w3.eth.contract(w3.toChecksumAddress('0xf46b841f9367f5ff559c8670617129452607e722'), abi=ABI)
      myWallet = "0xD0c08922adEDE10ff42dE72686DEf62c298708c8"
      nonce = w3.eth.get_transaction_count(myWallet)
      amt_withdrawed = int(amt_withdrawed)
      amt_withdrawed = amt_withdrawed * 1000000000000000000
      jolt_txn = contract.functions.transfer(
        wallet,
        amt_withdrawed
      ).buildTransaction({
        'chainId': 56,
        'gas': 70000,
        'gasPrice': w3.toWei('5', 'gwei'),
        'nonce': nonce,
      })     
      signed_txn = w3.eth.account.sign_transaction(jolt_txn,private_key=privk)
      hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
      txhashsite = "https://bscscan.com/tx/" + hash.hex()
      embed = E(title=f"Transaction Complete!", description=f"{ctx.message.author.mention}, you have withdrawed {amount} {command} to **{wallet}**!\nTransaction Hash: {txhashsite}", color=green)
      await ctx.send(embed=embed)
      embed = E(title=f"Globe Withdraw by {ctx.message.author}", description=f"Withdraw Logs\nUserID: {ctx.message.author.id}\nAmount withdrawed: {amt}\nFee Taken: {gas} Globe\nTotal: {fee}", color=blue)
      await withdrawlogchannel.send(embed=embed)
    elif command.lower() == "kitsune":
      embed = E(title=f"{walletl} Withdraw Kitsune!", description=f"Enter the address you want to send the kitsune to!", color=blue)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check, timeout=60)
        wal = '0x'
        
        if wal not in msg.content:
          embed = E(title=f"{wrong} Wallet Error", description=f"The wallet you entered is not valid, please make sure that the wallet you entered is a binance smart chain wallet!", color=red)
          await ctx.send(embed=embed)
          return
        elif len(msg.content) != 42:
          embed = E(title=f"{wrong} Wallet Error", description=f"The wallet you entered is not valid, please make sure that the wallet you entered is a binance smart chain wallet!", color=red)
          await ctx.send(embed=embed)
          return
        wallet = msg.content
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with your wallet address please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      else:
        pass
      if inventory[id]['sina']['amt'] >= float(amt):
            pass
            
      else:
            embed = E(title=f"{wrong} Fund Error!", description=f"{ctx.message.author.mention}, you do not have enough funds to complete this transaction!", color=red)
            await ctx.send(embed=embed)
            return
      embed = E(title="Withdraw Amount", description=f"Please enter the amount of Kitsune you want to withdraw!", color=blue)
      await ctx.send(embed=embed)
      def check1(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check1,timeout=60)
        amt_withdrawed = msg.content
        amount = msg.content
        amount = float(amount)
        amt = msg.content
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with the amount you want to withdraw please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      embed = E(title="Confirm Withdraw", description=f"A gas fee will be deducted from your deposit!\nAre you sure you want to confirm this transaction?\n\nAddress: `{wallet}`", color=green)
      embed.add_field(name=f"Withdrawal amount", value=amount)
      embed.add_field(name=f"Fee", value=gas)
      fee = amount + gas
      embed.add_field(name=f'Total', value=fee, inline=False)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check, timeout=60)
        
        if msg.content.lower() == 'no':
          embed = E(title=f"{wrong} Command cancelled", description=f"The withdrawal has been cancelled", color=red)
          await ctx.send(embed=embed)
          return
        elif msg.content.lower() == 'yes':
          
          if inventory[id]['sina']['amt'] >= float(fee):
            inventory[id]['sina']['amt'] -= fee
            savedb(inventory)
          else:
            embed = E(title=f"{wrong} Fund Error!", description=f"{ctx.message.author.mention}, you do not have enough funds to complete this transaction!", color=red)
            await ctx.send(embed=embed)
            return
        else:
          embed = E(title=f"{wrong} Command cancelled", description=f"The withdrawal has been cancelled", color=red)
          await ctx.send(embed=embed)
          return
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with your answer please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      databasebackup()
      privk = os.environ['privkey']
      contract = w3.eth.contract(w3.toChecksumAddress('0x66aFC53B499701f963548A578F990e3c528e2048'), abi=ABI)
      myWallet = "0xD0c08922adEDE10ff42dE72686DEf62c298708c8"
      nonce = w3.eth.get_transaction_count(myWallet)
      amt_withdrawed = int(amt_withdrawed)
      amt_withdrawed = amt_withdrawed * 1000000000000000000
      jolt_txn = contract.functions.transfer(
        wallet,
        amt_withdrawed
      ).buildTransaction({
        'chainId': 56,
        'gas': 70000,
        'gasPrice': w3.toWei('5', 'gwei'),
        'nonce': nonce,
      })     
      signed_txn = w3.eth.account.sign_transaction(jolt_txn,private_key=privk)
      hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
      txhashsite = "https://bscscan.com/tx/" + hash.hex()
      embed = E(title=f"Transaction Complete!", description=f"{ctx.message.author.mention}, you have withdrawed {amount} {command} to **{wallet}**!\nTransaction Hash: {txhashsite}", color=green)
      await ctx.send(embed=embed)
      embed = E(title=f"Kitsune Withdraw by {ctx.message.author}", description=f"Withdraw Logs\nUserID: {ctx.message.author.id}\nAmount withdrawed: {amt}\nFee Taken: {gas} Kitsune\nTotal: {fee}", color=blue)
      await withdrawlogchannel.send(embed=embed)
    elif command.lower() == "jlc" or command.lower() == "joltclassic":
      embed = E(title=f"{walletl} Withdraw Jolt Classic!", description=f"Enter the address you want to send the Jolt Classic to!", color=blue)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check, timeout=60)
        wal = '0x'
        
        if wal not in msg.content:
          embed = E(title=f"{wrong} Wallet Error", description=f"The wallet you entered is not valid, please make sure that the wallet you entered is a binance smart chain wallet!", color=red)
          await ctx.send(embed=embed)
          return
        elif len(msg.content) != 42:
          embed = E(title=f"{wrong} Wallet Error", description=f"The wallet you entered is not valid, please make sure that the wallet you entered is a binance smart chain wallet!", color=red)
          await ctx.send(embed=embed)
          return
        wallet = msg.content
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with your wallet address please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      else:
        pass
      if inventory[id]['jlc']['amt'] >= float(amt):
            pass
            
      else:
            embed = E(title=f"{wrong} Fund Error!", description=f"{ctx.message.author.mention}, you do not have enough funds to complete this transaction!", color=red)
            await ctx.send(embed=embed)
            return
      embed = E(title="Withdraw Amount", description=f"Please enter the amount of Jolt Classic you want to withdraw!", color=blue)
      await ctx.send(embed=embed)
      def check1(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check1,timeout=60)
        amt_withdrawed = msg.content
        amount = msg.content
        amount = float(amount)
        amt = msg.content
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with the amount you want to withdraw please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      embed = E(title="Confirm Withdraw", description=f"A gas fee will be deducted from your deposit!\nAre you sure you want to confirm this transaction?\n\nAddress: `{wallet}`", color=green)
      embed.add_field(name=f"Withdrawal amount", value=amount)
      embed.add_field(name=f"Fee", value=gas)
      fee = amount + gas
      embed.add_field(name=f'Total', value=fee, inline=False)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check, timeout=60)
        
        if msg.content.lower() == 'no':
          embed = E(title=f"{wrong} Command cancelled", description=f"The withdrawal has been cancelled", color=red)
          await ctx.send(embed=embed)
          return
        elif msg.content.lower() == 'yes':
          
          if inventory[id]['jlc']['amt'] >= float(fee):
            inventory[id]['jlc']['amt'] -= fee
            savedb(inventory)
          else:
            embed = E(title=f"{wrong} Fund Error!", description=f"{ctx.message.author.mention}, you do not have enough funds to complete this transaction!", color=red)
            await ctx.send(embed=embed)
            return
        else:
          embed = E(title=f"{wrong} Command cancelled", description=f"The withdrawal has been cancelled", color=red)
          await ctx.send(embed=embed)
          return
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with your answer please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      databasebackup()
      privk = os.environ['privkey']
      contract = w3.eth.contract(w3.toChecksumAddress('0x59b31ab138f895330337d7fb41ed0d79ae8763e0'), abi=ABI)
      myWallet = "0xD0c08922adEDE10ff42dE72686DEf62c298708c8"
      nonce = w3.eth.get_transaction_count(myWallet)
      amt_withdrawed = int(amt_withdrawed)
      amt_withdrawed = amt_withdrawed * 1000000000000000000
      jolt_txn = contract.functions.transfer(
        wallet,
        amt_withdrawed
      ).buildTransaction({
        'chainId': 56,
        'gas': 70000,
        'gasPrice': w3.toWei('5', 'gwei'),
        'nonce': nonce,
      })     
      signed_txn = w3.eth.account.sign_transaction(jolt_txn,private_key=privk)
      hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
      txhashsite = "https://bscscan.com/tx/" + hash.hex()
      embed = E(title=f"Transaction Complete!", description=f"{ctx.message.author.mention}, you have withdrawed {amount} {command} to **{wallet}**!\nTransaction Hash: {txhashsite}", color=green)
      await ctx.send(embed=embed)
      embed = E(title=f"Jolt Classic Withdraw by {ctx.message.author}", description=f"Withdraw Logs\nUserID: {ctx.message.author.id}\nAmount withdrawed: {amt}\nFee Taken: {gas} Jolt Classic\nTotal: {fee}", color=blue)
      await withdrawlogchannel.send(embed=embed)
    elif command.lower() == "busd" or command.lower() == "binanceusd":
      embed = E(title=f"{walletl} Withdraw Busd!", description=f"Enter the address you want to send the Busd to!", color=blue)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check, timeout=60)
        wal = '0x'
        
        if wal not in msg.content:
          embed = E(title=f"{wrong} Wallet Error", description=f"The wallet you entered is not valid, please make sure that the wallet you entered is a binance smart chain wallet!", color=red)
          await ctx.send(embed=embed)
          return
        elif len(msg.content) != 42:
          embed = E(title=f"{wrong} Wallet Error", description=f"The wallet you entered is not valid, please make sure that the wallet you entered is a binance smart chain wallet!", color=red)
          await ctx.send(embed=embed)
          return
        wallet = msg.content
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with your wallet address please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      else:
        pass
      if inventory[id]['busd']['amt'] >= float(amt):
            pass
            
      else:
            embed = E(title=f"{wrong} Fund Error!", description=f"{ctx.message.author.mention}, you do not have enough funds to complete this transaction!", color=red)
            await ctx.send(embed=embed)
            return
      embed = E(title="Withdraw Amount", description=f"Please enter the amount of BUSD you want to withdraw!", color=blue)
      await ctx.send(embed=embed)
      def check1(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check1,timeout=60)
        amt_withdrawed = msg.content
        dep_amt = msg.content
        dep_amt = dep_amt * 1000000000000000000
        dep_amt = int(dep_amt)
        amount = msg.content
        amt = msg.content
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with the amount you want to withdraw please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      embed = E(title="Confirm Withdraw", description=f"A gas fee will be deducted from your deposit!\nAre you sure you want to confirm this transaction?\n\nAddress: `{wallet}`", color=green)
      embed.add_field(name=f"Withdrawal amount", value=amt)
      embed.add_field(name=f"Fee", value=gas)
      fee = float(amt + gas)
      embed.add_field(name=f'Total', value=fee, inline=False)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check, timeout=60)
        
        if msg.content.lower() == 'no':
          embed = E(title=f"{wrong} Command cancelled", description=f"The withdrawal has been cancelled", color=red)
          await ctx.send(embed=embed)
          return
        elif msg.content.lower() == 'yes':
          
          if inventory[id]['busd']['amt'] >= float(fee):
            inventory[id]['busd']['amt'] -= fee
            savedb(inventory)
          else:
            embed = E(title=f"{wrong} Fund Error!", description=f"{ctx.message.author.mention}, you do not have enough funds to complete this transaction!", color=red)
            await ctx.send(embed=embed)
            return
        else:
          embed = E(title=f"{wrong} Command cancelled", description=f"The withdrawal has been cancelled", color=red)
          await ctx.send(embed=embed)
          return
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with your answer please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      databasebackup()
      privk = os.environ['privkey']
      contract = w3.eth.contract(w3.toChecksumAddress('0xe9e7cea3dedca5984780bafc599bd69add087d56'), abi=ABI)
      myWallet = "0xD0c08922adEDE10ff42dE72686DEf62c298708c8"
      nonce = w3.eth.get_transaction_count(myWallet)
      jolt_txn = contract.functions.transfer(
        wallet,
        dep_amt
      ).buildTransaction({
        'chainId': 56,
        'gas': 70000,
        'gasPrice': w3.toWei('5', 'gwei'),
        'nonce': nonce,
      })     
      signed_txn = w3.eth.account.sign_transaction(jolt_txn,private_key=privk)
      hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
      txhashsite = "https://bscscan.com/tx/" + hash.hex()
      embed = E(title=f"Transaction Complete!", description=f"{ctx.message.author.mention}, you have withdrawed {amount} {command} to **{wallet}**!\nTransaction Hash: {txhashsite}", color=green)
      await ctx.send(embed=embed)
      embed = E(title=f"Busd Withdraw by {ctx.message.author}", description=f"Withdraw Logs\nUserID: {ctx.message.author.id}\nAmount withdrawed: {amt}\nFee Taken: {gas} Busd\nTotal: {fee}", color=blue)
      await withdrawlogchannel.send(embed=embed)



    elif command.lower() == "st" or command.lower() == "slicktoken":
      await ctx.send("Slicktoken Withdraws are no longer supported!")
      return
      embed = E(title=f"{walletl} Withdraw ST", description=f"Enter the address you want to send the Slick to!", color=blue)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check, timeout=60)
        wal = '0x'
        if wal not in msg.content:
          embed = E(title=f"{wrong} Wallet Error", description=f"The wallet you entered is not valid, please make sure that the wallet you entered is a binance smart chain wallet!", color=red)
          await ctx.send(embed=embed)
          return
        elif len(msg.content) != 42:
          embed = E(title=f"{wrong} Wallet Error", description=f"The wallet you entered is not valid, please make sure that the wallet you entered is a binance smart chain wallet!", color=red)
          await ctx.send(embed=embed)
          return
        wallet = msg.content
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with your wallet address please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      else:
        pass
      embed = E(title="Withdraw Amount", description=f"Please enter the amount of Slick Token you want to withdraw!", color=blue)
      await ctx.send(embed=embed)
      def check1(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check1,timeout=60)
        amt_withdrawed = int(msg.content)
        amount = msg.content
        amt = msg.content
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with the amount you want to withdraw please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      if inventory[id]['st']['amt'] >= float(amt):
            pass
            
      else:
            embed = E(title=f"{wrong} Fund Error!", description=f"{ctx.message.author.mention}, you do not have enough funds to complete this transaction!", color=red)
            await ctx.send(embed=embed)
            return
      embed = E(title="Confirm Withdraw", description=f"A gas fee will be deducted from your deposit!\nAre you sure you want to confirm this transaction?\n\nAddress: `{wallet}`", color=green)
      embed.add_field(name=f"Withdrawal amount", value=amt_withdrawed)
      embed.add_field(name=f"Fee", value=f"{gas} slick")
      fee = int(amt_withdrawed) + int(gas)
      embed.add_field(name=f'Total', value=f"{fee} slick", inline=False)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check, timeout=240)
        
        if msg.content.lower() == 'no':
          embed = E(title=f"{wrong} Command cancelled", description=f"The withdrawal has been cancelled", color=red)
          await ctx.send(embed=embed)
          return
        elif msg.content.lower() == 'yes':
          
          if inventory[id]['st']['amt'] >= float(fee):
            inventory[id]['st']['amt'] -= fee
            savedb(inventory)
          else:
            embed = E(title=f"{wrong} Fund Error!", description=f"{ctx.message.author.mention}, you do not have enough funds to complete this transaction!", color=red)
            await ctx.send(embed=embed)
            return
        else:
          embed = E(title=f"{wrong} Command cancelled", description=f"The withdrawal has been cancelled", color=red)
          await ctx.send(embed=embed)
          return
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with your answer please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      databasebackup()
      privk = os.environ['privkey']
      contract = w3.eth.contract(w3.toChecksumAddress('0xd8320e3e5913b6acfaab9847ac391103ad0779e2'), abi=ABI)
      myWallet = "0xD0c08922adEDE10ff42dE72686DEf62c298708c8"
      nonce = w3.eth.get_transaction_count(myWallet)
      amt_withdrawed = int(amt_withdrawed)
      amt_withdrawed = amt_withdrawed * 10000000
      jolt_txn = contract.functions.transfer(
        wallet,
        amt_withdrawed
      ).buildTransaction({
        'chainId': 56,
        'gas': 70000,
        'gasPrice': w3.toWei('5', 'gwei'),
        'nonce': nonce,
      })     
      
      signed_txn = w3.eth.account.sign_transaction(jolt_txn,private_key=privk)
      hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
      txhashsite = "https://bscscan.com/tx/" + hash.hex()
      embed = E(title=f"Transaction Complete!", description=f"{ctx.message.author.mention}, you have withdrawed {amount} {command} to **{wallet}**!\nTransaction Hash: {txhashsite}", color=green)
      await ctx.send(embed=embed)
      embed = E(title=f"Slick Withdraw by {ctx.message.author}", description=f"Withdraw Logs\nUserID: {ctx.message.author.id}\nAmount withdrawed: {amt}\nFee Taken: {gas} Slick Token\nTotal: {fee}", color=blue)
      withdrawlogchannel = client.get_channel(905190880850358333)
      await withdrawlogchannel.send(embed=embed)
    elif command.lower() == "jet" or command.lower() == "jetoken":
      await ctx.send("Jetoken Withdraws are still being configured!")
      return



    elif command.lower() == "morphine" or command.lower() == "mrp":
      embed = E(title=f"{walletl} Withdraw MRP!", description=f"Enter the address you want to send the MRP to!", color=blue)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check, timeout=60)
        wal = '0x'
        
        if wal not in msg.content:
          embed = E(title=f"{wrong} Wallet Error", description=f"The wallet you entered is not valid, please make sure that the wallet you entered is a binance smart chain wallet!", color=red)
          await ctx.send(embed=embed)
          return
        elif len(msg.content) != 42:
          embed = E(title=f"{wrong} Wallet Error", description=f"The wallet you entered is not valid, please make sure that the wallet you entered is a binance smart chain wallet!", color=red)
          await ctx.send(embed=embed)
          return
        wallet = msg.content
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with your wallet address please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      else:
        pass
      if inventory[id]['mrp']['amt'] >= float(amt):
            pass
            
      else:
            embed = E(title=f"{wrong} Fund Error!", description=f"{ctx.message.author.mention}, you do not have enough funds to complete this transaction!", color=red)
            await ctx.send(embed=embed)
            return
      embed = E(title="Withdraw Amount", description=f"Please enter the amount of MRP you want to withdraw!", color=blue)
      await ctx.send(embed=embed)
      def check1(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check1,timeout=60)
        amt_withdrawed = msg.content
        dep_amt = msg.content
        dep_amt = dep_amt * 1000000000
        dep_amt = int(dep_amt)
        amount = msg.content
        amt = msg.content
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with the amount you want to withdraw please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      embed = E(title="Confirm Withdraw", description=f"A gas fee will be deducted from your deposit!\nAre you sure you want to confirm this transaction?\n\nAddress: `{wallet}`", color=green)
      embed.add_field(name=f"Withdrawal amount", value=amt)
      embed.add_field(name=f"Fee", value=gas)
      fee = float(amt + gas)
      embed.add_field(name=f'Total', value=fee, inline=False)
      await ctx.send(embed=embed)
      def check(m) -> bool:
        return m.author == ctx.author
      try:
        msg = await client.wait_for("message", check=check, timeout=60)
        
        if msg.content.lower() == 'no':
          embed = E(title=f"{wrong} Command cancelled", description=f"The withdrawal has been cancelled", color=red)
          await ctx.send(embed=embed)
          return
        elif msg.content.lower() == 'yes':
          
          if inventory[id]['mrp']['amt'] >= float(fee):
            inventory[id]['mrp']['amt'] -= fee
            savedb(inventory)
          else:
            embed = E(title=f"{wrong} Fund Error!", description=f"{ctx.message.author.mention}, you do not have enough funds to complete this transaction!", color=red)
            await ctx.send(embed=embed)
            return
        else:
          embed = E(title=f"{wrong} Command cancelled", description=f"The withdrawal has been cancelled", color=red)
          await ctx.send(embed=embed)
          return
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Canceled", description=f"You took to long to responed with your answer please rerun the command!", color=red)
        await ctx.send(embed=embed)
        return
      databasebackup()
      privk = os.environ['privkey']
      contract = w3.eth.contract(w3.toChecksumAddress('0xb8608f270497764a10c28bfe75454f68b31ba2b1'), abi=ABI)
      myWallet = "0xD0c08922adEDE10ff42dE72686DEf62c298708c8"
      nonce = w3.eth.get_transaction_count(myWallet)
      jolt_txn = contract.functions.transfer(
        wallet,
        dep_amt
      ).buildTransaction({
        'chainId': 56,
        'gas': 70000,
        'gasPrice': w3.toWei('5', 'gwei'),
        'nonce': nonce,
      })     
      signed_txn = w3.eth.account.sign_transaction(jolt_txn,private_key=privk)
      hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
      txhashsite = "https://bscscan.com/tx/" + hash.hex()
      embed = E(title=f"Transaction Complete!", description=f"{ctx.message.author.mention}, you have withdrawed {amount} {command} to **{wallet}**!\nTransaction Hash: {txhashsite}", color=green)
      await ctx.send(embed=embed)
      embed = E(title=f"MRP Withdraw by {ctx.message.author}", description=f"Withdraw Logs\nUserID: {ctx.message.author.id}\nAmount withdrawed: {amt}\nFee Taken: {gas} MRP\nTotal: {fee}", color=blue)
      await withdrawlogchannel.send(embed=embed)
#ETHEREUM CHAIN _____________________________________________________!!!!!!!!!!!!!!!!!!


  else:
    Embed = E(title=f"{wrong} Messsage Error", description=f"{ctx.author.mention} This command can only be used in direct messages! Please direct message me {prefix}withdraw for this command to work!", color=red)
    await ctx.send(embed=Embed)

def convertusdtocurrency(amount, currency):
  currency = currency.lower()
  amount = str(amount)
  if amount.startswith("$"):
    try:
      amount = amount.lstrip("$")
    except:
      pass
    
    try:
      amount = float(amount)
    except Exception:
      amount = int(amount)
    if currency.lower() == "jolt":
      gas = (float(float(amount) / jltPrice))
      gas = round(gas,6)
    elif currency.lower() == "joltclassic":
      gas = (float(float(amount) / jlcPrice))
      gas = round(gas,6)
    elif currency.lower() == "jlc":
      gas = (float(float(amount) / jlcPrice))
      gas = round(gas,6)
    elif currency.lower() == "bnb":
      gas = (float(float(amount) / bnbPrice))
      gas = round(gas,6)
    elif currency.lower() == "capt":
      gas = (float(float(amount) / captPrice))
      gas = round(gas,6)
    elif currency.lower() == "jlt":
      gas = (float(float(amount) / bnbPrice))
      gas = round(gas,6)
    elif currency.lower() == "busd":
      gas = (float(float(amount) / busdPrice))
      gas = round(gas,6)
    elif currency.lower() == "shiba" or currency.lower() == "shib":
      gas = (float(float(amount) / shibaPrice))
      gas = round(gas,6)
    elif currency.lower() == "kitsune":
      gas = (float(float(amount) / sinaPrice))
      gas = round(gas,6)
    elif currency.lower() == "glb" or currency.lower() == "globe":
      gas = (float(float(amount) / glbPrice))
      gas = round(gas,6)
    elif currency.lower() == "eth":
      gas = (float(float(amount) / ethPrice))
      gas = round(gas, 8)
    elif currency.lower() == "matic":
      gas = (float(float(amount) / maticPrice))
      gas = round(gas,6)
    elif currency.lower() == "nano":
      gas = (float(float(amount) / nanoPrice))
      gas = round(gas,6)
    elif currency.lower() == "st":
      gas = (float(float(amount) / stPrice))
      gas = round(gas,6)
    elif currency.lower() == "jet" or currency.lower() == "jetoken":
      gas = (float(float(amount) / jetokenPrice))
      gas = round(gas,6)
    elif currency.lower() == "mrp" or currency.lower() == "morphine":
      gas = (float(float(amount) / morphinePrice))
      gas = round(gas,6)
  return gas 
def convertcurrencytousd(amount, currency):
  currency = currency.lower()
  try:
    amount = float(amount)
  except:
    amount = int(amount)
  if True:
    if currency.lower() == "jolt":
      dollaramt = (round(float(float(amount) * jltPrice), 6))
    elif currency.lower() == "jlt":
      dollaramt = (round(float(float(amount) * jltPrice), 6))
    elif currency.lower() == "joltclassic":
      dollaramt = (round(float(float(amount) * jlcPrice), 4))
    elif currency.lower() == "jlc":
      dollaramt = (round(float(float(amount) * jlcPrice), 4))
    elif currency.lower() == "bnb":
      dollaramt = (round(float(float(amount) * bnbPrice), 4))
    elif currency.lower() == "capt":
      dollaramt = (round(float(float(amount) * captPrice), 4))
    elif currency.lower() == "shiba" or currency.lower() == "shib":
      dollaramt = (round(float(float(amount) * shibaPrice) , 4))
    elif currency.lower() == "busd":
      dollaramt = (round(float(float(amount) * busdPrice) , 4))
    elif currency.lower() == "glb" or currency.lower() == "globe":
      dollaramt = (round(float(float(amount) * glbPrice) , 4))
    elif currency.lower() == 'globe':
      dollaramt = (round(float(float(amount) * glbPrice) , 4))
    elif currency.lower() == 'nano':
      dollaramt = (round(float(float(amount) * nanoPrice) , 4))
    elif currency.lower() == "kitsune":
      dollaramt = (round(float(float(amount) * sinaPrice), 4))
    elif currency.lower() == "matic":
      dollaramt = (round(float(float(amount) * maticPrice) , 4)) 
    elif currency.lower() == "jet" or currency.lower() == "jetoken":
      dollaramt = (round(float(float(amount) * jetokenPrice) , 4)) 
    elif currency.lower() == "mrp" or currency.lower() == "morphine":
      dollaramt = (round(float(float(amount) * morphinePrice) , 4)) 
  return dollaramt
  
  
  

def convertdollarsign(amount, currency):
  dollar_sign = "$"
  if currency.lower() == "capt":
    amount = "$3.50"
  if currency.lower() == "jet" or currency.lower() == "jetoken":
    amount = "$1.56"
  if currency.lower() == "mrp" or currency.lower() == "morphine":
    amount = "$0.35"
  if dollar_sign in amount:
    amount = amount.lstrip("$")
    amount = float(amount)
    if currency.lower() == "jolt":
      gas = (float(float(amount) / jltPrice))
      gas = round(gas)
    elif currency.lower() == "joltclassic":
      gas = (float(float(amount) / jlcPrice))
      gas = round(gas)
    elif currency.lower() == "jlc":
      gas = (float(float(amount) / jlcPrice))
      gas = round(gas)
    elif currency.lower() == "bnb":
      gas = (float(float(amount) / bnbPrice))
      gas = round(gas, 4)
    elif currency.lower() == "capt":
      gas = (float(float(amount) / captPrice))
      gas = round(gas)
    elif currency.lower() == "jlt":
      gas = (float(float(amount) / jltPrice))
      gas = round(gas)
    elif currency.lower() == "busd":
      gas = (float(float(amount) / busdPrice))
      gas = round(gas, 2)
    elif currency.lower() == "shiba" or currency.lower() == "shib":
      gas = (float(float(amount) / shibaPrice))
      gas = round(gas)
    elif currency.lower() == "kitsune":
      gas = (float(float(amount) / sinaPrice))
      gas = round(gas, 2)
    elif currency.lower() == "glb" or currency.lower() == "globe":
      gas = (float(float(amount) / glbPrice))
      gas = round(gas)
    elif currency.lower() == "eth":
      gas = (float(float(amount) / ethPrice))
      gas = round(gas, 8)
    elif currency.lower() == "matic":
      gas = (float(float(amount) / maticPrice))
      gas = round(gas, 5)
    elif currency.lower() == "nano":
      gas = (float(float(amount) / nanoPrice))
      gas = round(gas, 5)
    elif currency.lower() == "st":
      gas = (float(float(amount) / stPrice))
      gas = round(gas)
    elif currency.lower() == "jet" or currency.lower() == "jetoken":
      gas = (float(float(amount) / jetokenPrice))
      gas = round(gas)
    elif currency.lower() == "mrp" or currency.lower() == "morphine":
      gas = (float(float(amount) / morphinePrice))
      gas = round(gas)   
  return gas


wallet = '<:wallet:901189994578841671>'
# Jolt_acct_bal / 1000000000000000000 accurate balance
# Step 6 add deposit command
@client.command()
async def deposit(ctx, command=None):
  if command == None:
    embed = E(title=f"{wrong} Deposit", descripiton=f"You must privde a currency to deposit!", color=red)
    await ctx.reply(embed=embed)
    return
  command = command.lower()

  getliveprices()
  databasebackup()
  global gas
  global pending_trxs
  w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
  b_balance = w3.eth.get_balance("0xD0c08922adEDE10ff42dE72686DEf62c298708c8")
  b_balance = b_balance / 1000000000000000000

  if float(b_balance) < 0.0007:
    embed = E(title=f"{wrong} deposits are suspended!", description=f"We are currently experincing some diffuculties with our systems please contact support for more information!", color=red)
    await ctx.send(embed=embed)
    return
  if TRX_lock == True:
    embed = E(title=f"{wrong} Bot preparing for maintenance!", descripiton=f"{ctx.message.author.mention}, This bot is in preperation to restart all further transactions from here on will be blocked untill the bot is restarted! This is a feature we added so we can insure our users that their data will not be lost!", color=red)
    await ctx.send(embed=embed)
    return
  if disabledeposits == True:
    if ctx.message.author.id not in admins:
      embed = E(title=f"{wrong} Deposits", description=f"{ctx.message.author.mention}, the deposit command is currently under maintainance!", color=red)
      await ctx.send(embed=embed)
      return
    else:
      await ctx.send("Deposits are blocked for regular users but since your an admin we are procceding!")
  id = str(ctx.message.author.id)
  blacklist = openblacklist()
  if id in blacklist:
    b_status = blacklist[id]["blacklisted"]["status"]
    if b_status == True:
      print(f"{ctx.message.author}, ({ctx.message.author.id}) tried to withdraw! BLACKLISTED USER!!!")
      embed = E(title=f"{wrong} Account Blacklisted!", description=f"Your account is locked and under review by administrators! For more info you can join the support server (https://discord.gg/nCtGsxfrAu) or you can run the **.team** command to get the full list of all the moderaters contact information!", color=red)
      await ctx.send(embed=embed)
      return
  if command.lower() in currencies:
    if command.lower() == "jolt":
      dollaramt = (round(float(float(2000000000000) * jltPrice), 6))
    elif command.lower() == "jlt":
      dollaramt = (round(float(float(2000000000000) * jltPrice), 6))
    elif command.lower() == "joltclassic":
      dollaramt = (round(float(float(15) * jlcPrice), 4))
    elif command.lower() == "jlc":
      dollaramt = (round(float(float(15) * jlcPrice), 4))
    elif command.lower() == "bnb":
      dollaramt = (round(float(float(0.000420) * bnbPrice), 4))
    elif command.lower() == "capt":
      dollaramt = (round(float(float(12000000000) * captPrice), 4))
    elif command.lower() == "shiba" or command.lower() == "shib":
      dollaramt = (round(float(float(12000000000) * shibaPrice) , 4))
    elif command.lower() == "busd":
      dollaramt = (round(float(float(0.4) * busdPrice) , 4))
    elif command.lower() == "glb" or command.lower() == "globe":
      dollaramt = (round(float(float(20000) * glbPrice) , 4))
    elif command.lower() == 'globe':
      dollaramt = (round(float(float(20000) * glbPrice) , 4))
    elif command.lower() == "kitsune":
      dollaramt = (round(float(float(250) * sinaPrice), 4))
    elif command.lower() == "matic":
      dollaramt = (round(float(float(0.006) * maticPrice) , 4)) 
    elif command.lower() == "jet" or command.lower() == "jetoken":
      dollaramt = (round(float(float(0.006) * jetokenPrice) , 4)) 
    elif command.lower() == "mrp" or command.lower() == "morphine":
      dollaramt = (round(float(float(0.006) * morphinePrice) , 4)) 
    #add nano
    inventory = opendb()
    if isinstance(ctx.channel, discord.channel.DMChannel):
      
      if id not in inventory:
        createaccount(id)
      gas_fee = "$0.28"
      dollar_sign = "$"
      if command == None:
        Embed = E(title=f"{wrong} Messsage Usage Error", description=f"{ctx.author.mention}, You must choose the currency you want to deposit!\nExample: ```{prefix}dCposit Jlc```", color=red)
        await ctx.send(embed=Embed)
        return
      wallet = '<:wallet:901189994578841671>'
      if True:
        if dollar_sign in gas_fee:
          gas = convertdollarsign(gas_fee, command)
      if command.lower() == "jolt":
        w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
        pending_trxs += 1
        account = w3.eth.account.create()
        Embed = E(title=f"{wallet} Deposit Address", description=f"Trasaction Fee: {gas}  **(~$0.24)** \n```If you send any amount less than the gas fee the Jolt will not be deposited to your account!```\n Deposit address: ```{account.address}```\nNote: You have 45 mins to deposit! If you deposit after that time frame the Jolt wont be credited to your account!", colour=discord.Colour(0x000000))
        await ctx.send(embed=Embed)
        contract = w3.eth.contract(w3.toChecksumAddress('0xac19e03d269811a2d837109ff6582da1a4016e9d'), abi=ABI)
        jolt_account_bal = contract.functions.balanceOf(account.address).call()
        old_account_bal = jolt_account_bal / 1000000000000000000
        loop = 0
        while old_account_bal == old_account_bal:
          jolt_new_account_bal = contract.functions.balanceOf(account.address).call()
          new_account_bal = jolt_new_account_bal / 1000000000000000000
          await asyncio.sleep(1)
          loop += 1
          if loop > 6000:
            await ctx.send("Your time has ran out to deposit JLT (Jolt)!")
            pending_trxs -= 1
            return
          elif new_account_bal > old_account_bal:
            break
        amount_deposited = new_account_bal - old_account_bal
        if amount_deposited > gas:
          amount_deposited_with_fee = amount_deposited - gas
        else:
          eb = E(title=f"{wrong} Deposit Failed", description=f"You have not deposited enough jolt for it to be credited to your account.", color=red)
          await ctx.send(embed=eb)
          return
        embed = E(title=f"{check} Deposit Detected!", description=f"A Jolt Deposit has been recieved!\nPlease allow up to 7 minutes for the Jolt deposit to confirm and to be credited to your account!\n\nFull Amount Deposited: {amount_deposited} JLT\nAmount after fees: {amount_deposited_with_fee} JLT", color=blue)

        await ctx.send(embed=embed)  
        await asyncio.sleep(random.randint(240, 420))
        confirm_deposit = contract.functions.balanceOf(account.address).call()
        confirm_deposit = confirm_deposit / 1000000000000000000
        if confirm_deposit == new_account_bal:
          pass
        else:
          embed=E(title=f"{wrong} Deposit Refunded", description=f"It seems like you refunded the deposit for {amount_deposited} JLT!", color=red)
          await ctx.send(embed=embed)
          return
        inventory[id]['jlt']['amt'] += amount_deposited_with_fee
        savedb(inventory) #done ok that's all i needed
        await asyncio.sleep(5)
        
        Embed = E(title=f"Transaction Complete!", description=f"{ctx.author.mention}, Transaction Complete!\nJolt Added to Account: {amount_deposited_with_fee}!", color=green)
        await ctx.send(embed=Embed)
        #automated Transaction
        databasebackup()
        privk = os.environ['privkey']
        signed_txn = w3.eth.account.sign_transaction(dict(
            nonce=w3.eth.get_transaction_count('0xD0c08922adEDE10ff42dE72686DEf62c298708c8'),
            chainId=56,
            gasPrice= w3.toWei('5', 'gwei'),
            gas=70000,
            to=account.address,
            value=490000000000000, # 0.00069 bnb
            data=b'',
            ),
          privk,
        )

        hash = w3.eth.send_raw_transaction  (signed_txn.rawTransaction)
        if True:
          await asyncio.sleep(60)
          myWallet = account.address
          toSend = "0xD0c08922adEDE10ff42dE72686DEf62c298708c8"
          nonce = w3.eth.get_transaction_count(myWallet)
          amount = amount_deposited * 1000000000000000000
          real_amt = int(amount)
        
          jolt_txn = contract.functions.transfer(
            toSend,
            real_amt
          ).buildTransaction({
            'chainId': 56,
            'gas': 70000,
            'gasPrice': w3.toWei('5', 'gwei'),
            'nonce': nonce,
          })
          privKeyy = account.privateKey
          signed_txn = w3.eth.account.sign_transaction(jolt_txn,private_key=privKeyy)
          depositlogschannel = client.get_channel(905190880850358333)
          hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
          
          txhashsite = "https://bscscan.com/tx/" + hash.hex()
          fee_taken = 1500000000000
          embed = E(title=f"{ctx.message.author}, Deposited Jolt!", description=f"Depsoit Amount: {amount_deposited}\nUserID: {ctx.message.author.id}\nTransaction Hash: {(txhashsite)}\nFee Taken: {gas} Jolt", color=blue)
          await depositlogschannel.send(embed=embed)
          pending_trxs -= 1
          return
      elif command.lower() == "bnb":
        await ctx.send("Bnb deposits are currently being worked on!")
        return
        pending_trxs += 1
        w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
        account = w3.eth.account.create()
        Embed = E(title=f"{wallet} Deposit Address", description=f"Gas Fee: {gas} bnb **(~$0.24)** \n```If you send any amount less than the gas fee listed above the BNB will not be deposited to your account!```\n Deposit address: ```{account.address}```\nNote: You have 45 mins to deposit! If you deposit after that time frame the bnb wont be credited to your account!", colour=discord.Colour(0xe8d552))
        await ctx.send(embed=Embed)
        old_bal = w3.eth.get_balance(account.address)
        loop = 0
        while old_bal == old_bal:
          await asyncio.sleep(1)
          loop+=1 
          new_bal = w3.eth.get_balance(account.address)
          if old_bal != new_bal:
            break
          elif loop > 6000:
            await ctx.send("Your time has ran out to deposit BNB!")
            pending_trxs -= 1
            return
        amount_deposited = new_bal
        deposit_amt = new_bal - old_bal
        if deposit_amt < gas: # c
          eb = E(title=f"{wrong} Deposit Failed", description=f"You have not deposited enough BNB for it to be credited to your account. Amount deposited: {deposit_amt}", color=red)
          await ctx.send(embed=eb)
          pending_trxs -= 1
          return 
        else:
          embed = E(title=f"{check} Deposit Detected!", description=f"A BNB Deposit has been recieved!\nPlease allow up to 7 minutes for the BNB deposit to confirm and to be credited to your account!\n\nFull Amount Deposited: {round(amount_deposited / 1000000000000000000, 5)} BNB\nAmount after fees: {round(deposit_amt / 1000000000000000000, 5)} BNB", color=blue)

          await ctx.send(embed=embed)
          await asyncio.sleep(random.randint(240, 420))
          confirm_deposit = w3.eth.get_balance(account.address)
          if confirm_deposit == amount_deposited:
            pass
          else:
            embed=E(title=f"{wrong} Deposit Refunded", description=f"It seems like you refunded the deposit for {amount_deposited} BNB!", color=red)
            await ctx.send(embed=embed)
            return
          inventory = opendb()
          id = str(ctx.message.author.id)
          deposit_amt_with_fee = deposit_amt - gas # what do you need help with?
          deposit_amt_with_fee_full = deposit_amt_with_fee / 1000000000000000000
          inventory[id]['bnb']['amt'] += deposit_amt_with_fee_full
          Embed = E(title=f"Transaction Complete!", description=f"{ctx.author.mention}, Transaction Complete!\nBNB Added to Account: {round(deposit_amt_with_fee_full, 5)}!", color=green)
          await ctx.send(embed=Embed)
          savedb(inventory)
          databasebackup()
          privky = account.privateKey
          deposit_amt = "{:.7f}".format(deposit_amt)
          send = deposit_amt * 1000000000000000000
          
          send_full = send - 0.001

          tomainwallet = '0xD0c08922adEDE10ff42dE72686DEf62c298708c8'
          signed_txn = w3.eth.account.sign_transaction(dict(
                nonce=w3.eth.get_transaction_count(account.address),
                chainId=56,
                gasPrice= w3.toWei('5', 'gwei'),
                gas=70000,
                to=tomainwallet,
                value=send_full,
                data=b'',
              ),
            privky,
          )
          privKeyy = account.privateKey # use this in to save the funds in case it doesnt work
          signed_txn = w3.eth.account.sign_transaction(signed_txn,private_key=privKeyy)
          depositlogschannel = client.get_channel(905190880850358333)
          hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
          txhashsite = "https://bscscan.com/tx/" + hash.hex()
          fee_taken = 0.000420
          embed = E(title=f"{ctx.message.author}, Deposited BNB!", description=f"Depsoit Amount: {round(amount_deposited, 5)}\nUserID: {ctx.message.author.id}\nTransaction Hash: {(txhashsite)}\nFee Taken: {fee_taken} BNB", color=blue)
          await depositlogschannel.send(embed=embed)
          pending_trxs -= 1
          return
      elif command.lower() == "capt":
        pending_trxs += 1
        w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
        contract = w3.eth.contract(w3.toChecksumAddress('0xdf5301b96ceccb9c2a61505b3a7577111056a4c5'), abi=ABI)
        account = w3.eth.account.create()
        Embed = E(title=f"{wallet} Deposit Address", description=f"Gas Fee: {gas} capt **(~$3.50)** \n```If you send any amount less than the gas fee listed above the CAPT will not be deposited to your account!```\n Deposit address: ```{account.address}```\nNote: You have 45 mins to deposit! If you deposit after that time frame the capt wont be credited to your account!", color=blue)
        await ctx.send(embed=Embed)
        old_bal = contract.functions.balanceOf(account.address).call()
        joltc_account_bal = contract.functions.balanceOf(account.address).call()
        old_account_bal = joltc_account_bal / 1000000000000000000 # this is the accurate balance we have to do this to get the correct balance because of the Decimals
        loop = 0
        while old_account_bal == old_account_bal:
          joltc_new_account_bal = contract.functions.balanceOf(account.address).call()
          new_account_bal = joltc_new_account_bal / 1000000000000000000
          await asyncio.sleep(1)
          loop += 1
          if loop > 6000:
            await ctx.send("Your time has ran out to deposit CAPT!")
            pending_trxs -= 1
            return
          if new_account_bal > old_account_bal:
            break
        amount_deposited = new_account_bal - old_account_bal
        if amount_deposited > gas:
          amount_deposited_with_fee = amount_deposited - gas
        else:
          await ctx.send("You did not have enough CAPT to cover the gas fee!\n **The CAPT is unable to be credited to your account! for more information you can contact the bot founder or the admins!**")
          pending_trxs -= 1
          return
        embed = E(title=f"{check} Deposit Detected!", description=f"A CAPT Deposit has been recieved!\nPlease allow up to 7 minutes for the CAPT deposit to confirm and to be credited to your account!\n\nFull Amount Deposited: {amount_deposited} CAPT\nAmount after fees: {amount_deposited_with_fee} CAPT", color=blue)

        await ctx.send(embed=embed)
        await asyncio.sleep(random.randint(240, 420))
        confirm_deposit = contract.functions.balanceOf(account.address).call()
        confirm_deposit = confirm_deposit / 1000000000000000000
        if confirm_deposit == new_account_bal:
          pass
        else:
          embed=E(title=f"{wrong} Deposit Refunded", description=f"It seems like you refunded the deposit for {amount_deposited} CAPT!", color=red)
          await ctx.send(embed=embed)
          return
        inventory[id]['capt']['amt'] += amount_deposited_with_fee
        savedb(inventory)
        databasebackup()
        dollaramt = (round(float(float(amount_deposited_with_fee) * captPrice), 6))
        await asyncio.sleep(5)
        Embed = E(title=f"{check}Transaction Complete!", description=f"{ctx.author.mention}, Transaction Complete!\n{amount_deposited_with_fee} (~${dollaramt}) CAPT has been added to your Account!\n New balance: {inventory[id]['capt']['amt']} CAPT", color=green)
        await ctx.send(embed=Embed)
        privk = os.environ['privkey']
        signed_txn = w3.eth.account.sign_transaction(dict(
            nonce=w3.eth.get_transaction_count('0xD0c08922adEDE10ff42dE72686DEf62c298708c8'),
            chainId=56,
            gasPrice= w3.toWei('5', 'gwei'),
            gas=70000,
            to=account.address,
            value=490000000000000, # 0.00049 bnb
            data=b'',
            ),
          privk,
        )
        hash = w3.eth.send_raw_transaction  (signed_txn.rawTransaction)
        if True:
          await asyncio.sleep(60)
          myWallet = account.address
          toSend = "0xD0c08922adEDE10ff42dE72686DEf62c298708c8" #  hot wallet
          nonce = w3.eth.get_transaction_count(myWallet)
          amount = amount_deposited * 1000000000000000000
          real_amt = int(amount)
          joltc_txn = contract.functions.transfer(
            toSend,
            real_amt
          ).buildTransaction({
            'chainId': 56,
            'gas': 70000,
            'gasPrice': w3.toWei('5', 'gwei'),
            'nonce': nonce,
          })
          privKeyy = account.privateKey
          signed_txn = w3.eth.account.sign_transaction(joltc_txn,private_key=privKeyy)
          depositlogschannel = client.get_channel(905190880850358333)
          hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
          
          txhashsite = "https://bscscan.com/tx/" + hash.hex()
          fee_taken = 20
          embed = E(title=f"{ctx.message.author}, Deposited CAPT!", description=f"Depsoit Amount: {amount_deposited}\nUserID: {ctx.message.author.id}\nTransaction Hash: {(txhashsite)}\nFee Taken: {gas} CAPT", color=blue)
          await depositlogschannel.send(embed=embed)
          pending_trxs -= 1
          return
      elif command.lower() == 'jlc':
        pending_trxs += 1
        w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
        account = w3.eth.account.create() # look here
        Embed = E(title=f"{wallet} Deposit Address", description=f"Gas Fee: {gas} JLC  **(~$0.30)** \n```If you send any amount less than the gas fee listed above the JLC will not be deposited to your account!```\n Deposit address: ```{account.address}```\nNote: You have 45 mins to deposit! If you deposit after that time frame the JLC wont be credited to your account!", color=discord.Colour(0x5C28F4))
        await ctx.send(embed=Embed)
        await ctx.send(account.address)
        contract = w3.eth.contract(w3.toChecksumAddress('0x59b31ab138f895330337d7fb41ed0d79ae8763e0'), abi=ABI)
        joltc_account_bal = contract.functions.balanceOf(account.address).call()
        old_account_bal = joltc_account_bal / 1000000000000000000 # this is the accurate balance we have to do this to get the correct balance because of the Decimals
        loop = 0
        while old_account_bal == old_account_bal:
          joltc_new_account_bal = contract.functions.balanceOf(account.address).call()
          new_account_bal = joltc_new_account_bal / 1000000000000000000
          await asyncio.sleep(1)
          loop += 1
          if loop > 6000:
            await ctx.send("Your time has ran out to deposit JLC!")
            pending_trxs -= 1
            return
          if new_account_bal > old_account_bal:
            break
        amount_deposited = new_account_bal - old_account_bal
        if amount_deposited > gas:
          amount_deposited_with_fee = amount_deposited - gas
        else:
          await ctx.send("You did not have enough JLC to cover the gas fee!\n **The JLC is unable to be credited to your account! for more information you can contact the bot founder or the admins!**")
          pending_trxs -= 1
          return
        embed = E(title=f"{check} Deposit Detected!", description=f"A Jolt Classic Deposit has been recieved!\nPlease allow up to 7 minutes for the Jolt Classic deposit to confirm and to be credited to your account!\n\nFull Amount Deposited: {amount_deposited} JLC\nAmount after fees: {amount_deposited_with_fee} JLC", color=blue)

        await ctx.send(embed=embed)
        await asyncio.sleep(random.randint(240, 420))
        confirm_deposit = contract.functions.balanceOf(account.address).call()
        confirm_deposit = confirm_deposit / 1000000000000000000
        if confirm_deposit == new_account_bal:
          pass
        else:
          embed=E(title=f"{wrong} Deposit Refunded", description=f"It seems like you refunded the deposit for {amount_deposited} JLC!", color=red)
          await ctx.send(embed=embed)
          return
        inventory[id]['jlc']['amt'] += amount_deposited_with_fee
        savedb(inventory)
        databasebackup()
        dollaramt = (round(float(float(amount_deposited_with_fee) * jlcPrice), 6))
        await asyncio.sleep(5)
        Embed = E(title=f"{check}Transaction Complete!", description=f"{ctx.author.mention}, Transaction Complete!\n{amount_deposited_with_fee} (~${dollaramt}) Jolt Classic has been added to your Account!\n New balance: {joltclassic}:{inventory[id]['jlc']['amt']}", color=green)
        await ctx.send(embed=Embed)
        privk = os.environ['privkey']
        signed_txn = w3.eth.account.sign_transaction(dict(
            nonce=w3.eth.get_transaction_count('0xD0c08922adEDE10ff42dE72686DEf62c298708c8'),
            chainId=56,
            gasPrice= w3.toWei('5', 'gwei'),
            gas=70000,
            to=account.address,
            value=490000000000000, # 0.00049 bnb
            data=b'',
            ),
          privk,
        )
        hash = w3.eth.send_raw_transaction  (signed_txn.rawTransaction)
        if True:
          await asyncio.sleep(60)
          myWallet = account.address
          toSend = "0xD0c08922adEDE10ff42dE72686DEf62c298708c8" #  hot wallet
          nonce = w3.eth.get_transaction_count(myWallet)
          amount = amount_deposited * 1000000000000000000
          real_amt = int(amount)
          joltc_txn = contract.functions.transfer(
            toSend,
            real_amt
          ).buildTransaction({
            'chainId': 56,
            'gas': 70000,
            'gasPrice': w3.toWei('5', 'gwei'),
            'nonce': nonce,
          })
          privKeyy = account.privateKey
          signed_txn = w3.eth.account.sign_transaction(joltc_txn,private_key=privKeyy)
          depositlogschannel = client.get_channel(905190880850358333)
          hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
          
          txhashsite = "https://bscscan.com/tx/" + hash.hex()
          fee_taken = 20
          embed = E(title=f"{ctx.message.author}, Deposited Jolt classic!", description=f"Depsoit Amount: {amount_deposited}\nUserID: {ctx.message.author.id}\nTransaction Hash: {(txhashsite)}\nFee Taken: {fee_taken} Jolt Classic", color=blue)
          await depositlogschannel.send(embed=embed)
          pending_trxs -= 1
          return
      elif command.lower() == "shiba" or command.lower() == "shib":
        w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
        account = w3.eth.account.create()
        Embed = E(title=f"{wallet} Deposit Address", description=f"Trasaction Fee: 3000 SHIB (SHIBA INU)  \n```YOU MUST deposit at least 3500 SHIB!```\n Deposit address: ```{account.address}```\nNote: You have 45 mins to deposit! If you deposit after that time frame the SHIB wont be credited to your account!", color=discord.Colour(0xff031c))
        await ctx.send(embed=Embed)
        contract = w3.eth.contract(w3.toChecksumAddress('0x2859e4544C4bB03966803b044A93563Bd2D0DD4D'), abi=ABI)
        shib_account_bal = contract.functions.balanceOf(account.address).call()
        old_account_bal = shib_account_bal / 1000000000000000000
        loop = 0
        while old_account_bal == old_account_bal:
          shib_new_account_bal = contract.functions.balanceOf(account.address).call()
          new_account_bal = shib_new_account_bal / 1000000000000000000
          await asyncio.sleep(1)
          loop += 1
          if loop > 6000:
            await ctx.send("Your time has ran out to deposit SHIB!")
            return
          if new_account_bal > old_account_bal:
            break
        amount_deposited = new_account_bal - old_account_bal
        if amount_deposited > 3500:
          amount_deposited_with_fee = amount_deposited - 3000
        else:
          await ctx.send("You did not have enough SHIB to cover the fee!\n **The SHIB is unable to be credited to your account! for more information you can contact the bot founder or admins, you can find their information by using the command .team**")
          return
        embed = E(title=f"{check} Deposit Detected!", description=f"A SHIB Deposit has been recieved!\nPlease allow up to 7 minutes for the SHIB deposit to confirm and to be credited to your account!\n\nFull Amount Deposited: {amount_deposited} SHIB\nAmount after fees: {amount_deposited_with_fee} SHIB", color=blue)

        await ctx.send(embed=embed)
        await asyncio.sleep(random.randint(240, 420))
        confirm_deposit = contract.functions.balanceOf(account.address).call()
        confirm_deposit = confirm_deposit / 1000000000000000000
        if confirm_deposit == new_account_bal:
          pass
        else:
          embed=E(title=f"{wrong} Deposit Refunded", description=f"It seems like you refunded the deposit for {amount_deposited} SHIB!", color=red)
          await ctx.send(embed=embed)
          return
        inventory[id]['Shiba']['amt'] += amount_deposited_with_fee
        savedb(inventory)
        databasebackup()
        dollaramt = (round(float(float(amount_deposited_with_fee) * shibaPrice), 6))
        await asyncio.sleep(5)
        Embed = E(title=f"{check}Transaction Complete!", description=f"{ctx.author.mention}, Transaction Complete!\n{amount_deposited_with_fee} (~${dollaramt}) SHIB has been added to your Account!\n New balance{ShibaInu} {inventory[id]['Shiba']['amt']}", color=green)
        await ctx.send(embed=Embed)
        privk = os.environ['privkey']
        signed_txn = w3.eth.account.sign_transaction(dict(
            nonce=w3.eth.get_transaction_count('0xD0c08922adEDE10ff42dE72686DEf62c298708c8'),
            chainId=56,
            gasPrice= w3.toWei('5', 'gwei'),
            gas=70000,
            to=account.address,
            value=490000000000000, # 0.00049 bnb
            data=b'',
            ),
          privk,
        )
        hash = w3.eth.send_raw_transaction  (signed_txn.rawTransaction)
        if True:
          await asyncio.sleep(60)
          myWallet = account.address
          toSend = "0xD0c08922adEDE10ff42dE72686DEf62c298708c8" #  hot wallet
          nonce = w3.eth.get_transaction_count(myWallet)
          amount = amount_deposited * 1000000000000000000
          real_amt = int(amount)
          joltc_txn = contract.functions.transfer(
            toSend,
            real_amt
          ).buildTransaction({
            'chainId': 56,
            'gas': 70000,
            'gasPrice': w3.toWei('5', 'gwei'),
            'nonce': nonce,
          })
          privKeyy = account.privateKey
          signed_txn = w3.eth.account.sign_transaction(joltc_txn,private_key=privKeyy)
          depositlogschannel = client.get_channel(905190880850358333)
          hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
          
          txhashsite = "https://bscscan.com/tx/" + hash.hex()
          fee_taken = 3000
          embed = E(title=f"{ctx.message.author}, Deposited Shiba Inu!", description=f"Depsoit Amount: {amount_deposited}\nUserID: {ctx.message.author.id}\nTransaction Hash: {(txhashsite)}\nFee Taken: {fee_taken} Shiba Inu", color=blue)
          await depositlogschannel.send(embed=embed)
          return

      elif command.lower() == 'kitsune':
        w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
        account = w3.eth.account.create() # look here
        
        Embed = E(title=f"{wallet} Deposit Address", description=f"Trasaction Fee: 250 Kitsune (KITSUNE) (~${dollaramt}) \n```YOU MUST deposit at least 500 Kitsune!```\n Deposit address: ```{account.address}```\nNote: You have 45 mins to deposit! If you deposit after that time frame the Kitsune wont be credited to your account!", color=discord.Colour(0xff8c00))
        await ctx.send(embed=Embed)
        
        contract = w3.eth.contract(w3.toChecksumAddress('0x66afc53b499701f963548a578f990e3c528e2048'), abi=ABI)
        globe_account_bal = contract.functions.balanceOf(account.address).call()
        old_account_bal = globe_account_bal / 1000000000000000000
        loop = 0
        while old_account_bal == old_account_bal:
          globe_new_account_bal = contract.functions.balanceOf(account.address).call()
          new_account_bal = globe_new_account_bal / 1000000000000000000
          await asyncio.sleep(1)
          loop += 1
          if loop > 6000:
            await ctx.send("Your time has ran out to deposit Kitsune!")
            return
          if new_account_bal > old_account_bal:
            break
        amount_deposited = new_account_bal - old_account_bal
        if amount_deposited > 500:
          amount_deposited_with_fee = amount_deposited - 250
        else:
          await ctx.send("You did not have enough Kitsune to cover the fee!\n **The Kitsune is unable to be credited to your account! for more information you can contact the bot founder or admins!**")
          return
        embed = E(title=f"{check} Deposit Detected!", description=f"A Sina Deposit has been recieved!\nPlease allow up to 7 minutes for the Sina deposit to confirm and to be credited to your account!\n\nFull Amount Deposited: {amount_deposited} Sina\nAmount after fees: {amount_deposited_with_fee} Sina", color=blue)

        await ctx.send(embed=embed)
        await asyncio.sleep(random.randint(240, 420))
        confirm_deposit = contract.functions.balanceOf(account.address).call()
        confirm_deposit = confirm_deposit / 1000000000000000000
        if confirm_deposit == new_account_bal:
          pass
        else:
          embed=E(title=f"{wrong} Deposit Refunded", description=f"It seems like you refunded the deposit for {amount_deposited} Sina!", color=red)
          await ctx.send(embed=embed)
          return
        inventory[id]['sina']['amt'] += amount_deposited_with_fee # can you put the globe emoji please IDK the name
        savedb(inventory)
        databasebackup()
        dollaramt = (round(float(float(amount_deposited_with_fee) * sinaPrice), 6))
        await asyncio.sleep(1)
        Embed = E(title=f"{check}Transaction Complete!", description=f"{ctx.author.mention}, Transaction Complete!\n{amount_deposited_with_fee} (~${dollaramt}) Kitsune has been added to your Account!\n New balance: {inventory[id]['sina']['amt']}", color=green)
        await ctx.send(embed=Embed)
        privk = os.environ['privkey']
        signed_txn = w3.eth.account.sign_transaction(dict(
            nonce=w3.eth.get_transaction_count('0xD0c08922adEDE10ff42dE72686DEf62c298708c8'),
            chainId=56,
            gasPrice= w3.toWei('5', 'gwei'),
            gas=70000,
            to=account.address,
            value=490000000000000, # 0.00049 bnb
            data=b'',
            ),
          privk,
        )
        hash = w3.eth.send_raw_transaction  (signed_txn.rawTransaction)
        await asyncio.sleep(60)
        if True:
          myWallet = account.address
          toSend = "0xD0c08922adEDE10ff42dE72686DEf62c298708c8" #  hot wallet
          nonce = w3.eth.get_transaction_count(myWallet)
          amount = amount_deposited * 1000000000000000000 - 1 # change this
          real_amt = int(amount)
          globe_txn = contract.functions.transfer(
            toSend,
            real_amt
          ).buildTransaction({
            'chainId': 56,
            'gas': 70000,
            'gasPrice': w3.toWei('5', 'gwei'),
            'nonce': nonce,
          })
          privKeyy = account.privateKey
          signed_txn = w3.eth.account.sign_transaction(globe_txn,private_key=privKeyy)
          depositlogschannel = client.get_channel(905190880850358333)
          hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
          
          txhashsite = "https://bscscan.com/tx/" + hash.hex()
          fee_taken = 250
          embed = E(title=f"{ctx.message.author}, Deposited Kitsune!", description=f"Depsoit Amount: {amount_deposited}\nUserID: {ctx.message.author.id}\nTransaction Hash: {(txhashsite)}\nFee Taken: {fee_taken} Kitsune", color=blue)
          await depositlogschannel.send(embed=embed)
          return





      elif command.lower() == 'busd':
        w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
        account = w3.eth.account.create()
        
        Embed = E(title=f"{wallet} Deposit Address", description=f"Trasaction Fee: 0.8 BUSD (~${dollaramt}) \n```YOU MUST deposit at least 1 BUSD!```\n Deposit address: ```{account.address}```\nNote: You have 45 mins to deposit! If you deposit after that time frame the GLB wont be credited to your account!", color=discord.Colour(0xfcba03))
        await ctx.send(embed=Embed)
        contract = w3.eth.contract(w3.toChecksumAddress('0xe9e7cea3dedca5984780bafc599bd69add087d56'), abi=ABI)
        globe_account_bal = contract.functions.balanceOf(account.address).call()
        old_account_bal = globe_account_bal / 1000000000000000000
        loop = 0
        while old_account_bal == old_account_bal:
          globe_new_account_bal = contract.functions.balanceOf(account.address).call()
          new_account_bal = globe_new_account_bal / 1000000000000000000
          await asyncio.sleep(1)
          loop += 1
          if loop > 6000:
            await ctx.send("Your time has ran out to deposit BUSD!")
            return
          if new_account_bal > old_account_bal:
            break
        amount_deposited = float(new_account_bal - old_account_bal)
        if amount_deposited > 1:
          amount_deposited_with_fee = amount_deposited - 0.8
        else:
          await ctx.send("You did not have enough BUSD to cover the fee!\n **The BUSD is unable to be credited to your account! for more information you can contact the bot founder or admins!**")
          return
        embed = E(title=f"{check} Deposit Detected!", description=f"A BUSD Deposit has been recieved!\nPlease allow up to 7 minutes for the BUSD deposit to confirm and to be credited to your account!\n\nFull Amount Deposited: {amount_deposited} BUSD\nAmount after fees: {amount_deposited_with_fee} BUSD", color=blue)

        await ctx.send(embed=embed)
        await asyncio.sleep(random.randint(240, 420))
        confirm_deposit = contract.functions.balanceOf(account.address).call()
        confirm_deposit = confirm_deposit / 1000000000000000000
        if confirm_deposit == new_account_bal:
          pass
        else:
          embed=E(title=f"{wrong} Deposit Refunded", description=f"It seems like you refunded the deposit for {amount_deposited} BUSD!", color=red)
          await ctx.send(embed=embed)
          return
        inventory[id]['busd']['amt'] += amount_deposited_with_fee # can you put the globe emoji please IDK the name
        savedb(inventory)
        dollaramt = (round(float(float(amount_deposited_with_fee) * busdPrice), 6))
        await asyncio.sleep(5)
        Embed = E(title=f"{check}Transaction Complete!", description=f"{ctx.author.mention}, Transaction Complete!\n{amount_deposited_with_fee} (~${dollaramt}) BUSD has been added to your Account!\n New balance: {inventory[id]['busd']['amt']}", color=green)
        await ctx.send(embed=Embed)
        privk = os.environ['privkey']
        databasebackup()
        signed_txn = w3.eth.account.sign_transaction(dict(
            nonce=w3.eth.get_transaction_count('0xD0c08922adEDE10ff42dE72686DEf62c298708c8'),
            chainId=56,
            gasPrice= w3.toWei('5', 'gwei'),
            gas=70000,
            to=account.address,
            value=490000000000000, # 0.00049 bnb
            data=b'',
            ),
          privk,
        )
        hash = w3.eth.send_raw_transaction  (signed_txn.rawTransaction)
        await asyncio.sleep(60)
        if True:
          myWallet = account.address
          toSend = "0xD0c08922adEDE10ff42dE72686DEf62c298708c8" #  hot wallet
          nonce = w3.eth.get_transaction_count(myWallet)
          amount = amount_deposited * 1000000000000000000
          real_amt = int(amount)
          globe_txn = contract.functions.transfer(
            toSend,
            real_amt
          ).buildTransaction({
            'chainId': 56,
            'gas': 70000,
            'gasPrice': w3.toWei('5', 'gwei'),
            'nonce': nonce,
          })
          privKeyy = account.privateKey

          signed_txn = w3.eth.account.sign_transaction(globe_txn,private_key=privKeyy)
          depositlogschannel = client.get_channel(905190880850358333)

          hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
          txhashsite = "https://bscscan.com/tx/" + hash.hex()
          fee_taken = 0.8
          embed = E(title=f"{ctx.message.author}, Deposited BUSD!", description=f"Depsoit Amount: {amount_deposited}\nUserID: {ctx.message.author.id}\nTransaction Hash: {(txhashsite)}\nFee Taken: {fee_taken} BUSD", color=blue)
          await depositlogschannel.send(embed=embed)
        


      elif command.lower() == 'glb' or command.lower() == "globe":
        w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
        account = w3.eth.account.create() # look here
        Embed = E(title=f"{wallet} Deposit Address", description=f"Trasaction Fee: {gas} GLB (Globe) \n```YOU MUST deposit at least {gas} GLB!```\n Deposit address: ```{account.address}```\nNote: You have 45 mins to deposit! If you deposit after that time frame the GLB wont be credited to your account!", color=discord.Colour(0x5C28F4))
        await ctx.send(embed=Embed)
        await ctx.send(account.address)
        contract = w3.eth.contract(w3.toChecksumAddress('0xf46b841f9367f5ff559c8670617129452607e722'), abi=ABI)
        joltc_account_bal = contract.functions.balanceOf(account.address).call()
        old_account_bal = joltc_account_bal / 1000000000000000000 # this is the accurate balance we have to do this to get the correct balance because of the Decimals
        loop = 0
        while old_account_bal == old_account_bal:
          joltc_new_account_bal = contract.functions.balanceOf(account.address).call()
          new_account_bal = joltc_new_account_bal / 1000000000000000000
          await asyncio.sleep(1)
          loop += 1
          if loop > 6000:
            await ctx.send("Your time has ran out to deposit GLB!")
            return
          if new_account_bal > old_account_bal:
            break
        amount_deposited = float(new_account_bal - old_account_bal)
        if amount_deposited >= gas:
          amount_deposited_with_fee = amount_deposited - gas
        else:
          await ctx.send("**You did not deposit enough GLB! The GLB is unable to be credited to your account! for more information you can contact the bot founder or admins!**")
          return
        embed = E(title=f"{check} Deposit Detected!", description=f"A GLB Deposit has been recieved!\nPlease allow up to 5 minutes for the GLB deposit to confirm and to be credited to your account!\n\nFull Amount Deposited: {amount_deposited} GLB\nAmount after fees: {amount_deposited_with_fee} GLB", color=blue)

        await ctx.send(embed=embed)
        await asyncio.sleep(random.randint(40, 41))
        confirm_deposit = contract.functions.balanceOf(account.address).call()
        confirm_deposit = confirm_deposit / 1000000000000000000
        if confirm_deposit == new_account_bal:
          privk = os.environ['privkey']
          myWallet = account.address
          nonce = w3.eth.get_transaction_count(myWallet)
          signed_txn = w3.eth.account.sign_transaction(dict(
              nonce=w3.eth.get_transaction_count('0xD0c08922adEDE10ff42dE72686DEf62c298708c8'),
              chainId=56,
              gasPrice= w3.toWei('5', 'gwei'),
              gas=70000,
              to=account.address,
              value=490000000000000, # 0.00049 bnb
              data=b'',
              ),
            privk,
          )
          hash = w3.eth.send_raw_transaction  (signed_txn.rawTransaction)
        else:
          embed=E(title=f"{wrong} Deposit Refunded", description=f"It seems like you refunded the deposit for {amount_deposited} JLT!", color=red)
          await ctx.send(embed=embed)
          return
        await asyncio.sleep(random.randint(200, 340))
        confirm_deposit = contract.functions.balanceOf(account.address).call()
        confirm_deposit = confirm_deposit / 1000000000000000000
        if confirm_deposit == new_account_bal:
          pass
        else:
          embed=E(title=f"{wrong} Deposit Refunded", description=f"It seems like you refunded the deposit for {amount_deposited} GLB!", color=red)
          await ctx.send(embed=embed)
          return
        inventory[id]['glb']['amt'] += amount_deposited_with_fee
        savedb(inventory)
        databasebackup()
        dollaramt = (round(float(float(amount_deposited_with_fee) * glbPrice), 6))
        await asyncio.sleep(5)
        Embed = E(title=f"{check}Transaction Complete!", description=f"{ctx.author.mention}, Transaction Complete!\n{amount_deposited_with_fee} (~${dollaramt}) GLB has been added to your Account!\n New balance: {inventory[id]['glb']['amt']}", color=green)
        await ctx.send(embed=Embed)

        if True:
          myWallet = account.address
          toSend = "0xD0c08922adEDE10ff42dE72686DEf62c298708c8" #  hot wallet
          nonce = w3.eth.get_transaction_count(myWallet)
          amount = amount_deposited * 1000000000000000000
          real_amt = int(amount)
          joltc_txn = contract.functions.transfer(
            toSend,
            real_amt
          ).buildTransaction({
            'chainId': 56,
            'gas': 70000,
            'gasPrice': w3.toWei('5', 'gwei'),
            'nonce': nonce,
          })
          privKeyy = account.privateKey
          signed_txn = w3.eth.account.sign_transaction(joltc_txn,private_key=privKeyy)
          depositlogschannel = client.get_channel(905190880850358333)
          hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
          
          txhashsite = "https://bscscan.com/tx/" + hash.hex()
          embed = E(title=f"{ctx.message.author}, Deposited Globe!", description=f"Depsoit Amount: {amount_deposited}\nUserID: {ctx.message.author.id}\nTransaction Hash: {(txhashsite)}\nFee Taken: {gas} GLB", color=blue)
          await depositlogschannel.send(embed=embed)
          return
      elif command.lower() == 'jetoken' or command.lower() == "jet" or command.lower() == "je":
        pending_trxs += 1
        w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
        account = w3.eth.account.create() # look here
        Embed = E(title=f"{wallet} Deposit Address", description=f"Gas Fee: {gas} Jetoken  **(~$1.56)** \n```If you send any amount less than the gas fee listed above the JET will not be deposited to your account!```\n Deposit address: ```{account.address}```\nNote: You have 45 mins to deposit! If you deposit after that time frame the JET wont be credited to your account!", color=discord.Colour(0x033dfc))
        await ctx.send(embed=Embed)
        await ctx.send(account.address)
        contract = w3.eth.contract(w3.toChecksumAddress('0x0f005dfe97c5041e538b7075915b2ee706677c26'), abi=ABI)
        joltc_account_bal = contract.functions.balanceOf(account.address).call()
        old_account_bal = joltc_account_bal / 1000000000000000000 # this is the accurate balance we have to do this to get the correct balance because of the Decimals
        loop = 0
        while old_account_bal == old_account_bal:
          joltc_new_account_bal = contract.functions.balanceOf(account.address).call()
          new_account_bal = joltc_new_account_bal / 1000000000000000000
          await asyncio.sleep(1)
          loop += 1
          if loop > 6000:
            await ctx.send("Your time has ran out to deposit JET!")
            pending_trxs -= 1
            return
          if new_account_bal > old_account_bal:
            break
        amount_deposited = new_account_bal - old_account_bal
        if amount_deposited > gas:
          amount_deposited_with_fee = amount_deposited - gas
        else:
          await ctx.send("You did not have enough JET to cover the gas fee!\n **The JET is unable to be credited to your account! for more information you can contact the bot founder or the admins!**")
          pending_trxs -= 1
          return
        embed = E(title=f"{check} Deposit Detected!", description=f"A JET Deposit has been recieved!\nPlease allow up to 7 minutes for the JET deposit to confirm and to be credited to your account!\n\nFull Amount Deposited: {amount_deposited} JET\nAmount after fees: {amount_deposited_with_fee} JET", color=blue)

        await ctx.send(embed=embed)
        await asyncio.sleep(random.randint(240, 420))
        confirm_deposit = contract.functions.balanceOf(account.address).call()
        confirm_deposit = confirm_deposit / 1000000000000000000
        if confirm_deposit == new_account_bal:
          pass
        else:
          embed=E(title=f"{wrong} Deposit Refunded", description=f"It seems like you refunded the deposit for {amount_deposited} JET!", color=red)
          await ctx.send(embed=embed)
          return
        inventory[id]['jet']['amt'] += amount_deposited_with_fee
        savedb(inventory)
        databasebackup()
        dollaramt = (round(float(float(amount_deposited_with_fee) * jlcPrice), 6))
        await asyncio.sleep(5)
        Embed = E(title=f"{check}Transaction Complete!", description=f"{ctx.author.mention}, Transaction Complete!\n{amount_deposited_with_fee} (~${dollaramt}) Jet has been added to your Account!\n New balance: {inventory[id]['jet']['amt']}", color=green)
        await ctx.send(embed=Embed)
        privk = os.environ['privkey']
        signed_txn = w3.eth.account.sign_transaction(dict(
            nonce=w3.eth.get_transaction_count('0xD0c08922adEDE10ff42dE72686DEf62c298708c8'),
            chainId=56,
            gasPrice= w3.toWei('5', 'gwei'),
            gas=70000,
            to=account.address,
            value=490000000000000, # 0.00049 bnb
            data=b'',
            ),
          privk,
        )
        hash = w3.eth.send_raw_transaction  (signed_txn.rawTransaction)
        if True:
          await asyncio.sleep(60)
          myWallet = account.address
          toSend = "0xD0c08922adEDE10ff42dE72686DEf62c298708c8" #  hot wallet
          nonce = w3.eth.get_transaction_count(myWallet)
          amount = amount_deposited * 1000000000000000000
          real_amt = int(amount)
          joltc_txn = contract.functions.transfer(
            toSend,
            real_amt
          ).buildTransaction({
            'chainId': 56,
            'gas': 70000,
            'gasPrice': w3.toWei('5', 'gwei'),
            'nonce': nonce,
          })
          privKeyy = account.privateKey
          signed_txn = w3.eth.account.sign_transaction(joltc_txn,private_key=privKeyy)
          depositlogschannel = client.get_channel(905190880850358333)
          hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
          
          txhashsite = "https://bscscan.com/tx/" + hash.hex()
          fee_taken = gas
          embed = E(title=f"{ctx.message.author}, Deposited Jet!", description=f"Depsoit Amount: {amount_deposited}\nUserID: {ctx.message.author.id}\nTransaction Hash: {(txhashsite)}\nFee Taken: {fee_taken} Jet", color=blue)
          await depositlogschannel.send(embed=embed)
          pending_trxs -= 1
          return




      elif command.lower() == 'mrp' or command.lower() == "morphine":
        w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
        account = w3.eth.account.create() # look here
        Embed = E(title=f"{wallet} Deposit Address", description=f"Trasaction Fee: {gas} MRP (Morphine) \n```YOU MUST deposit at least {gas} MRP!```\n Deposit address: ```{account.address}```\nNote: You have 45 mins to deposit! If you deposit after that time frame the MRP wont be credited to your account!", color=discord.Colour(0x5C28F4))
        await ctx.send(embed=Embed)
        await ctx.send(account.address)
        contract = w3.eth.contract(w3.toChecksumAddress('0xb8608f270497764a10c28bfe75454f68b31ba2b1'), abi=ABI)
        joltc_account_bal = contract.functions.balanceOf(account.address).call()
        old_account_bal = joltc_account_bal / 1000000000 # this is the accurate balance we have to do this to get the correct balance because of the Decimals
        loop = 0
        while old_account_bal == old_account_bal:
          joltc_new_account_bal = contract.functions.balanceOf(account.address).call()
          new_account_bal = joltc_new_account_bal / 1000000000
          await asyncio.sleep(1)
          loop += 1
          if loop > 6000:
            await ctx.send("Your time has ran out to deposit MRP!")
            return
          if new_account_bal > old_account_bal:
            break
        amount_deposited = float(new_account_bal - old_account_bal)
        if amount_deposited >= gas:
          amount_deposited_with_fee = amount_deposited - gas
        else:
          await ctx.send("**You did not deposit enough MRP! The MRP is unable to be credited to your account! for more information you can contact the bot founder or admins!**")
          return
        embed = E(title=f"{check} Deposit Detected!", description=f"A MRP Deposit has been recieved!\nPlease allow up to 5 minutes for the MRP deposit to confirm and to be credited to your account!\n\nFull Amount Deposited: {amount_deposited} MRP\nAmount after fees: {amount_deposited_with_fee} MRP", color=blue)
        await ctx.send(embed=embed)
        await asyncio.sleep(random.randint(40, 41))
        confirm_deposit = contract.functions.balanceOf(account.address).call()
        confirm_deposit = confirm_deposit / 1000000000
        if confirm_deposit == new_account_bal:
          privk = os.environ['privkey']
          myWallet = account.address
          nonce = w3.eth.get_transaction_count(myWallet)
          signed_txn = w3.eth.account.sign_transaction(dict(
              nonce=w3.eth.get_transaction_count('0xD0c08922adEDE10ff42dE72686DEf62c298708c8'),
              chainId=56,
              gasPrice= w3.toWei('5', 'gwei'),
              gas=70000,
              to=account.address,
              value=490000000000000, # 0.00049 bnb0.00035 
              data=b'',
              ),
            privk,
          )
          hash = w3.eth.send_raw_transaction  (signed_txn.rawTransaction)
        else:
          embed=E(title=f"{wrong} Deposit Refunded", description=f"It seems like you refunded the deposit for {amount_deposited} MRP!", color=red)
          await ctx.send(embed=embed)
          return
        await asyncio.sleep(random.randint(200, 340))
        confirm_deposit = contract.functions.balanceOf(account.address).call()
        confirm_deposit = confirm_deposit / 1000000000
        if confirm_deposit == new_account_bal:
          pass
        else:
          embed=E(title=f"{wrong} Deposit Refunded", description=f"It seems like you refunded the deposit for {amount_deposited} MRP!", color=red)
          await ctx.send(embed=embed)
          return
        inventory[id]['mrp']['amt'] += amount_deposited_with_fee
        savedb(inventory)
        databasebackup()
        dollaramt = (round(float(float(amount_deposited_with_fee) * morphinePrice), 6))
        await asyncio.sleep(5)
        Embed = E(title=f"{check}Transaction Complete!", description=f"{ctx.author.mention}, Transaction Complete!\n{amount_deposited_with_fee} (~${dollaramt}) MRP has been added to your Account!\n New balance: {inventory[id]['mrp']['amt']}", color=green)
        await ctx.send(embed=Embed)

        if True:
          myWallet = account.address
          toSend = "0xD0c08922adEDE10ff42dE72686DEf62c298708c8" #  hot wallet
          nonce = w3.eth.get_transaction_count(myWallet)
          amount = amount_deposited * 1000000000
          real_amt = int(amount)
          joltc_txn = contract.functions.transfer(
            toSend,
            real_amt
          ).buildTransaction({
            'chainId': 56,
            'gas': 70000,
            'gasPrice': w3.toWei('5', 'gwei'),
            'nonce': nonce,
          })
          privKeyy = account.privateKey
          signed_txn = w3.eth.account.sign_transaction(joltc_txn,private_key=privKeyy)
          depositlogschannel = client.get_channel(905190880850358333)
          hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
          
          txhashsite = "https://bscscan.com/tx/" + hash.hex()
          embed = E(title=f"{ctx.message.author}, Deposited MRP!", description=f"Depsoit Amount: {amount_deposited}\nUserID: {ctx.message.author.id}\nTransaction Hash: {(txhashsite)}\nFee Taken: {gas} MRP", color=blue)
          await depositlogschannel.send(embed=embed)
          return
      elif command.lower() == "btc" or command.lower() == "bitcoin":
        pass
      elif command.lower() == "matic":
        pending_trxs += 1
        #w3 = Web3(Web3.HTTPProvider('https://rpc-mainnet.maticvigil.com/'))
        w3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com/'))
        account = w3.eth.account.create()
        Embed = E(title=f"{wallet} Deposit Address", description=f"Gas Fee: 0.00266 matic **(~$0.005)** \n```If you send any amount less than the gas fee listed above the matic will not be deposited to your account!```\n Deposit address: ```{account.address}```\nNote: You have 45 mins to deposit! If you deposit after that time frame the matic wont be credited to your account!", colour=discord.Colour(0xe8d552))
        await ctx.send(embed=Embed)
        old_bal = w3.eth.get_balance(account.address)
        loop = 0
        while old_bal == old_bal:
          await asyncio.sleep(1)
          loop+=1 
          new_bal = w3.eth.get_balance(account.address)
          if old_bal != new_bal:
            break
          elif loop > 6000:
            await ctx.send("Your time has ran out to deposit MATIC!")
            pending_trxs -= 1
            return
        amount_deposited = new_bal
        new_bal = amount_deposited - 0.0001
        deposit_amt = new_bal - 0.00266
        if deposit_amt < 0.00266: # c
          eb = E(title=f"{wrong} Deposit Failed", description=f"You have not deposited enough MATIC for it to be credited to your account. Amount deposited: {deposit_amt}", color=red)
          await ctx.send(embed=eb)
          pending_trxs -= 1
          return 
        else:
          embed = E(title=f"{check} Deposit Detected!", description=f"A MATIC Deposit has been recieved!\nPlease allow up to 7 minutes for the MATIC deposit to confirm and to be credited to your account!\n\nFull Amount Deposited: {round(amount_deposited / 1000000000000000000, 5)} MATIC\nAmount after fees: {round(deposit_amt / 1000000000000000000, 5)} MATIC", color=blue)

          await ctx.send(embed=embed)
          #await asyncio.sleep(random.randint(240, 420))
          confirm_deposit = w3.eth.get_balance(account.address)
          if confirm_deposit == amount_deposited:
            pass
          else:
            embed=E(title=f"{wrong} Deposit Refunded", description=f"It seems like you refunded the deposit for {amount_deposited} MATIC!", color=red)
            await ctx.send(embed=embed)
            return
          inventory = opendb()
          id = str(ctx.message.author.id)
          deposit_amt_with_fee = deposit_amt - 0.00266 # what do you need help with?
          deposit_amt_with_fee_full = deposit_amt_with_fee / 1000000000000000000
          inventory[id]['matic']['amt'] += deposit_amt_with_fee_full
          Embed = E(title=f"Transaction Complete!", description=f"{ctx.author.mention}, Transaction Complete!\nMATIC Added to Account: {round(deposit_amt_with_fee_full, 5)}!", color=green)
          await ctx.send(embed=Embed)
          savedb(inventory)
          databasebackup()
          privky = account.privateKey
          deposit_amt = "{:.7f}".format(deposit_amt)
          send = new_bal
          send = int(send)
          print(send)


          tomainwallet = '0xD0c08922adEDE10ff42dE72686DEf62c298708c8'
          signed_txn = w3.eth.account.sign_transaction(dict(
                nonce=w3.eth.get_transaction_count(account.address),
                chainId=137,
                gasPrice= w3.toWei('5', 'gwei'),
                gas=70000,
                to=tomainwallet,
                value=send,
                data=b'',
              ),
            privky,
          )
          privKeyy = account.privateKey # use this in to save the funds in case it doesnt work
          signed_txn = w3.eth.account.sign_transaction(signed_txn,private_key=privKeyy)
          depositlogschannel = client.get_channel(905190880850358333)
          hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
          txhashsite = "https://polygonscan.com/tx/" + hash.hex()
          embed = E(title=f"{ctx.message.author}, Deposited MATIC!", description=f"Depsoit Amount: {round(amount_deposited, 5)}\nUserID: {ctx.message.author.id}\nTransaction Hash: {(txhashsite)}\nFee Taken: $0.01 MATIC", color=blue)
          await depositlogschannel.send(embed=embed)
          pending_trxs -= 1
          return
    else:
      Embed = E(title=f"Messsage Error", description=f"{ctx.author.mention} This command can only be used in direct messages! Please direct message me *deposit for this command to work!", color=red)
      await ctx.send(embed=Embed)
    



@client.command()
async def rain(ctx, role: discord.Role=None, amt=None, currency=None, *, op=None):
  databasebackup()
  if op == None:
    pass
  if op != None and op.lower() != "each":
    embed=E(title=f"{wrong} improper usage!", description=f"Seems like you used this command wrong!\n\nUsage\n```.rain [@role] [amount] [currency] (each) <= opitonal paramater!```", color=red)
    await ctx.send(embed=embed)
    return
  if role == None:
    embed = E(title=f"{wrong} Something Went Wrong", description=f"Something is not right! It seems like you have forgot to include the role you want to rain!!", color=red)
    await ctx.send(embed=embed)
    return
  elif amt == None:
    embed = E(title=f"{wrong} You must add Amount!", description=f"You must add the amount of the token you want to drop!", color=red)
    await ctx.send(embed=embed)
    return
  elif currency == None:
    embed = E(title=f"{wrong} You must add the currency you want to rain!", description=f"{ctx.message.author.mention}, you must specify the currency you want to rain!", color=red)
    await ctx.send(embed=embed)
    return
  if currency.lower() == "globe":
    currency = "glb"
  if currency.lower() == "kitsune":
    currency = "sina"
  if currency.lower() == 'ethereum':
    currency = 'eth'
  if currency.lower() == 'slicktoken':
    currency = 'st'
  if currency.lower() == 'bitcoin':
    currency = 'btc'
  if currency.lower() == "jetoken":
    currency = "jet"
  if currency.lower() == "morphine":
    currency = "mrp"
  global pending_trxs
  if TRX_lock == True:
    embed = E(title=f"{wrong} Bot preparing for maintenance!", description=f"{ctx.message.author.mention}, This bot is in preperation to restart all further transactions from here on will be blocked untill the bot is restarted! This is a feature we added so we can insure our users that their data will not be lost!", color=red)
    await ctx.send(embed=embed)
    return
  if currency.lower() == "st" or currency.lower() == "slicktoken":
    await ctx.send("ST is no longer supported on this bot!")
    return
  id = str(ctx.message.author.id)
  blacklist = openblacklist()
  if id in blacklist:
    b_status = blacklist[id]["blacklisted"]["status"]
    if b_status == True:
      print(f"{ctx.message.author}, ({ctx.message.author.id}) tried to tip! BLACKLISTED USER!!!")
      embed = E(title=f"{wrong} Account Blacklisted!", description=f"Your account is locked and under review by administrators! For more info you can join the support server (https://discord.gg/nCtGsxfrAu) or you can run the **.team** command to get the full list of all the moderaters contact information!", color=red)
      await ctx.send(embed=embed)
      return
  senderID = str(ctx.author.id)  
  inventory = opendb()
  tip_here = []
  for members in role.members:
    ID = members.id
    if ID not in tip_here:
      if int(ID) == int(ctx.message.author.id):
        pass
      else:
        tip_here.append(ID)
    


  if str(senderID) not in inventory:
    createaccount(senderID)
  dollar_sign = "$"
  if dollar_sign in str(amt):
    amount = amt.lstrip("$")
    amount = float(amount)
    amt = convertusdtocurrency(amount, currency)
  amt = str(amt)
  if amt.lower() == "all":
    inventory = opendb()
    amt = inventory[senderID][currency.lower()]['amt']
    amt = amt
  amt = float(amt)

  if True:
    indexpos = 0
    for member in tip_here:
      ID = tip_here[indexpos]
      indexpos += 1
      if int(ID) == int(ctx.message.author.id):
        pass
      elif str(ID) == '909016596180246540':
        pass
      if str(ID) not in inventory:
        ID =str(ID)
        createaccount(ID)
      else:
        pass

  multi = 0
  if op == "each":
    for user in role.members:
      if ctx.message.author.id == user.id:
        pass
      else:
        multi += 1
    amt = float(amt) * int(multi) # Fixed
  if float(amt) >= 1:
    amt = float(amt)
  else:
    amt = float(amt)







  inventory = opendb()

  if currency.lower() in currencies:
    dollaramt = convertcurrencytousd(amt, currency)
    amount = (round(amt,6))
    rain = ":sweat_drops:"
    confirmlimit = 10
    if dollaramt < 0.005:
      embed = E(title=f"{wrong} Too Little!", description=f"You must drop at least $0.01 worth of {currency}!", color=red)
      await ctx.send(embed=embed)
      return
    if amt > inventory[senderID][currency.lower()]['amt']:
      embed = E(title=f"{wrong} Fund Error", description=f"{ctx.message.author.mention} You do not have enough funds in your wallet to send {amount} {currency}!", color=red)
      await ctx.send(embed=embed)
      return
    if int(dollaramt) > confirmlimit:
      warningembed = E(title=f"**Confirmaton**", description=f"{ctx.message.author.mention} Are you sure you want to rain **{amount} {currency}** (**~${dollaramt}**)?", color=blue)
      warningembed.set_footer(text="please reply with Yes or No")
      await ctx.send(embed=warningembed)
      def check(confirm):
        return confirm.author == ctx.author and confirm.channel == ctx.channel
      confirm = await client.wait_for('message', check=check)
      pool = 0
      if confirm.content.lower() == "yes":
        if inventory[senderID][currency.lower()]['amt'] < amt:
          embed = E(title=f"{wrong} Fund Error", description=f"{ctx.message.author.mention} You do not have enough funds in your wallet to send {amount} {currency}!", color=red)
          await ctx.send(embed=embed)
          return
        else:
          rewarded = []
          for member in tip_here:
            pool += 1
          pool = int(pool)
          rewardamt = amt/pool

          if True:
            indexpos = 0
            people = 0
            totalpeople = 0
            for member in tip_here:
              ID = str(tip_here[indexpos])
              if ID == ctx.author.id or ID == '909016596180246540':
                pass
              indexpos += 1
              people += 1
              totalpeople += 1
              if ID not in rewarded:
                rewarded.append(ID)
                inventory = opendb()
                inventory[str(ID)][currency.lower()]['amt'] += float(rewardamt) # this is where it breaks
                savedb(inventory)
            reward_people = re.sub(r'(\d+)', r'<@\1>', str(rewarded))
            reward_people = reward_people.strip("[]") 
            reward_people = reward_people.replace(",", "")
            reward_people = reward_people.replace("'", "")
          inventory[str(ctx.message.author.id)][currency.lower()]['amt'] -= amt
          savedb(inventory)
          await ctx.send(f"{rain} it's getting wet in here!!!\n\n{inventory[senderID][currency.lower()]['emoji']} <@{senderID}> dropped {amount} (~${dollaramt}) {inventory[senderID][currency.lower()]['symbol']}\n\nCollected By\nEveryone in <@&{role.id}> ({totalpeople} People)\n\nReward\n**{round(rewardamt, 6)} {currency.upper()}** each!")
          databasebackup()
          return
      elif confirm.content.lower() == "no":
        pending_trxs -= 1
        embed = E(title=f":cry: Rain Canceled", description=f"The rain for **{amt} {currency.upper()}** has been canceled!", color=red)
        await ctx.send(embed=embed)
        return 
    else:
      rewarded = []
      pool = 0
      if inventory[senderID][currency.lower()]['amt'] < amt:
        embed = E(title=f"{wrong} Fund Error", description=f"{ctx.message.author.mention} You do not have enough funds in your wallet to send {amount} {currency}!", color=red)
        await ctx.send(embed=embed)
        return
      inventory[senderID][currency.lower()]['amt'] -= amt
      for member in tip_here:
        pool += 1
      pool = int(pool)
      rewardamt = amt/pool
      if True:
        indexpos = 0
        totalpeople = 0
        for member in tip_here:
          ID = str(tip_here[indexpos])
          if ID == ctx.author.id or ID == '909016596180246540':
            pass
          indexpos += 1
          totalpeople += 1
          if ID not in rewarded:
            rewarded.append(ID)
            inventory = opendb()
            inventory[str(ID)][currency.lower()]['amt'] += float(rewardamt) 
            savedb(inventory)
        reward_people = re.sub(r'(\d+)', r'<@\1>', str(rewarded))
        reward_people = reward_people.strip("[]") 
        reward_people = reward_people.replace(",", "")
        reward_people = reward_people.replace("'", "")
        inventory[str(ctx.message.author.id)][currency.lower()]['amt'] -= amt
        savedb(inventory)
        await ctx.send(f"{rain} it's getting wet in here!!!\n\n{inventory[senderID][currency.lower()]['emoji']} <@{senderID}> dropped {amount} (~${dollaramt}) {inventory[senderID][currency.lower()]['symbol']}\n\nCollected By\nEveryone in <@&{role.id}> ({totalpeople} People)\n\nReward\n**{round(rewardamt, 6)} {currency.upper()}** each!")
        databasebackup()
        return

@client.group(invoke_without_command=True)
async def tip(ctx, member:discord.Member=None, amt=None, *,currency=None):
  databasebackup()
  if member in currencies:
    embed = E(title=f"{wrong} Error", description=f"You must specify who you want to tip!!\nUsage: `{prefix}tip @baby chrome [amount] [currency]`", color=red)
    await ctx.send(embed=embed) 
    return
  elif amt in currencies:
    embed = E(title=f"{wrong} Error", description=f"You must specify how much you want to tip!!\nUsage: `{prefix}tip @baby chrome [amount] [currency]`", color=red)
    await ctx.send(embed=embed)
    return
  elif currency == None:
    embed = E(title=f"{wrong} Error", description=f"You must specify what currency you want to tip!\nUsage: `{prefix}tip @baby chrome [amount] [currency]`", color=red)
    await ctx.send(embed=embed)
    return
  neg_detectin = "-"
  if neg_detectin in str(amt):
    embed=E(title=f"{wrong} Negative Tipping", description=f"You cannot tip negative amounts!", color=red)
    await ctx.send(embed=embed)
    return
  if str(amt) == "penny":
    amt = "$0.01"
  if str(amt) == "dime":
    amt = "$0.10"
  if currency.lower() == "globe":
    currency = "glb"
  if currency.lower() == "kitsune":
    currency = "sina"
  if currency.lower() == 'ethereum':
    currency = 'eth'
  if currency.lower() == 'bitcoin':
    currency = 'btc'
  if currency.lower() == 'jolt':
    currency = 'jlt'
  if currency.lower() == 'joltclassic':
    currency = 'jlc'
  if currency.lower() == "jetoken":
    currency = "jet"
  if currency.lower() == "morphine":
    currency = "mrp"

  
  global pending_trxs
  if TRX_lock == True:
    embed = E(title=f"{wrong} Bot preparing for maintenance!", description=f"{ctx.message.author.mention}, This bot is in preperation to restart all further transactions from here on will be blocked untill the bot is restarted! This is a feature we added so we can insure our users that their data will not be lost!", color=red)
    await ctx.send(embed=embed)
    return
  if currency.lower() == "st" or currency.lower() == "slicktoken":
    await ctx.send("ST is no longer supported on this bot!")
    return
  id = str(ctx.message.author.id)
  blacklist = openblacklist()
  if id in blacklist:
    b_status = blacklist[id]["blacklisted"]["status"]
    if b_status == True:
      print(f"{ctx.message.author}, ({ctx.message.author.id}) tried to tip! BLACKLISTED USER!!!")
      embed = E(title=f"{wrong} Account Blacklisted!", description=f"Your account is locked and under review by administrators! For more info you can join the support server (https://discord.gg/nCtGsxfrAu) or you can run the **.team** command to get the full list of all the moderaters contact information!", color=red)
      await ctx.send(embed=embed)
      return
  id = str(ctx.message.author.id)
  
  if str(ctx.message.author) == str(member):
    embed = E(title=f"{wrong} Message Use Error!", description=f"{ctx.message.author}, you cannot Tip yourself!", color=red)
    await ctx.send(embed=embed)
    return
  senderID = str(ctx.author.id)  
  receiverID = str(member.id)
  inventory = opendb()
  dollar_sign = "$"
  if senderID not in inventory:
    ID = senderID
    createaccount(ID)
  elif receiverID not in inventory:
    ID = receiverID
    createaccount(ID)
  
  if isinstance(ctx.channel, discord.channel.DMChannel):
    embed = E(title=f"{wrong} Error", description=f"You can only use this command in a server!!", color=red)
    await ctx.send(embed=embed)
    return
  
  if amt.lower() == "all":
    inventory = opendb()
    ab = '$0.001'
    amt1 = convertusdtocurrency(ab, currency)
    amt = inventory[senderID][currency.lower()]['amt']
    amt = amt - amt1
    amt = amt

  elif dollar_sign in amt:
    amt = convertusdtocurrency(amt, currency)


  channel = client.get_channel(942185720615931904)

  amt=float(amt)



  inventory = opendb()
  if currency.lower() in currencies:
    dollaramt = convertcurrencytousd(amt, currency)
    amt = (round(amt,6))
    amount = (round(amt,6))
    amount = float(amount)
    if dollaramt < 0.0:
      embed=E(title=f"{wrong} Amount Too Low!", description=f"You must tip at least $0.0001 in {currency.upper()}!", color=red)
      await ctx.send(embed=embed)
      return

    confirmlimit = 10
    if amt > inventory[senderID][currency.lower()]['amt']:
      embed = E(title=f"{wrong} Fund Error", description=f"{ctx.message.author.mention} You do not have enough funds in your wallet to send {amount} {currency}!", color=red)
      await ctx.send(embed=embed)
      return
    amount = convertnotation(amount, 6)
    if int(dollaramt) > confirmlimit:
      warningembed = E(title=f"**Confirmaton**", description=f"{ctx.message.author.mention} Are you sure you want to send **{amount} {currency}** (**~${dollaramt}**) to {member.mention}?", color=blue)
      warningembed.set_footer(text="please reply with Yes or No")
      await ctx.send(embed=warningembed)
      def check(confirm):
        return confirm.author == ctx.author and confirm.channel == ctx.channel and confirm.content in ["Yes", "No", "no", "yes"]
      confirm = await client.wait_for('message', check=check)

      if confirm.content.lower() == "yes":
        if inventory[senderID][currency.lower()]['amt'] < amt:
          embed = E(title=f"{wrong} Fund Error", description=f"{ctx.message.author.mention} You do not have enough funds in your wallet to send {amount} {currency}!", color=red)
          await ctx.send(embed=embed)
          return
        else:
          
          inventory[str(senderID)][currency.lower()]['amt'] -= amt
          inventory[str(receiverID)][currency.lower()]['amt'] += amt
          amt = convertnotation(amt, 6)
          await ctx.send(f"{inventory[senderID][currency.lower()]['emoji']} <@{senderID}> sent <@{receiverID}> {amt} (~${dollaramt}) {inventory[senderID][currency.lower()]['symbol']}")
          savedb(inventory)
          embed = E(title=f"Transaction", description=f"New tip from <@{senderID}> ({senderID}) to <@{receiverID}> ({receiverID})\nAmount:{amt} {currency.lower()}(~${dollaramt})\nSenders Bal:{inventory[str(senderID)][currency.lower()]['amt']}\nRecievers Bal:{inventory[str(receiverID)][currency.lower()]['amt']}")
          await channel.send(embed=embed)
          
          return

      elif confirm.content.lower() == "no":
        pending_trxs -= 1
        embed = E(title=f"{wrong} Tip Canceled", description=f"The tip for {amt} {currency} has been canceled!", color=red)
        await ctx.send(embed=embed)
        return 
    if inventory[senderID][currency.lower()]['amt'] < amt:
      embed = E(title=f"{wrong} Fund Error", description=f"{ctx.message.author.mention} You do not have enough funds in your wallet to send {amt} {currency}!", color=red)
      await ctx.send(embed=embed)
      return
    else:
      inventory[str(senderID)][currency.lower()]['amt'] -= amt
      inventory[str(receiverID)][currency.lower()]['amt'] += amt
      amt = convertnotation(amt, 6)
      await ctx.send(f"{inventory[senderID][currency.lower()]['emoji']} <@{senderID}> sent <@{receiverID}> {amt} (~${dollaramt}) {inventory[senderID][currency.lower()]['symbol']}")
      savedb(inventory)
      embed = E(title=f"Transaction", description=f"New tip from <@{senderID}> ({senderID}) to <@{receiverID}> ({receiverID})\nAmount:{amt} {currency.lower()}(~${dollaramt})\nSenders Bal:{inventory[str(senderID)][currency.lower()]['amt']}\nRecievers Bal:{inventory[str(receiverID)][currency.lower()]['amt']}")
      await channel.send(embed=embed)
  else:
    Embed=E(title=f"{wrong} Currency Not Supported", description=f"{currency} is either not a currency we support, there is a typo in your message, or that currency does not exist.", color=red)
    
  pending_trxs -= 1




@client.command(aliases=["tt"])
async def totaltips(ctx):
  with open('dbs/tips.json') as f: 
    fulltips = json.load(f) 
    bot = str(client.user.id)
    amt = fulltips[bot]
  Embed=E(title=f"Total Tips", description=f"A total of **${amt}** tips have happened on **Jolt Wallet**", color=green)
  Embed.set_footer(text="Calculated from 18/10/2021(UK standard)")
  await ctx.send(embed=Embed)


@tip.command()
async def stats(ctx):
  with open('dbs/tipstatssent.json') as f: 
    tipstats = json.load(f) 
  id = str(ctx.author.id)
  with open('dbs/tipstatsre.json') as f: 
    stats = json.load(f)   
  id = str(ctx.author.id)
  if id not in tipstats:
    if id not in stats:

      Embed=E(title=f"{ctx.author}'s tip stats", description=f"**Recieved** = $0.00 \n**Sent** = $0.00", color=green)
      await ctx.send(embed=Embed)
      return
    else:
      reamt = stats[id]
      Embed=E(title=f"{ctx.author}'s tip stats", description=f"**Recieved** = ${round(reamt, 4)} \n**Sent** = $0.00", color=green)
      await ctx.send(embed=Embed)
  else:
    if id not in stats:
      sentamt = tipstats[id]
      Embed=E(title=f"{ctx.author}'s tip stats", description=f"**Recieved** = $0.00 \n**Sent** = ${round(sentamt, 4)}", color=green)
      await ctx.send(embed=Embed)
    else:
      sentamt = tipstats[id]
      reamt = stats[id]
      Embed=E(title=f"{ctx.author}'s tip stats", description=f"**Recieved** = ${round(reamt, 4)}\n**Sent** = ${round(sentamt, 4)}", color=blue)
      await ctx.send(embed=Embed)


@client.command()
async def admin(ctx, ID):
  if len(ID) != 18:
    await ctx.send(f"{wrong} Please enter a USERID!")
    return
  if ID == "":
    await ctx.send("PLEASE SEND AN ID!!")
    return
  if ID in admins:
    await ctx.send(f"<@{id}> is already an admin!")
  if ctx.message.author.id not in admins:

    await ctx.send("Missing permisons!")
    return
  member = int(ID)
  admins.append(member)
  await ctx.send(f"You have added <@{member}> as a admin!")
  return

@client.command()
async def convert(ctx, amt ,*, currency=None):
  getliveprices()
  if currency not in currencies:
    try:
      dURL = f'https://api.coingecko.com/api/v3/simple/price?ids={currency.lower()}&vs_currencies=usd'
      stats_= requests.get(dURL)
      json_stats_ = stats_.json()
      Price = float(json_stats_[f"{currency.lower()}"]["usd"])      
      Embed=E(title=f"{amt} {currency} is worth..", description=f"${Price}", colour=discord.Colour(0x2c2f33))
      await ctx.send(embed=Embed)
      return
    except Exception as e:
      embed = E(title=f"{wrong} Error!", description=f"That currency may not be valid or not listed on the bot!", color=red)
      await ctx.send(embed=embed)
      return 
  if currency == None:
    currency = 'jlc'
  elif currency == 'globe':
    currency = 'glb'
  elif currency == 'bitcoin':
    currency = 'btc'
  elif currency == 'morphine':
    currency = 'mrp'
  if amt.startswith('$'):
    amount = amt
    amt = convertusdtocurrency(amount, currency)
    amt = (round(amt, 6))
  if currency.lower() in currencies:
    dollaramt = convertcurrencytousd(amt, currency)
  if currency.lower() == "globe":
    currency = "glb"
  if currency.lower() in currencies:
    if currency.lower() == "jolt":
      Embed=E(title=f"{jolt} {amt} {currency} is worth..", description=f"${dollaramt}", colour=discord.Colour(0x2c2f33))
      await ctx.send(embed=Embed)
    elif currency.lower() == "jlt":
      Embed=E(title=f"{jolt} {amt} {currency} is worth..", description=f"${dollaramt}", colour=discord.Colour(0x2c2f33))
      await ctx.send(embed=Embed)
    elif currency.lower() == "joltclassic":
      Embed=E(title=f"{joltclassic} {amt} {currency} is worth..", description=f"${dollaramt}", colour=discord.Colour(0xa161d5))
      await ctx.send(embed=Embed)
    elif currency.lower() == "jlc":
      Embed=E(title=f"{joltclassic} {amt} {currency} is worth..", description=f"${dollaramt}", colour=discord.Colour(0xa161d5))
      await ctx.send(embed=Embed)
    elif currency.lower() == "bnb":
      Embed = E(color=0xe8d552)
      Embed=E(title=f"{bnb} {amt} {currency} is worth..", description=f"${dollaramt}", colour=discord.Colour(0xe8d552))
      await ctx.send(embed=Embed)
    elif currency.lower() == "capt":
      Embed=E(title=f"{capt} {amt} {currency} is worth..", description=f"${dollaramt}", color=blue)
      await ctx.send(embed=Embed)
    elif currency.lower() == "busd":
      Embed=E(title=f" {BinanceUSD} {amt} {currency} is worth..", description=f"${dollaramt}", color=blue)
      await ctx.send(embed=Embed)
    elif currency.lower() == "shiba":
      Embed=E(title=f" {ShibaInu} {amt} {currency} is worth..", description=f"${dollaramt}", color=blue)
      await ctx.send(embed=Embed)
    elif currency.lower() == "kitsune":
      Embed=E(title=f" {KitsuneToken} {amt} {currency} is worth..", description=f"${dollaramt}", color=blue)
      await ctx.send(embed=Embed)
    elif currency.lower() == "glb":
      Embed=E(title=f" {globeToken} {amt} {currency} is worth..", description=f"${dollaramt}", color=blue)
      await ctx.send(embed=Embed)
    elif currency.lower() == "eth":
      Embed=E(title=f" {ethToken} {amt} {currency} is worth..", description=f"${dollaramt}", color=blue)
      await ctx.send(embed=Embed)
    elif currency.lower() == "matic":
      Embed=E(title=f" {Polygon} {amt} {currency} is worth..", description=f"${dollaramt}", color=blue)
      await ctx.send(embed=Embed)
    elif currency.lower() == "nano":
      Embed=E(title=f" {nano} {amt} {currency} is worth..", description=f"${dollaramt}", color=blue)
      await ctx.send(embed=Embed)
    elif currency.lower() == "st":
      Embed=E(title=f" {st} {amt} {currency} is worth..", description=f"${dollaramt}", color=blue)
      await ctx.send(embed=Embed)
    elif currency.lower() == "btc":
      Embed=E(title=f" {btc} {amt} {currency} is worth..", description=f"${dollaramt}", color=blue)
      await ctx.send(embed=Embed)
    elif currency.lower() == "jet":
      Embed=E(title=f" {jetokenToken} {amt} {currency} is worth..", description=f"${dollaramt}", color=blue)
      await ctx.send(embed=Embed)
    elif currency.lower() == "mrp":
      Embed=E(title=f" {MorphineToken} {amt} {currency} is worth..", description=f"${dollaramt}", color=blue)
      await ctx.send(embed=Embed)






@client.command(aliases=["balances"])
async def bals(ctx):

  id = str(ctx.message.author.id)
  blacklist = openblacklist()
  if id in blacklist:
    b_status = blacklist[id]["blacklisted"]["status"]
    if b_status == True:
      print(f"{ctx.message.author}, ({ctx.message.author.id}) tried to withdraw! BLACKLISTED USER!!!")
      embed = E(title=f"{wrong} Account Blacklisted!", description=f"Your account is locked and under review by administrators! For more info you can join the support server (https://discord.gg/nCtGsxfrAu) or you can run the **.team** command to get the full list of all the moderaters contact information!", color=red)
      await ctx.send(embed=embed)
      return
  user = ctx.author
  ID = str(user.id)
  id = str(ctx.message.author.id)
  inventory = opendb()

  if id not in inventory:
    createaccount(id)
  if ID not in inventory:
    createaccount(ID)
  user = ctx.author
  ID = str(user.id)
  inventory = opendb()
  if ID in inventory:
    Embed=E(color=blue)
    Embed.set_author(name=f"{user.name}'s balances", icon_url=user.avatar_url)
    Embed.set_footer(text="Prices provided by CoinGecko")
    #step 8 add Jolt Classic to bal check!
    totall = round(inventory[ID]['bnb']['amt'] * bnbPrice, 2) + round(inventory[ID]['capt']['amt'] * captPrice, 2) + round(inventory[ID]['jlt']['amt'] * jltPrice, 6) + round(inventory[ID]['jlc']['amt'] * jlcPrice, 2) + round(inventory[ID]['busd']['amt'] * busdPrice, 2) + round(inventory[ID]['Shiba']['amt'] * shibaPrice, 2) + round(inventory[ID]['sina']['amt'] * sinaPrice, 2) + round(inventory[ID]['glb']['amt'] * glbPrice, 2)+ round(inventory[ID]['eth']['amt'] * ethPrice, 2)+ round(inventory[ID]['matic']['amt'] * maticPrice, 2)+ round(inventory[ID]['nano']['amt'] * nanoPrice, 2) + round(inventory[ID]['btc']['amt'] * bitcoinPrice) + round(inventory[ID]['jet']['amt'] * jetokenPrice, 2)+ round(inventory[ID]['mrp']['amt'] * morphinePrice, 2)

    total = round(totall,2)
    for currency in inventory[ID]:
      if currency == "bnb":
        if inventory[ID][currency]['amt'] == 0.0:
          pass
        else:
          num = '%f' % (inventory[ID][currency]['amt'])
          Embed.add_field(name=inventory[ID][currency]["name"], value=f"{inventory[ID][currency]['emoji']} **{num} {inventory[ID][currency]['symbol']}**\n( ≈ ${round(float(float((inventory[ID][currency]['amt'])) * bnbPrice), 6):,})")
      if currency == "btc":
        if inventory[ID][currency]['amt'] == 0.0:
          pass
        else:
          num = '%f' % (inventory[ID][currency]['amt'])
          Embed.add_field(name=inventory[ID][currency]["name"], value=f"{inventory[ID][currency]['emoji']} **{num} {inventory[ID][currency]['symbol']}**\n( ≈ ${round(float(float((inventory[ID][currency]['amt'])) * bitcoinPrice), 6):,})")
      if currency == "capt":
        if inventory[ID][currency]['amt'] == 0.0:
          pass
        else:
          num = '%f' % (inventory[ID][currency]['amt'])
          Embed.add_field(name=inventory[ID][currency]["name"], value=f"{inventory[ID][currency]['emoji']} **{(round(inventory[ID][currency]['amt'], 6)):,} {inventory[ID][currency]['symbol']}**\n( ≈ ${round(float((inventory[ID][currency]['amt']) * captPrice), 2):,})")
      if currency == "jlt":
        if inventory[ID][currency]['amt'] == 0.0:
          pass
        else:
          num = '%f' % (inventory[ID][currency]['amt'])         
          Embed.add_field(name=inventory[ID][currency]["name"], value=f"{inventory[ID][currency]['emoji']} **{(round(inventory[ID][currency]['amt'], 6)):,} {inventory[ID][currency]['symbol']}**\n( ≈ ${round(float((inventory[ID][currency]['amt']) * jltPrice), 6):,})") # that just rounds them farther. ah
      if currency == "jlc":
        if inventory[ID][currency]['amt'] == 0.0:
          pass
        else:
          num = '%f' % (inventory[ID][currency]['amt'])         
          Embed.add_field(name=inventory[ID][currency]["name"], value=f"{inventory[ID][currency]['emoji']} **{(round(inventory[ID][currency]['amt'], 6)):,} {inventory[ID][currency]['symbol']}**\n( ≈ ${round(float((inventory[ID][currency]['amt']) * jlcPrice), 2):,})")
      if currency == "busd":
        if inventory[ID][currency]['amt'] == 0.0:
          pass
        else:
          num = '%f' % (inventory[ID][currency]['amt'])         
          Embed.add_field(name=inventory[ID][currency]["name"], value=f"{inventory[ID][currency]['emoji']} **{(round(inventory[ID][currency]['amt'], 6)):,} {inventory[ID][currency]['symbol']}**\n( ≈ ${round(float((inventory[ID][currency]['amt']) * busdPrice), 2):,})")
      if currency == "glb":
        if inventory[ID][currency]['amt'] == 0.0:
          pass
        else:
          num = '%f' % (inventory[ID][currency]['amt'])         
          Embed.add_field(name=inventory[ID][currency]["name"], value=f"{inventory[ID][currency]['emoji']} **{(round(inventory[ID][currency]['amt'], 6)):,} {inventory[ID][currency]['symbol']}**\n( ≈ ${round(float((inventory[ID][currency]['amt']) * glbPrice), 2):,})")
      if currency == "Shiba":
        if inventory[ID][currency]['amt'] == 0.0:
          pass
        else:
          num = '%f' % (inventory[ID][currency]['amt'])         
          Embed.add_field(name=inventory[ID][currency]["name"], value=f"{inventory[ID][currency]['emoji']} **{(round(inventory[ID][currency]['amt'], 6)):,} {inventory[ID][currency]['symbol']}**\n( ≈ ${round(float((inventory[ID][currency]['amt']) * shibaPrice), 2):,})")
      if currency == "sina":
        if inventory[ID][currency]['amt'] == 0.0:
          pass
        else:
          num = '%f' % (inventory[ID][currency]['amt'])         
          Embed.add_field(name=inventory[ID][currency]["name"], value=f"{inventory[ID][currency]['emoji']} **{(round(inventory[ID][currency]['amt'], 6)):,} {inventory[ID][currency]['symbol']}**\n( ≈ ${round(float((inventory[ID][currency]['amt']) * sinaPrice), 2):,})")
      if currency == "eth":
        if inventory[ID][currency]['amt'] == 0.0:
          pass
        else:
          num = '%f' % (inventory[ID][currency]['amt'])         
          Embed.add_field(name=inventory[ID][currency]["name"], value=f"{inventory[ID][currency]['emoji']} **{(round(inventory[ID][currency]['amt'], 6)):,} {inventory[ID][currency]['symbol']}**\n( ≈ ${round(float((inventory[ID][currency]['amt']) * ethPrice), 2):,})")
      if currency == "matic":
        if inventory[ID][currency]['amt'] == 0.0:
          pass
        else:
          num = '%f' % (inventory[ID][currency]['amt'])         
          Embed.add_field(name=inventory[ID][currency]["name"], value=f"{inventory[ID][currency]['emoji']} **{(round(inventory[ID][currency]['amt'], 6)):,} {inventory[ID][currency]['symbol']}**\n( ≈ ${round(float((inventory[ID][currency]['amt']) * maticPrice), 2):,})")
      if currency == "mrp":
        if inventory[ID][currency]['amt'] == 0.0:
          pass
        else:
          num = '%f' % (inventory[ID][currency]['amt'])         
          Embed.add_field(name=inventory[ID][currency]["name"], value=f"{inventory[ID][currency]['emoji']} **{(round(inventory[ID][currency]['amt'], 6)):,} {inventory[ID][currency]['symbol']}**\n( ≈ ${round(float((inventory[ID][currency]['amt']) * morphinePrice), 2):,})")
      if currency == "nano":
        if inventory[ID][currency]['amt'] == 0.0:
          pass
        else:
          if inventory[ID][currency]['amt'] > 100:
            display_this = "(round(inventory[ID][currency]['amt'], 6)):,"
          else:
            display_this = convertnotation(inventory[ID][currency]['amt'], 6)
          num = '%f' % (inventory[ID][currency]['amt'])
          Embed.add_field(name=inventory[ID][currency]["name"], value=f"{inventory[ID][currency]['emoji']} **{display_this} {inventory[ID][currency]['symbol']}**\n( ≈ ${round(float((inventory[ID][currency]['amt']) * nanoPrice), 2):,})")
      if currency == "st":
        if inventory[ID][currency]['amt'] == 0.0:
          pass
        else:
          pass
      if currency == "jetoken":
        if inventory[ID][currency]['amt'] == 0.0:
          pass
        else:
          num = '%f' % (inventory[ID][currency]['amt'])         
          Embed.add_field(name=inventory[ID][currency]["name"], value=f"{inventory[ID][currency]['emoji']} **{(round(inventory[ID][currency]['amt'], 6)):,} {inventory[ID][currency]['symbol']}**\n( ≈ ${round(float((inventory[ID][currency]['amt']) * jetokenPrice), 2):,})")
    Embed.add_field(name="Estimated total (USD)", value=f"**${total}**", inline=False)
  Text = await ctx.reply(embed=Embed)
  if isinstance(ctx.channel, discord.channel.DMChannel):
    return
  else:
    right_emoji = "➡️"
    left_emoji = "⬅️" 
    await Text.add_reaction(emoji=animatedx)
    await asyncio.sleep(0.01)
    def check(reaction, user):
      return user == ctx.author or user.id in admins and reaction.emoji == animatedx and reaction.message == Text
    reaction, user = await client.wait_for("reaction_add", check=check)
    if user.id == ctx.message.author.id:
      await Text.delete()
      await ctx.message.delete()
    elif user.id in admins: 
      await Text.delete()
      await ctx.message.delete()
    else:
      pass










@client.command()
@commands.cooldown(1, 7200, commands.BucketType.user)
async def faucet(ctx, currency: str=None):
  if TRX_lock == True:
    embed = E(title=f"{wrong} Bot preparing for maintenance!", descripiton=f"{ctx.message.author.mention}, This bot is in preperation to restart all further transactions from here on will be blocked untill the bot is restarted! This is a feature we added so we can insure our users that their data will not be lost!", color=red)
    await ctx.send(embed=embed)
    return
  if isinstance(ctx.channel, discord.channel.DMChannel):
    embed = E(title=f"{wrong} Usage Error!", description=f"You cannot use this command in direct messages!", color=red)
    await ctx.send(embed=embed)
    faucet.reset_cooldown(ctx)
    return

  if currency == None:
    embed = E(title=f"{wrong} Error!", description=f"Please provide a currency to faucet!", color=red)
    await ctx.send(embed=embed)
    faucet.reset_cooldown(ctx)
    return 
  id = str(ctx.message.author.id)
  blacklist = openblacklist()
  if id in blacklist:
    b_status = blacklist[id]["blacklisted"]["status"]
    if b_status == True:
      print(f"{ctx.message.author}, ({ctx.message.author.id}) tried to withdraw! BLACKLISTED USER!!!")
      embed = E(title=f"{wrong} Account Blacklisted!", description=f"Your account is locked and under review by administrators! For more info you can join the support server (https://discord.gg/nCtGsxfrAu) or you can run the **.team** command to get the full list of all the moderaters contact information!", color=red)
      await ctx.send(embed=embed)
      return
  if currency.lower() == 'joltclassic':
    currency = 'jlc'
  elif currency.lower() == 'jolt':
    currency = 'jlt'
  elif currency.lower() == 'globe':
    currency = 'glb'
  elif currency.lower() == 'ethereum':
    currency = 'eth'
  elif currency.lower() == 'slicktoken':
    currency = 'st'
  elif currency.lower() == 'bitcoin':
    currency = 'btc'
  elif currency.lower() == 'jetoken':
    currency = 'btc'
  elif currency.lower() == 'morphine':
    currency = 'mrp'
  #step 9 add to faucet list!
  id = str(ctx.message.author.id)
  inventory = opendb()
  if id not in inventory:
    ID = str(ctx.message.author.id)
    createaccount(ID)
    pass
  
  # This function adds two numbers
  def add(x, y):
      return x + y
  guild = client.get_guild(899102396423209011)
  boosterrole = discord.utils.get(guild.roles, name="Server Booster")
  if boosterrole in ctx.author.roles:
    amount = '$0.001'
    streward = 0.45
    await ctx.author.send('You have recived an extra reward of **10x** ($0.001) as you are a server booster!\nThankyou for supporting jolt wallet!')
  else:
    amount = '$0.0001'
    streward = 0.17
  if currency in currencies:
    amt = convertusdtocurrency(amount, currency)  
    amt = round(amt,6)
  n1 = random.randint(1,20)
  n2 = random.randint(1,20)
  answer = add(n1, n2)
  function = '+' 
  channel = client.get_channel(942185720615931904)

  

  if id in inventory:
    if currency == None:
      embed = E(title=f"{wrong} Faucet Error", description=f"{ctx.message.author.mention} You must define the currency you want to faucet!", color=red)
      await ctx.send(embed=embed)
      faucet.reset_cooldown(ctx)
    elif currency not in currencies:
      embed = E(title=f"{wrong} Currency not found!", description=f"The currency you specified was not found, please type **{prefix}tokens** to check listed tokens!", color=red)
      await ctx.send(embed=embed)
      faucet.reset_cooldown(ctx) 
  
    elif currency.lower() == "jlt":
      embed = E(title=f"Faucet verification!", description=f'{ctx.author.mention}, What is `{n1} {function} {n2}`?', color=green)
      await ctx.send(embed=embed)
      def check(reward):
        return reward.author == ctx.author and reward.channel == ctx.channel
      try:
        reward = await client.wait_for('message', check=check, timeout=120)
          
        if int(reward.content) == answer:
          embed = E(title=f":white_check_mark: Jolt Faucet", description=f"{ctx.message.author.mention} has fauceted {amt} Jolt!", color=green)
          inventory = opendb()
          inventory[id]['jlt']['amt'] += amt
          savedb(inventory)
          await ctx.send(embed=embed)
          embed = E(title=f"Faucet claim", description=f"Faucet Claim from {ctx.author}({ctx.author.id})\nAmount:{amt} {currency.lower()}\nUsers Bal:{inventory[str(id)][currency.lower()]['amt']}")
          await channel.send(embed=embed)
        else:
          embed = E(title=f"{wrong} Command Cancelled", description=f"Your answer is incorrect!", color=red)
          await ctx.reply(embed=embed)   
          return
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Cancelled", description=f"You took to long to respond with your answer", color=red)
        await ctx.reply(embed=embed)
        return    
      else:
        pass
    elif currency.lower() ==  "mrp":
      embed = E(title=f"Faucet verification!", description=f'{ctx.author.mention}, What is {n1} {function} {n2}?', color=green)
      await ctx.send(embed=embed)
      def check(reward):
        return reward.author == ctx.author and reward.channel == ctx.channel
      try:
        reward = await client.wait_for('message', check=check, timeout=120)

        if int(reward.content) == answer:
          streward = 0.1
          embed = E(title=f":white_check_mark: Morphine Faucet", description=f"{ctx.message.author.mention} has fauceted {streward} Morphine!", color=green)
          inventory = opendb()
          inventory[id]['mrp']['amt'] += streward
          savedb(inventory)
          await ctx.send(embed=embed)
          embed = E(title=f"Faucet claim", description=f"Faucet Claim from {ctx.author}({ctx.author.id})\nAmount:{amt} {currency.lower()}\nUsers Bal:{inventory[str(id)][currency.lower()]['amt']}")
          await channel.send(embed=embed)
        else:
          embed = E(title=f"{wrong} Command Cancelled", description=f"Your answer is incorrect!", color=red)
          await ctx.reply(embed=embed)
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Cancelled", description=f"You took to long to respond with your answer", color=red)
        await ctx.reply(embed=embed)
        return
      else:
        pass
    elif currency.lower() == "glb":
      embed = E(title=f"Faucet verification!", description=f'{ctx.author.mention}, What is {n1} {function} {n2}?', color=green)
      await ctx.send(embed=embed)
      def check(reward):
        return reward.author == ctx.author and reward.channel == ctx.channel
      try:
        reward = await client.wait_for('message', check=check, timeout=120)

        if int(reward.content) == answer:
          embed = E(title=f":white_check_mark: Globe Token Faucet", description=f"{ctx.message.author.mention} has fauceted {amt} Globe!", color=green)
          inventory = opendb()
          inventory[id]['glb']['amt'] += amt
          savedb(inventory)
          await ctx.send(embed=embed)
          embed = E(title=f"Faucet claim", description=f"Faucet Claim from {ctx.author}({ctx.author.id})\nAmount:{amt} {currency.lower()}\nUsers Bal:{inventory[str(id)][currency.lower()]['amt']}")
          await channel.send(embed=embed)          
        else:
          embed = E(title=f"{wrong} Command Cancelled", description=f"Your answer is incorrect!", color=red)
          await ctx.reply(embed=embed)
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Cancelled", description=f"You took to long to respond with your answer", color=red)
        await ctx.reply(embed=embed)
        return
      else:
        pass
    elif currency.lower() == "st":
      embed = E(title=f"Faucet verification!", description=f'{ctx.author.mention}, What is {n1} {function} {n2}?', color=green)
      await ctx.send(embed=embed)
      def check(reward):
        return reward.author == ctx.author and reward.channel == ctx.channel
      try:
        reward = await client.wait_for('message', check=check, timeout=120)

        if int(reward.content) == answer:
          embed = E(title=f":white_check_mark: SlickToken Faucet", description=f"{ctx.message.author.mention} has fauceted {streward} ST!", color=green)
          inventory = opendb()
          inventory[id]['st']['amt'] += streward
          savedb(inventory)
          await ctx.send(embed=embed)
          embed = E(title=f"Faucet claim", description=f"Faucet Claim from {ctx.author}({ctx.author.id})\nAmount:{amt} {currency.lower()}\nUsers Bal:{inventory[str(id)][currency.lower()]['amt']}")
          await channel.send(embed=embed)          
        else:
          embed = E(title=f"{wrong} Command Cancelled", description=f"Your answer is incorrect!", color=red)
          await ctx.reply(embed=embed)
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Cancelled", description=f"You took to long to respond with your answer", color=red)
        await ctx.reply(embed=embed)
        return
      else:
        pass
    elif currency.lower() == "kitsune":
      embed = E(title=f"{wrong} Empty Faucet", description=f"{ctx.message.author.mention} the kitsune faucet is empty please choose another currency to faucet!", color=red)
      await ctx.send(embed=embed)
      faucet.reset_cooldown(ctx)
    elif currency.lower() == "bnb":
      embed = E(title=f"{wrong} Empty Faucet", description=f"{ctx.message.author.mention} the bnb faucet is empty please choose another currency to faucet!", color=red)
      await ctx.send(embed=embed)
      faucet.reset_cooldown(ctx)
    elif currency.lower() == "capt":
      embed = E(title=f"{wrong} Empty Faucet", description=f"{ctx.message.author.mention} the capt faucet is empty please choose another currency to faucet!", color=red)
      await ctx.send(embed=embed)
      faucet.reset_cooldown(ctx)
    elif currency.lower() == "st":
      embed = E(title=f"{wrong} Empty Faucet", description=f"{ctx.message.author.mention} the st faucet is empty please choose another currency to faucet!", color=red)
      await ctx.send(embed=embed)
      faucet.reset_cooldown(ctx)
    elif currency.lower() == "btc":
      embed = E(title=f"{wrong} Empty Faucet", description=f"{ctx.message.author.mention} the Bitcoin faucet is empty please choose another currency to faucet!", color=red)
      await ctx.send(embed=embed)
      faucet.reset_cooldown(ctx)
    elif currency.lower() == "nano":
      embed = E(title=f"{wrong} Empty Faucet", description=f"{ctx.message.author.mention} the nano faucet is empty please choose another currency to faucet!", color=red)
      await ctx.send(embed=embed)
      faucet.reset_cooldown(ctx)
    elif currency.lower() == "mrp":
      embed = E(title=f"{wrong} Empty Faucet", description=f"{ctx.message.author.mention} the mrp faucet is empty please choose another currency to faucet!", color=red)
      await ctx.send(embed=embed)
      faucet.reset_cooldown(ctx)
    elif currency.lower() == "busd":
      embed = E(title=f"{wrong} Empty Faucet", description=f"{ctx.message.author.mention} the busd faucet is empty please choose another currency to faucet!", color=red)
      await ctx.send(embed=embed)
      faucet.reset_cooldown(ctx)
    elif currency.lower() == "shiba":
      embed = E(title=f"{wrong} Empty Faucet", description=f"{ctx.message.author.mention} the shiba faucet is empty please choose another currency to faucet!", color=red)
      await ctx.send(embed=embed)
      faucet.reset_cooldown(ctx)
    elif currency.lower() == "eth":
      embed = E(title=f"{wrong} Empty Faucet", description=f"{ctx.message.author.mention} the eth faucet is empty please choose another currency to faucet!", color=red)
      await ctx.send(embed=embed)
      faucet.reset_cooldown(ctx)
    elif currency.lower() == "matic":
      embed = E(title=f"{wrong} Empty Faucet", description=f"{ctx.message.author.mention} the MATIC faucet is empty please choose another currency to faucet!", color=red)
      await ctx.send(embed=embed)
      faucet.reset_cooldown(ctx)
    elif currency.lower() == "jetoken" or currency.lower() == "jet":
      embed = E(title=f"{wrong} Empty Faucet", description=f"{ctx.message.author.mention} the Jetoken faucet is empty please choose another currency to faucet!", color=red)
      await ctx.send(embed=embed)
      faucet.reset_cooldown(ctx)
    elif currency.lower() == "jlc":
      embed = E(title=f"Faucet verification!", description=f'{ctx.author.mention}, What is {n1} {function} {n2}?', color=green)
      await ctx.send(embed=embed)
      def check(reward):
        return reward.author == ctx.author and reward.channel == ctx.channel
      try:
        reward = await client.wait_for('message', check=check, timeout=120)

        if int(reward.content) == answer:
          embed = E(title=f":white_check_mark: Jolt Classic Faucet", description=f"{ctx.message.author.mention} has fauceted {amt} Jolt Classic!", color=green)
          inventory = opendb()
          inventory[id]['jlc']['amt'] += amt
          savedb(inventory)
          await ctx.send(embed=embed)
          embed = E(title=f"Faucet claim", description=f"Faucet Claim from {ctx.author}({ctx.author.id})\nAmount:{amt} {currency.lower()}\nUsers Bal:{inventory[str(id)][currency.lower()]['amt']}")
          await channel.send(embed=embed)          
        else:
          embed = E(title=f"{wrong} Command Cancelled", description=f"Your answer is incorrect!", color=red)
          await ctx.reply(embed=embed)
      except asyncio.exceptions.TimeoutError:
        embed = E(title=f"{wrong} Command Cancelled", description=f"You took to long to respond with your answer", color=red)
        await ctx.reply(embed=embed)
        return
      else:
        pass


  else:
    embed = E(title=f"{wrong} Account Not Found", description=f"Your account was not found please insure you have an account before you try to faucet! You can make an account by typing ```.create```", color=red)
    await ctx.send(embed=embed)
    faucet.reset_cooldown(ctx)






@client.command()
async def bal(ctx, currency='jlc'):
  id = str(ctx.message.author.id)
  currency = currency.lower()
  blacklist = openblacklist()
  if id in blacklist:
    b_status = blacklist[id]["blacklisted"]["status"]
    if b_status == True:
      print(f"{ctx.message.author}, ({ctx.message.author.id}) tried to withdraw! BLACKLISTED USER!!!")
      embed = E(title=f"{wrong} Account Blacklisted!", description=f"Your account is locked and under review by administrators! For more info you can join the support server (https://discord.gg/nCtGsxfrAu) or you can run the **.team** command to get the full list of all the moderaters contact information!", color=red)
      await ctx.send(embed=embed)
      return
  inventory = opendb()
  iD = str(ctx.author.id)

  
  if iD not in inventory:
    user = ctx.author
    ID = str(user.id)
    createaccount(ID)
  inventory = opendb()
  if currency.lower() == 'joltclassic':
    currency = "jlc"
  elif currency.lower() == 'jolt':
    currency = 'jlt'
  elif currency.lower() == "shiba":
    currency = "Shiba"
  elif currency.lower() == 'globe':
    currency = 'glb'
  elif currency.lower() == 'ethereum':
    currency = 'eth'
  elif currency.lower() == 'slicktoken':
    currency = 'st'
  elif currency.lower() == 'bitcoin':
    currency = 'btc'
  elif currency.lower() == 'jetoken':
    currency = 'jet'
  elif currency.lower() == 'morphine':
    currency = 'mrp'
  else:
    pass
  if currency==None:
    Embed = E(color=0xa161d5)
    Embed.set_author(name=f"{ctx.author.name}'s Jolt Classic wallet", icon_url=ctx.author.avatar_url)
    Embed.add_field(name="Balance", value=f"**{inventory[iD]['jlc']['emoji']} {round(inventory[iD]['jlc']['amt'], 6)} {inventory[iD]['jlc']['symbol']}** ( ≈ ${round(float((inventory[iD]['jlc']['amt']) * jlcPrice), 4):,})")
    Embed.set_footer(text=f"Try {prefix}bals to see all of your balances.")
    await ctx.send(embed=Embed)
  elif currency.lower() == 'jlt' or currency.lower() == "jolt":
    Embed = E(color=0x000000)
    Embed.set_author(name=f"{ctx.author.name}'s Jolt wallet", icon_url=ctx.author.avatar_url)
    Embed.add_field(name="Balance", value=f"**{inventory[iD]['jlt']['emoji']} {round(inventory[iD]['jlt']['amt'], 6)} {inventory[iD]['jlt']['symbol']}** ( ≈ ${round(float((inventory[iD]['jlt']['amt']) * jltPrice), 6):,})")
    Embed.set_footer(text=f"Try {prefix}bals to see all of your balances.")
    await ctx.send(embed=Embed)
  elif currency.lower() == 'jlc' or currency.lower() == "joltclassic":
    Embed = E(color=0xa161d5)
    Embed.set_author(name=f"{ctx.author.name}'s Jolt Classic wallet", icon_url=ctx.author.avatar_url)
    Embed.add_field(name="Balance", value=f"**{inventory[iD]['jlc']['emoji']} {round(inventory[iD]['jlc']['amt'], 6)} {inventory[iD]['jlc']['symbol']}** ( ≈ ${round(float((inventory[iD]['jlc']['amt']) * jlcPrice), 4):,})")
    Embed.set_footer(text=f"Try {prefix}bals to see all of your balances.")
    await ctx.send(embed=Embed)
  elif currency.lower() == 'bnb' or currency.lower() == "binance":
    Embed = E(color=0xe8d552)
    Embed.set_author(name=f"{ctx.author.name}'s BNB wallet", icon_url=ctx.author.avatar_url)
    Embed.add_field(name="Balance", value=f"**{inventory[iD]['bnb']['emoji']} {round(inventory[iD]['bnb']['amt'], 6)} {inventory[iD]['bnb']['symbol']}** ( ≈ ${round(float((inventory[iD]['bnb']['amt']) * bnbPrice), 4):,})")
    Embed.set_footer(text=f"Try {prefix}bals to see all of your balances.")
    await ctx.send(embed=Embed)
  elif currency.lower() == 'busd':
    Embed = E(color=0xe8d552)
    Embed.set_author(name=f"{ctx.author.name}'s BUSD wallet", icon_url=ctx.author.avatar_url)
    Embed.add_field(name="Balance", value=f"**{inventory[iD]['busd']['emoji']} {round(inventory[iD]['busd']['amt'], 6)} {inventory[iD]['busd']['symbol']}** ( ≈ ${round(float((inventory[iD]['busd']['amt']) * busdPrice), 4):,})")
    Embed.set_footer(text=f"Try {prefix}bals to see all of your balances.")
    await ctx.send(embed=Embed)
  elif currency.lower() == 'Shiba' or currency.lower() == "shib":
    Embed = E(color=0xfc0317)
    Embed.set_author(name=f"{ctx.author.name}'s SHIBA INU wallet", icon_url=ctx.author.avatar_url)
    Embed.add_field(name="Balance", value=f"**{inventory[iD]['Shiba']['emoji']} {round(inventory[iD]['Shiba']['amt'], 6)} {inventory[iD]['Shiba']['symbol']}** ( ≈ ${round(float((inventory[iD]['Shiba']['amt']) * shibaPrice), 4):,})")
    Embed.set_footer(text=f"Try {prefix}bals to see all of your balances.")
    await ctx.send(embed=Embed)
  elif currency.lower() == 'btc' or currency.lower() == "bitcoin":
    Embed = E(color=0xffd500)
    Embed.set_author(name=f"{ctx.author.name}'s Bitcoin wallet", icon_url=ctx.author.avatar_url)
    Embed.add_field(name="Balance", value=f"**{inventory[iD]['btc']['emoji']} {round(inventory[iD]['btc']['amt'], 6)} {inventory[iD]['btc']['symbol']}** ( ≈ ${round(float((inventory[iD]['btc']['amt']) * bitcoinPrice), 6):,})")
    Embed.set_footer(text=f"Try {prefix}bals to see all of your balances.")
    await ctx.send(embed=Embed)
  elif currency.lower() == 'capt' or currency.lower() == "captian":
    Embed = E(color=0x5a8ad3)
    Embed.set_author(name=f"{ctx.author.name}'s Captain wallet", icon_url=ctx.author.avatar_url)
    Embed.add_field(name="Balance", value=f"**{inventory[iD]['capt']['emoji']} {round(inventory[iD]['capt']['amt'], 6)} {inventory[iD]['capt']['symbol']}** ( ≈ ${round(float((inventory[iD]['capt']['amt']) * captPrice), 4):,})")
    Embed.set_footer(text=f"Try {prefix}bals to see all of your balances.")
    await ctx.send(embed=Embed)
  elif currency == 'kitsune':
    Embed = E(color=0xfc0317)
    Embed.set_author(name=f"{ctx.author.name}'s Kitsune wallet", icon_url=ctx.author.avatar_url)
    Embed.add_field(name="Balance", value=f"**{inventory[iD]['sina']['emoji']} {round(inventory[iD]['sina']['amt'], 6)} {inventory[iD]['sina']['symbol']}** ( ≈ ${round(float((inventory[iD]['sina']['amt']) * sinaPrice), 4):,})")
    Embed.set_footer(text=f"Try {prefix}bals to see all of your balances.")
    await ctx.send(embed=Embed)
  elif currency == 'glb' or currency == "globe":
    Embed = E(color=0xff6f00)
    Embed.set_author(name=f"{ctx.author.name}'s Globe wallet", icon_url=ctx.author.avatar_url)
    Embed.add_field(name="Balance", value=f"**{inventory[iD]['glb']['emoji']} {round(inventory[iD]['glb']['amt'], 6)} {inventory[iD]['glb']['symbol']}** ( ≈ ${round(float((inventory[iD]['glb']['amt']) *glbPrice), 4):,})")
    Embed.set_footer(text=f"Try {prefix}bals to see all of your balances.")
    await ctx.send(embed=Embed)
  elif currency == 'morphine' or currency == "mrp":
    Embed = E(color=0x0394fc)
    Embed.set_author(name=f"{ctx.author.name}'s Morphine wallet", icon_url=ctx.author.avatar_url)
    Embed.add_field(name="Balance", value=f"**{inventory[iD]['mrp']['emoji']} {round(inventory[iD]['mrp']['amt'], 6)} {inventory[iD]['mrp']['symbol']}** ( ≈ ${round(float((inventory[iD]['mrp']['amt']) *morphinePrice), 4):,})")
    Embed.set_footer(text=f"Try {prefix}bals to see all of your balances.")
    await ctx.send(embed=Embed)
  elif currency == 'eth':
    display_this = convertnotation(inventory[iD]['eth']['amt'], 6)
    Embed = E(color=0xa161d5)
    Embed.set_author(name=f"{ctx.author.name}'s Ethereum wallet", icon_url=ctx.author.avatar_url)
    Embed.add_field(name="Balance", value=f"**{inventory[iD]['eth']['emoji']} {display_this} ETH** ( ≈ ${round(float((inventory[iD]['eth']['amt']) *ethPrice), 4):,})")
    Embed.set_footer(text=f"Try {prefix}bals to see all of your balances.")
    await ctx.send(embed=Embed)
  elif currency == 'matic':
    display_this = convertnotation(inventory[iD]['matic']['amt'], 6)
    Embed = E(color=0xa161d5)
    Embed.set_author(name=f"{ctx.author.name}'s Polygon wallet", icon_url=ctx.author.avatar_url)
    Embed.add_field(name="Balance", value=f"**{inventory[iD]['matic']['emoji']} {display_this} MATIC** ( ≈ ${round(float((inventory[iD]['matic']['amt']) *maticPrice), 4):,})")
    Embed.set_footer(text=f"Try {prefix}bals to see all of your balances.")
    await ctx.send(embed=Embed)
  elif currency == 'nano':
    Embed = E(color=0x0f75d4)
    Embed.set_author(name=f"{ctx.author.name}'s Nano wallet", icon_url=ctx.author.avatar_url)
    display_this = convertnotation(inventory[iD]['nano']['amt'], 6)
    Embed.add_field(name="Balance", value=f"**{inventory[iD]['nano']['emoji']} {display_this} NANO** ( ≈ ${round(float((inventory[iD]['nano']['amt']) * nanoPrice), 4):,})")
    Embed.set_footer(text=f"Try {prefix}bals to see all of your balances.")
    await ctx.send(embed=Embed)
  elif currency == 'st':
    await ctx.send("slicktoken is no longer supported on this bot")
    return
    Embed = E(color=0xa161d5)
    Embed.set_author(name=f"{ctx.author.name}'s SlickToken wallet", icon_url=ctx.author.avatar_url)
    Embed.add_field(name="Balance", value=f"**{inventory[iD]['st']['emoji']} {round(inventory[iD]['st']['amt'], 6)} ST** ( ≈ ${round(float((inventory[iD]['st']['amt']) * stPrice), 4):,})")
    Embed.set_footer(text=f"Try {prefix}bals to see all of your balances.")
    await ctx.send(embed=Embed)
  elif currency == 'jet':
    Embed = E(color=0x033dfc)
    Embed.set_author(name=f"{ctx.author.name}'s Jetoken wallet", icon_url=ctx.author.avatar_url)
    Embed.add_field(name="Balance", value=f"**{inventory[iD]['jet']['emoji']} {round(inventory[iD]['jet']['amt'], 6)} JET** ( ≈ ${round(float((inventory[iD]['jet']['amt']) * jetokenPrice), 4):,})")
    Embed.set_footer(text=f"Try {prefix}bals to see all of your balances.")
    await ctx.send(embed=Embed)
  else:
    em = discord.Embed(
        title=f"{wrong}Command Error!",
        description=
        "This currency is not supported on our bot!",
        color=red)
    await ctx.send(embed=em)



def conv(time):
	pos = ["s", "m", "h", "d"]

	time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

	unit = time[-1]

	if unit not in pos:
		return -1
	try:
		val = int(time[:-1])
	except:
		return -2

	return val * time_dict[unit]

#packets done and working!

#from discord import *
# ^^ Cryptic did not have this imported 
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member , *, reason=None):
  try:
    await member.ban()
  except discord.errors.Forbidden:
    embed=E(title=f"{wrong} This user has a higher priority role than me!", description=f"{member} Cannot be Banned!", color=discord.Color.red())
    await ctx.send(embed=embed)
    return
  except Exception as err:
    embed=E(title=f"{wrong} Something in the code is not right!", description=f"{member} Cannot be Banned!\nError Thrown ```{err}```", color=discord.Color.red())
    await ctx.send(embed=embed)

  embed=E(title=f"Jolt ban logs", description=f"{member} has been banned from the server!", color=discord.Color.green())
  await ctx.send(embed=embed)

@client.command()
async def packet(ctx, amount, currency:str, time: str = '15s'):
  databasebackup()
  global TRX_lock
  global pending_trxs 
  if TRX_lock == True:
    embed = E(title=f"{wrong} Bot preparing for maintenance!", descripiton=f"{ctx.message.author.mention}, This bot is in preperation to be restart all further transactions from here on will be blocked untill the bot is restarted! This is a feature we added so we can insure our users that their data will not be lost!", color=red)
    await ctx.send(embed=embed)
    return
#  ID = client.user.id
#  openkillbot()
#  kill = killbot[ID]["killbot"]["status"]
#  if kill == True:
#    embed = E(title=f"{wrong} Bot is preparing for shutdown", description=f"This bot is in preperation to be shutdown all further transactions from here on will be blocked untill the bot is restarted! This is a feature we added so we can insure our users that their data will not be lost!", color=red)
#    await ctx.send(embed=embed)
#    return
  id = str(ctx.message.author.id)
  blacklist = openblacklist()
  if id in blacklist:
    b_status = blacklist[id]["blacklisted"]["status"]
    if b_status == True:
      print(f"{ctx.message.author}, ({ctx.message.author.id}) tried to withdraw! BLACKLISTED USER!!!")
      embed = E(title=f"{wrong} Account Blacklisted!", description=f"Your account is locked and under review by administrators! For more info you can join the support server (https://discord.gg/nCtGsxfrAu) or you can run the **.team** command to get the full list of all the moderaters contact information!", color=red)
      await ctx.send(embed=embed)
      return

  ID = str(ctx.message.author.id)
  inventory = opendb()
  if ID not in inventory:
    createaccount(ID)
  drop_id=str(ctx.author.id)
  dollar_sign = "$"
  if isinstance(ctx.channel, discord.channel.DMChannel):
    embed = E(title=f"{wrong} Error", description=f"You can only use this command in a server!!", color=red)
    await ctx.send(embed=embed)
    return
  if currency == "jolt":
    currency = "jlt"
  elif currency == 'bitcoin':
    currency == 'btc'
  elif currency == 'morphine':
    currency == 'mrp'
  if amount.lower() == "all":
    inventory = opendb()
    amount = inventory[drop_id][currency.lower()]['amt']
    amount = amount
  elif dollar_sign in amount:
    amount = convertusdtocurrency(amount, currency)
  if currency.lower() in currencies:
    amount = float(amount)
    dollaramt = convertcurrencytousd(amount, currency)
  time = conv(time)
  if time > 7200:
    embed = E(title=f"{wrong} Time Error", description=f"you cannot set a packet to be longer than 2 hours!", color=red)
    await ctx.send(embed=embed)
    return
  if time == 0:
    time = 3600
  inventory = opendb()
  if inventory[drop_id][currency.lower()]['amt'] < amount:
    embed = E(title=f"{wrong} Insufficient Funds", description=f"{ctx.message.author.mention}, You do not have enough **{currency.lower()}** to complete this transaction!", color=red)
    await ctx.send(embed=embed)
    return
  if dollaramt < 0.0001:
    embed = E(title=f"{wrong} Amount Too Small!", description=f"{ctx.message.author.mention}, you must drop at least 0.0001$ of {currency}", color=red)
    await ctx.send(embed=embed)
    return
  try:
    inventory[drop_id][str(currency)]['amt'] -= amount
    savedb(inventory)
    pending_trxs += 1
  except Exception:
    return
  customid = str(ctx.author.id)
  if customid in custom:
    if customid == '440998802527354890':
      emoji = bombreaction
    elif customid  == '755514549821767861':
      emoji = globeToken
    elif customid == '809456156149284884':
      emoji = '🖥️'
    elif customid == '851224281752666123':
      emoji = '🖥️'
    elif customid == '758488582968705064':
      emoji = rureaction
    elif customid in '663393254284328973':
      emoji = dragon
  else:
    emojis = ["✅", "😃", "🤣", "😊", "🥰", "😇", "😍", "😘"]
    emoji = random.choice(emojis)
  rabbit = ":rabbit2:"
  sad = ":cry:"
  if currency in currencies:
    if currency.lower() == "jlt":
      a_bal = 'jlt'
    elif currency.lower() == 'bnb':
      a_bal = 'bnb'
    elif currency.lower() == 'capt':
      a_bal = 'capt'
    elif currency.lower() == 'jlc':
      a_bal = 'jlc'
    elif currency.lower() == 'busd':
      a_bal = 'busd'
    elif currency.lower() == 'shiba':
      a_bal = 'shiba'
    elif currency.lower() == 'sina':
      a_bal = 'sina'
    elif currency.lower() == 'glb':
      a_bal = 'glb'
    elif currency.lower() == 'eth':
      a_bal = 'eth'
    elif currency.lower() == 'matic':
      a_bal = 'matic'
    elif currency.lower() == 'nano':
      a_bal = 'nano' 
    elif currency.lower() == 'st':
      a_bal = 'st'
    elif currency.lower() == 'btc':
      a_bal = 'btc'
    elif currency.lower() == 'mrp':
      a_bal = 'mrp'
    am = (round(amount, 6))
    embed = E(title=f"{rabbit} Fast Packet!", description=f"{ctx.message.author.mention}, Dropped a Packet for {am} {currency.upper()} (~${dollaramt})\n\n**React with the {emoji} emoji to grab the prize!**", color=green)
    embed.set_footer(text=f"Ending in {time} seconds!")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction(emoji)
    nil = 0
        
    while time > nil:
      time -= 1
      await asyncio.sleep(1)
      try:
        new_msg = await ctx.channel.fetch_message(msg.id)
        users = await new_msg.reactions[0].users().flatten()
        if TRX_lock == True:
          embed = E(title=f"{wrong} Bot preparing for maintenance!", description=f"This Packet has been refunded to the owner since the bot was scheduled for maitenence!", color=red)
          await ctx.send(embed=embed)
          pending_trxs -= 1
          return
        for user in users:
          winner = ''
          if user.id == 869390064172552192:
            pass
          elif user.id == 909016596180246540:
            pass
          elif user.id == ctx.author.id:
            pass
          else:
            winner = user.id
            time = 0
      
      except IndexError:
        pass
    if winner == '':
      pass
    else:
      winner = str(winner)
    if str(winner) == 869390064172552192:
      pass
    elif str(winner) == ctx.author.id: 
      pass
    elif winner == '':
      new_embed = E(title=f"{sad} This Fast Packet has Ended!", description=f"Nobody reacted to this packet of {am} {currency.upper()}", color=red)
      new_embed.set_footer(text='Ended:')
      await msg.edit(embed=new_embed)
      inventory[drop_id][str(currency)]['amt'] += amount
      savedb(inventory)
      pending_trxs -= 1
      return
    elif str(winner) not in inventory:
      ID = str(winner)
      #add this for the new token
      createaccount(ID)
      inventory = opendb()
      inventory[winner][a_bal]['amt'] += amount
      savedb(inventory)
      am = (round(amount, 6))
      new_embedd = E(title=f"{sad} This Packet has already been collected!", description=f"This packet of **{am} {currency.upper()}** has been collected! by <@{winner}>", color=red)
      new_embedd.set_footer(text='Ended:')
      await msg.edit(embed=new_embedd)
      pending_trxs -= 1
      return
    else:
      inventory = opendb()
      b_bal = inventory[winner][a_bal]['amt']
      inventory[winner][a_bal]['amt'] += amount
      savedb(inventory)
      am = (round(amount, 6))
      new_embedd = E(title=f"{sad} This Packet has already been collected!", description=f"<@{winner}> has collected this packet of **{am} {currency.upper()}**", color=red)
      new_embedd.set_footer(text='Ended')
      await msg.edit(embed=new_embedd)
      pending_trxs -= 1
      return
        

        
    
    new_embed = E(title=f"{sad} This Fast Packet has Ended!", description=f"Nobody reacted to this packet of {amount} {currency.upper()}", color=red)
    new_embed.set_footer(text='Ended')
    await msg.edit(embed=new_embed)
    inventory = opendb()
    inventory[drop_id][str(currency)]['amt'] += amount
    savedb(inventory)
    pending_trxs -= 1
    return
    
      

    
  else:
    
    embed = E(title=f"{wrong} Message Error", description="The currency you tried to packet is not on this bot!", color=red)
    await ctx.send(embed=embed)



for file in os.listdir("./cogs"):
  if file.endswith(".py"):
    client.load_extension(f"cogs.{file[:-3]}")



@client.command()
async def reload(ctx):
  total = 0
  files=[]
  if ctx.author.id not in admins:
    return
  else:
    for file in os.listdir("./cogs"):
      if file.endswith(".py"):
        client.unload_extension(f"cogs.{file[:-3]}")
        await asyncio.sleep(1)
        client.load_extension(f"cogs.{file[:-3]}")
        files.append(file)
        total += 1
    await ctx.send(f"Loaded a total of {total} cogs\n{files}")
        






@client.command()
async def id(ctx, user: discord.Member=None):
  if user == None:
    ID = ctx.author.id
    user = ctx.message.author
  else:
    ID = user.id
  embed1 = E(title="<a:loading:905550477511503892> Fetching ID! Please wait!")
  msg = await ctx.send(embed=embed1)
  await asyncio.sleep(2)
  embed = E(title=f"{check} ID found!", description=f"{ctx.message.author.mention}, {user} ID is: `{ID}`", color=green)
  await msg.edit(embed=embed)


def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)


@client.command(aliases=['kill'])
async def restart(ctx):
  channel = client.get_channel(942182366145835108)
  databasebackup()
  b=(time.strftime("%H:%M:%S"))
  await channel.send(f'Database Backup! (Bot is being restarted:Part1)\nTime:{b}', file=discord.File("databasebackup.txt"))
  global pending_trxs
  global TRX_lock
  await asyncio.sleep(1)
  if ctx.author.id not in admins:
    embed = E(title=f"{wrong} Missing Permissions!", description=f"{ctx.message.author.mention}, You do not have permissions to kill this bot!", color=red)
    await ctx.send(embed=embed)
    return
  else:
    TRX_lock = True
    await client.change_presence(
          status=discord.Status.idle,
          activity=discord.Game('I am preparing for a quick restart for an update!'))
    if pending_trxs > 0:

      embed = E(title=f"{warning} Some Transactions are still proccessing!", description=f"{check} we have blocked people from making further transactions! Once all the transactions have proccessed the bot will restart!\nTransactions Proccessing: {pending_trxs}", color=green)
      e_msg = await ctx.send(embed=embed)
      await client.change_presence(
            status=discord.Status.online,
            activity=discord.Game('I am preparing for a quick restart for an update!'))
      while pending_trxs > 0:
        await asyncio.sleep(5)
        new_embed = E(title=f"{warning} Some Transactions are still proccessing!", description=f"{check} we have blocked people from making further transactions! Once all the transactions have proccessed the bot will shut down!\nTransactions Proccessing: {pending_trxs}", color=green)
        await e_msg.edit(embed=new_embed)
      await client.change_presence(
            status=discord.Status.idle,
            activity=discord.Game('I am quickly restarting for maintainance!'))
      embed = E(title=f"{check} Bot Restarted!")
      await e_msg.edit(embed=embed)
      databasebackup()
      c=(time.strftime("%H:%M:%S"))
      await channel.send(f'Database Backup! (Bot is being restarted:Part2)\nTime:{c}', file=discord.File("databasebackup.txt"))
      await asyncio.sleep(0.5)
      restart_bot()
      return
    
    embed = E(title=f"{check} Restarting bot!", description=f"{ctx.message.author} the bot is restarting!", color=green)
    await ctx.send(embed=embed)
    databasebackup()
    c=(time.strftime("%H:%M:%S"))
    await channel.send(f'Database Backup! (Bot is being restarted:Part2)\nTime:{c}', file=discord.File("databasebackup.txt"))
    await asyncio.sleep(0.5)
    restart_bot()




@client.group(invoke_without_command=True)
async def help(ctx):
	em = discord.Embed(
	    title="Jolt Wallet Help",
	    description=
	    "Use `.help <Command>` for extended help on a specific command",
	    color=blue)

	em.add_field(name="Introduction",
	             value="Jolt wallet is a discord bot that allows you to tip and make payments to any Discord user with your favorite cryptocurrency!",
	             inline=False)
	em.add_field(name="Free", value="We do not take any fees when you tip users or airdrop in the bot! ", inline=False)
	em.add_field(
	    name="Easy to use!",
	    value=
	    "Jolt wallet is very easy to use! If you want to tip someone, all you need to type is `.tip [user] [amount] [currency]`!\nIf you ever need help, our developers an moderators are there! Just Dm the bot `.modmail` and follow the instructions given!\n",
	    inline=False)
	em.add_field(name="Wallet", value="Use `.help wallet` to see commands", inline=False)
	em.add_field(
	    name="Fun commands!",
	    value=
	    "Use `.help fun` for more info on fun commands!!",
	    inline=False)

	await ctx.send(embed=em)

@help.command()
async def wallet(ctx):
	em = discord.Embed(
	    title="Wallet commands",
	    description=
	    "Help on your wallet!",
	    color=blue)

	em.add_field(name="Deposit",
	             value="If you would like to send funds to your wallet, Dm the bot `.deposit [currency]` then it will send you an address to deposit that currency to! Follow that and you will recive it in your bal!",
	             inline=False)
	em.add_field(name="Withdraw", value="If you would like to take your funds out of your discord wallet, DM the bot `.deposit [currency]` This will ask you for your address and how much you want to withdraw. Follow the steps and it will be sent to the address you specified!", inline=False)
	em.add_field(
	    name="Airdrop",
	    value=
	    "To airdrop, just type `.airdrop [amount] [currency] [time]` to start a drop that everyone can collect!",
	    inline=False)
	em.add_field(name="Packet", value="To packet, just type `.packet [amount] [currency] [time]` to start a packet that anyone can collect but only the first person to do so wins!", inline=False)
	em.add_field(
	    name="Tip",
	    value=
	    "To tip someone, just type `.tip [user] [amount] [currency] [time]` to tip that user!",
	    inline=False)

	await ctx.send(embed=em)
@client.command()
async def catfact(ctx):
  r = requests.get("https://meowfacts.herokuapp.com/")
  cat_fact_json = r.json()
  cat_fact = cat_fact_json["data"]
  cat_fact = str(cat_fact)
  cat_fact = cat_fact.strip("[")
  cat_fact = cat_fact.strip("]")
  cat_fact = cat_fact.replace("'", "")
  embed=E(title=f":cat: Here is a Cat Fun Fact!", description=f"Did you know\n\n **{cat_fact}**", color=blue)
  embed.set_footer(text="Fun Fact!")
  await ctx.send(embed=embed)
  return



def createstore(ID):
  store = openstore()
  name = False
  price = False
  currency = False
  roleid  = False
  if ID not in store:
    store[ID] = {}
    store[ID]["item1"] = {}
    store[ID]["item1"]["name"] = name
    store[ID]["item1"]["number"] = '1'
    store[ID]["item1"]["price"] = price
    store[ID]["item1"]["currency"] = currency
    store[ID]["item1"]["roleid"] = roleid
    store[ID]["item2"] = {}
    store[ID]["item2"]["name"] = name
    store[ID]["item2"]["number"] = '2'
    store[ID]["item2"]["price"] = price
    store[ID]["item2"]["currency"] = currency
    store[ID]["item2"]["roleid"] = roleid
    store[ID]["item3"] = {}
    store[ID]["item3"]["name"] = name
    store[ID]["item3"]["number"] = '3'
    store[ID]["item3"]["price"] = price
    store[ID]["item3"]["currency"] = currency
    store[ID]["item3"]["roleid"] = roleid
    store[ID]["item4"] = {}
    store[ID]["item4"]["name"] = name
    store[ID]["item4"]["number"] = '4'
    store[ID]["item4"]["price"] = price
    store[ID]["item4"]["currency"] = currency
    store[ID]["item4"]["roleid"] = roleid
    store[ID]["item5"] = {}
    store[ID]["item5"]["name"] = name
    store[ID]["item5"]["number"] = '5'
    store[ID]["item5"]["price"] = price
    store[ID]["item5"]["currency"] = currency
    store[ID]["item5"]["roleid"] = roleid
    savestore(store)  
@client.group()
async def store(ctx):
  store = openstore()
  ID = str(ctx.guild.id)
  if ID not in store:
    em = discord.Embed(
        title=f"{ctx.guild}",
        description=
        "No items have been listed in the store!",
        color=red)
    await ctx.reply(embed=em)
    createstore(ID)
    return
  else:
    em = discord.Embed(
        title=f"{ctx.guild}'s Store",
        description=
        "Use `.store buy {item}` to buy something from the store!",
        color=blue)
    for number in store[ID]:
      if number == '1':
        if store[ID]['roleid'] == False:
          pass
        else:
          em.add_field(name=f"{store[ID]['item1']['name']}",
                      value=f"<@{store[ID]['item1']['roleid']}>\nPrice:{store[ID]['item1']['price']} {store[ID]['item1']['currency']}\nUse `{prefix}store buy {store[ID]['item1']['name']} to buy this item!"
                      )
      if number == '2':
        if store[ID]['roleid'] == False:
          pass
        else:
          em.add_field(name=f"{store[ID]['item2']['name']}",
                      value=f"<@{store[ID]['item2']['roleid']}>\nPrice:{store[ID]['item2']['price']} {store[ID]['item2']['currency']}\nUse `{prefix}store buy {store[ID]['item2']['name']} to buy this item!"
                      )
      if number == '3':
        if store[ID]['roleid'] == False:
          pass
        else:
          em.add_field(name=f"{store[ID]['item3']['name']}",
                      value=f"<@{store[ID]['item3']['roleid']}>\nPrice:{store[ID]['item3']['price']} {store[ID]['item3']['currency']}\nUse `{prefix}store buy {store[ID]['item3']['name']} to buy this item!"
                      )
      if number == '4':
        if store[ID]['roleid'] == False:
          pass
        else:
          em.add_field(name=f"{store[ID]['item4']['name']}",
                      value=f"<@{store[ID]['item4']['roleid']}>\nPrice:{store[ID]['item4']['price']} {store[ID]['item4']['currency']}\nUse `{prefix}store buy {store[ID]['item4']['name']} to buy this item!"
                      )
      if number == '5':
        if store[ID]['roleid'] == False:
          pass
        else:
          em.add_field(name=f"{store[ID]['item5']['name']}",
                      value=f"<@{store[ID]['item5']['roleid']}>\nPrice:{store[ID]['item5']['price']} {store[ID]['item5']['currency']}\nUse `{prefix}store buy {store[ID]['item5']['name']} to buy this item!"
                      )
                                     

    await ctx.reply(embed=em)



keep_alive()
client.run(my_secret)