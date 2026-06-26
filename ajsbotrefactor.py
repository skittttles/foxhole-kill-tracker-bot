import discord
from discord import app_commands
from discord.ext import commands, tasks
from discord.utils import get
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import time
import requests
import oci
import base64
from dotenv import load_dotenv

from vehicleNames import vehicleHash
from vicPrices import *



# names = {
#   "svh" : "wSilverhand",
#   "silverhand" : "wSilverhand",
#   "tank" : "wSilverhand"
# }

load_dotenv()

botKey = os.getenv("DISCORD")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.tree.command(name="reset", description="Resets current database")
async def reset(interaction: discord.Interaction, confirm: bool):
  pass

@bot.tree.command(name="stats", description="Displays current server stats")
async def stats(interaction: discord.Interaction):
  pass


def calculateScrap(costList):
  totalScrap = 0
  for material, value in costList.items():
    totalScrap += scrapCosts[material] * value
  return totalScrap

def calculateComps(costList):
  totalComps = 0
  for material, value in costList.items():
    totalComps += compCosts[material] * value
  return totalComps

def calculateRares(costList):
  totalRares = 0
  for material, value in costList.items():
    totalRares += rareCosts[material] * value
  return totalRares

@bot.tree.command(name="killed", description="Use to log a kill")
#@app_commands.command(name="killed")
@app_commands.choices(type=[
  app_commands.Choice(name="T1",value="t1"),
  app_commands.Choice(name="T2",value="t2"),
  app_commands.Choice(name="T3",value="t3"),
  app_commands.Choice(name="Proto",value="proto"),
])
async def killed(interaction: discord.Interaction, quantity: int, vehicle: str, type: app_commands.Choice[str], clan: str=None):

  print(f"Args passed: {quantity} {vehicle} {type['value']} {clan}")
  #Need to get DB but this is a later issue

  #Simply calculate values

  #Get vehicle name
  vehicleName = vehicleHash.get(vehicle)

  if vehicleName == None:
    print("Not found")
    pass

  if quantity == 0:
    print("Cannot add 0 vehicles")
    return

  vehicleObject = vicPrices.get(vehicleName)

  if vehicleObject is None:
    print("No vicPrice entry found for this")
    return

  costDict = vehicleObject.get('cost')
  
  if costDict is None:
    print("Costs not found")
    return
  
  #Check of tier and append that and check cost prices from that?
  #such as svh -> wSilverhand -> wSilverhandT2 db entry?
  

  #Get prices
  scrapCost = 0
  compCost = 0
  rareCost = 0
  
  if type == "Proto":
    scrapCost = 200
    compCost = 0
    rareCost = 0
  elif type == "T2":
    print("T2 Price, check if t2 exists")
    scrapCost = calculateScrap(costDict)
    compCost = calculateComps(costDict)
    rareCost = calculateRares(costDict)
  elif type == "T3":
    print("T2 Price, check if t3 exists")
    scrapCost = calculateScrap(costDict)
    compCost = calculateComps(costDict)
    rareCost = calculateRares(costDict)
  else:
    scrapCost = calculateScrap(costDict)
    compCost = calculateComps(costDict)
    rareCost = calculateRares(costDict)
  

  print(costDict)
  print(f"Scrap: {scrapCost}")
  print(f"Comps: {compCost}")
  print(f"Rares: {rareCost}")
    
  pass

#Lists all available vehicle nicknames
@bot.tree.command(name="list", description="List all available names to use for logging")
#@app_commands.describe()
async def list(interaction: discord.Interaction):

  initialEmbed = discord.Embed(description=f"Displaying all acceptable vehicle names for use in the /killed command:\n")
  initialEmbed.set_author(name=f"All Accepted Names:")

  await interaction.response.send_message(embed=initialEmbed, ephemeral=True)

  concatString = ""
  for nickname, name in vehicleHash.items():
    concatString +=  (f"{nickname} ({name[1:]})\n")
    if len(concatString) > 1500:
      embed = discord.Embed(description=f"{concatString}")
      embed.set_author(name="Author")
      await interaction.followup.send(embed=embed, ephemeral=True)
      concatString = ""

  embed = discord.Embed(description=f"{concatString}")
  embed.set_author(name="Vehicle Names")
  await interaction.followup.send(embed=embed, ephemeral=True)


@bot.event
async def on_ready():
  print("Online...")

  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} commands")
  except Exception as e:
    print(e)

bot.run(botKey)