import discord
import requests
import json
import os
from dotenv import load_dotenv


bot = discord.Client(intents=discord.Intents.default())

def getLast10Games(jsonData, team):
    toReturn = "`"
    wins = jsonData['TeamGameTrends'][2]['Wins']
    losses = jsonData['TeamGameTrends'][2]['Losses']
    toReturn += team + " are " + str(wins) + "-" + str(losses) + " in their last 10 games\n"
    
    winsAgainstSpread = jsonData['TeamGameTrends'][2]['WinsAgainstTheSpread']
    lossesAgainstSpread = jsonData['TeamGameTrends'][2]['LossesAgainstTheSpread']
    toReturn += team + " are " + str(winsAgainstSpread) + "-" + str(lossesAgainstSpread) + " against the spread in their last 10 games\n"
    
    overs = jsonData['TeamGameTrends'][2]['Overs']
    unders = jsonData['TeamGameTrends'][2]['Unders']
    toReturn += team + " are " + str(overs) + "-" + str(unders) + " over/under in their last 10 games\n"

    averageScore = jsonData['TeamGameTrends'][2]['AverageScore']
    toReturn += team + " are scoring an average score of " + str(averageScore) + " in their last 10 games\n"

    averageOpponentScore = jsonData['TeamGameTrends'][2]['AverageOpponentScore']
    toReturn += team + " are giving up an average score of " + str(averageOpponentScore) + " in their last 10 games\n`"
    
    return toReturn

def getLast10HomeGames(jsonData, team):
    toReturn = "`"
    wins = jsonData['TeamGameTrends'][5]['Wins']
    losses = jsonData['TeamGameTrends'][5]['Losses']
    toReturn += team + " are " + str(wins) + "-" + str(losses) + " in their last 10 games\n"
    
    winsAgainstSpread = jsonData['TeamGameTrends'][5]['WinsAgainstTheSpread']
    lossesAgainstSpread = jsonData['TeamGameTrends'][5]['LossesAgainstTheSpread']
    toReturn += team + " are " + str(winsAgainstSpread) + "-" + str(lossesAgainstSpread) + " against the spread in their last 10 games\n"
    
    overs = jsonData['TeamGameTrends'][5]['Overs']
    unders = jsonData['TeamGameTrends'][5]['Unders']
    toReturn += team + " are " + str(overs) + "-" + str(unders) + " over/under in their last 10 games\n"

    averageScore = jsonData['TeamGameTrends'][5]['AverageScore']
    toReturn += team + " are scoring an average score of " + str(averageScore) + " in their last 10 games\n"

    averageOpponentScore = jsonData['TeamGameTrends'][5]['AverageOpponentScore']
    toReturn += team + " are giving up an average score of " + str(averageOpponentScore) + " in their last 10 games\n`"
    
    return toReturn

def getLast10AwayGames(jsonData, team):
    toReturn = "`"
    wins = jsonData['TeamGameTrends'][8]['Wins']
    losses = jsonData['TeamGameTrends'][8]['Losses']
    toReturn += team + " are " + str(wins) + "-" + str(losses) + " in their last 10 away games\n"
    
    winsAgainstSpread = jsonData['TeamGameTrends'][8]['WinsAgainstTheSpread']
    lossesAgainstSpread = jsonData['TeamGameTrends'][8]['LossesAgainstTheSpread']
    toReturn += team + " are " + str(winsAgainstSpread) + "-" + str(lossesAgainstSpread) + " against the spread in their last 10 away games\n"
    
    overs = jsonData['TeamGameTrends'][8]['Overs']
    unders = jsonData['TeamGameTrends'][8]['Unders']
    toReturn += team + " are " + str(overs) + "-" + str(unders) + " over/under in their last 10 away games\n"

    averageScore = jsonData['TeamGameTrends'][8]['AverageScore']
    toReturn += team + " are scoring an average score of " + str(averageScore) + " in their last 10 away games\n"

    averageOpponentScore = jsonData['TeamGameTrends'][8]['AverageOpponentScore']
    toReturn += team + " are giving up an average score of " + str(averageOpponentScore) + " in their last 10 away games\n`"
    
    return toReturn

