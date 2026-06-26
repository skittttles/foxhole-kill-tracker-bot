import discord
from discord import app_commands
from discord.ext import commands, tasks
from discord.utils import get

import os
import time
import requests
import oci
import base64
import logging
from dotenv import load_dotenv

from vehicleNames import vehicleHash
from vicPrices import *
import sql

load_dotenv()


botKey = os.getenv("DISCORD")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)

#Discord Helpers

def createGenericErrorEmbed(message):
  errorEmbed = discord.Embed(description=message, color=0x852424)
  errorEmbed.set_author(name=f"Error running command", icon_url="https://i.imgur.com/4cHVOnD.png")
  return errorEmbed

def createGenericEmbed(title, message):
  successEmbed = discord.Embed(title=title, description=message, color=0x245484)
  return successEmbed

#Specific Function Helpers

def calculateScrap(costList):
  totalScrap = 0
  for material, value in costList.items():
    costs = scrapCosts.get(material)
    if costs is None:
      print(f"Error could not find {material} in scrapCosts")
      pass
    totalScrap += costs * value
  return totalScrap

def calculateComps(costList):
  totalComps = 0
  for material, value in costList.items():
    costs = compCosts.get(material)
    if costs is None:
      print(f"Error could not find {material} in compCosts")
      pass
    totalComps += costs * value
  return totalComps

def calculateRares(costList):
  totalRares = 0
  for material, value in costList.items():
    costs = rareCosts.get(material)
    if costs is None:
      print(f"Error could not find {material} in rareCosts")
      pass
    totalRares += costs * value
  return totalRares

def getCostObject(costDict):
  returnObject = {
    "scrap" : calculateScrap(costDict),
    "comps" : calculateComps(costDict),
    "rares" : calculateRares(costDict),
  }
  return returnObject


#Discord Bot Commands

@bot.tree.command(name="reset", description="Resets current database")
async def reset(interaction: discord.Interaction, confirm: bool):
  pass

@bot.tree.command(name="stats", description="Displays current server stats")
async def stats(interaction: discord.Interaction):
  pass

@bot.tree.command(name="cost", description="Lookup cost of an item")
async def stats(interaction: discord.Interaction, vehicle: str):
  vehicleName = vehicleHash.get(vehicle)

  if vehicleName == None:
    logging.info(f"Could not find vehicle name {vehicle}")
    error = createGenericErrorEmbed(f"Vehicle name not found for {vehicle}, if you believe this is an error contact @skitttles")
    await interaction.response.send_message(embed=error, ephemeral=True)
    return

  vehicleObject = vicPrices.get(vehicleName)

  if vehicleObject is None:
    logging.warning(f"No vicPrices entry found for {vehicleName}")
    error = createGenericErrorEmbed(f"Vehicle price lookup entry not found for {vehicleName}, contact @skitttles")
    await interaction.response.send_message(embed=error, ephemeral=True)
    return

  costDict = vehicleObject.get('cost')
  
  if costDict is None:
    logging.warning(f"Cost dictionary not found for {vehicleName}")
    error = createGenericErrorEmbed(f"Vehicle price cost dictionary not found in lookup for {vehicleName}, contact @skitttles")
    await interaction.response.send_message(embed=error, ephemeral=True)
    return

  costs = getCostObject(costDict)
  title = f"Cost values for {vehicleName[1:]}"
  message = f"**T1 Cost**\nScrap: {costs.get("scrap")}\nComps: {costs.get("comps")}\nRares: {costs.get("rares")}"
  #Check if T2 / T3 is available then append here
  embed = createGenericEmbed(title, message)

  await interaction.response.send_message(embed=embed)



@bot.tree.command(name="killed", description="Use to log a kill")
@app_commands.describe(quantity="Number of this specific vehicle to log", vehicle="Vehicle name found in /list to log", type="Vehicle tier if applicable (T1 most common)",clan="List a clan associated with the kill if applicable")
@app_commands.choices(type=[
  app_commands.Choice(name="T1",value="t1"),
  app_commands.Choice(name="T2",value="t2"),
  app_commands.Choice(name="T3",value="t3"),
  app_commands.Choice(name="Proto",value="proto"),
])
async def killed(interaction: discord.Interaction, quantity: int, vehicle: str, type: app_commands.Choice[str], clan: str=None):

  print(f"Args passed: {quantity} {vehicle} {type.value} {clan}")
  #Need to get DB but this is a later issue

  #Get vehicle name
  vehicleName = vehicleHash.get(vehicle)

  if quantity <= 0:
    error = createGenericErrorEmbed(f"Invalid quantity, please enter a positive number (> 0)")
    await interaction.response.send_message(embed=error, ephemeral=True)
    return

  if vehicleName == None:
    logging.info(f"Could not find vehicle name {vehicle}")
    error = createGenericErrorEmbed(f"Vehicle name not found for {vehicle}, if you believe this is an error contact @skitttles")
    await interaction.response.send_message(embed=error, ephemeral=True)
    return

  vehicleObject = vicPrices.get(vehicleName)

  if vehicleObject is None:
    logging.warning(f"No vicPrices entry found for {vehicleName}")
    error = createGenericErrorEmbed(f"Vehicle price lookup entry not found for {vehicleName}, contact @skitttles")
    await interaction.response.send_message(embed=error, ephemeral=True)
    return

  costDict = vehicleObject.get('cost')
  
  if costDict is None:
    logging.warning(f"Cost dictionary not found for {vehicleName}")
    error = createGenericErrorEmbed(f"Vehicle price cost dictionary not found in lookup for {vehicleName}, contact @skitttles")
    await interaction.response.send_message(embed=error, ephemeral=True)
    return

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
  print(vehicleName)
  print(clan)
  print(f"Scrap: {scrapCost}")
  print(f"Comps: {compCost}")
  print(f"Rares: {rareCost}")

  #Now we need to 
    
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