def getLast10FavoriteGames(jsonData, team):
    toReturn = "`"
    wins = jsonData['TeamGameTrends'][11]['Wins']
    losses = jsonData['TeamGameTrends'][11]['Losses']
    toReturn += team + " are " + str(wins) + "-" + str(losses) + " in their last 10 games as a favorite\n"
    
    winsAgainstSpread = jsonData['TeamGameTrends'][11]['WinsAgainstTheSpread']
    lossesAgainstSpread = jsonData['TeamGameTrends'][11]['LossesAgainstTheSpread']
    toReturn += team + " are " + str(winsAgainstSpread) + "-" + str(lossesAgainstSpread) + " against the spread in their last 10 games as a favorite\n"
    
    overs = jsonData['TeamGameTrends'][11]['Overs']
    unders = jsonData['TeamGameTrends'][11]['Unders']
    toReturn += team + " are " + str(overs) + "-" + str(unders) + " over/under in their last 10 games as a favorite\n"

    averageScore = jsonData['TeamGameTrends'][11]['AverageScore']
    toReturn += team + " are scoring an average score of " + str(averageScore) + " in their last 10 games as a favorite\n"

    averageOpponentScore = jsonData['TeamGameTrends'][11]['AverageOpponentScore']
    toReturn += team + " are giving up an average score of " + str(averageOpponentScore) + " in their last 10 games as a favorite\n`"

    return toReturn

def getLast10UnderdogGames(jsonData, team):
    toReturn = "`"
    wins = jsonData['TeamGameTrends'][14]['Wins']
    losses = jsonData['TeamGameTrends'][14]['Losses']
    toReturn += team + " are " + str(wins) + "-" + str(losses) + " in their last 10 games as an underdog\n"
    
    winsAgainstSpread = jsonData['TeamGameTrends'][14]['WinsAgainstTheSpread']
    lossesAgainstSpread = jsonData['TeamGameTrends'][14]['LossesAgainstTheSpread']
    toReturn += team + " are " + str(winsAgainstSpread) + "-" + str(lossesAgainstSpread) + " against the spread in their last 10 games as an underdog\n"
    
    overs = jsonData['TeamGameTrends'][14]['Overs']
    unders = jsonData['TeamGameTrends'][14]['Unders']
    toReturn += team + " are " + str(overs) + "-" + str(unders) + " over/under in their last 10 games as an underdog\n"

    averageScore = jsonData['TeamGameTrends'][14]['AverageScore']
    toReturn += team + " are scoring an average score of " + str(averageScore) + " in their last 10 games as an underdog\n"

    averageOpponentScore = jsonData['TeamGameTrends'][14]['AverageOpponentScore']
    toReturn += team + " are giving up an average score of " + str(averageOpponentScore) + " in their last 10 games as an underdog\n`"
        
    return toReturn

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):

    # Ignore Messages Sent By Bot
    if message.author == bot.user:
        return
    
    team = message.content.strip()[-3:]
    response = requests.get('https://api.sportsdata.io/v3/mlb/odds/json/TeamTrends/'+team+'?key=2b98253206584a9d99a44b951e481155')
    jsonData = json.loads(response.text)
    
    if message.content == "!tb help":
        await message.channel.send("**MLB TrendBot Commands**\nFor Last 10 Games: `tb.trends <TEAM ABBREVIATION>`\nFor Last 10 Home Games: `tb.trends home <TEAM ABBREVIATION>`\nFor Last 10 Away Games: `tb.trends away <TEAM ABBREVIATION>`\nFor Last 10 Games as a Favorite: `tb.trends favorite <TEAM ABBREVIATION>\n`For Last 10 Games as an Underdog: `tb.trends underdog <TEAM ABBREVIATION>`")

    elif (message.content.startswith('!tb trends home')):
        await message.channel.send(getLast10HomeGames(jsonData, team))

    elif (message.content.startswith('!tb trends away')):
        await message.channel.send(getLast10AwayGames(jsonData, team))

    elif (message.content.startswith('!tb trends favorite')):
        await message.channel.send(getLast10FavoriteGames(jsonData, team))

    elif (message.content.startswith('!tb trends underdog')):
        await message.channel.send(getLast10UnderdogGames(jsonData, team))

    elif (message.content.startswith('!tb trends')):
        await message.channel.send(getLast10Games(jsonData, team))
    
        
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
