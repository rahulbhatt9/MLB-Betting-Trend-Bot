import discord
import requests
import json

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('trends'):
        team = message.content[7:]
        #await message.channel.send(team)
        response = requests.get('https://api.sportsdata.io/v3/mlb/odds/json/TeamTrends/'+team+'?key=2b98253206584a9d99a44b951e481155')
        jsonData = json.loads(response.text)

        # last 10 games
        wins = jsonData['TeamGameTrends'][2]['Wins']
        losses = jsonData['TeamGameTrends'][2]['Losses']
        await message.channel.send('The ' + team + ' have won ' + str(wins) + ' and lost ' + str(losses) + ' in their last 10 games')

        winsAgainstSpread = jsonData['TeamGameTrends'][2]['WinsAgainstTheSpread']
        lossesAgainstSpread = jsonData['TeamGameTrends'][2]['LossesAgainstTheSpread']
        await message.channel.send('The ' + team + ' have won ' + str(winsAgainstSpread) + ' and lost ' + str(lossesAgainstSpread) + ' against the spread in their last 10 games')

        overs = jsonData['TeamGameTrends'][2]['Overs']
        await message.channel.send('The ' + team + ' have hit the over in ' + str(overs) + ' of their last 10 games')

        unders = jsonData['TeamGameTrends'][2]['Unders']
        await message.channel.send('The ' + team + ' have hit the under in ' + str(unders) + ' of their last 10 games')

        # last 10 home games

        


client.run('OTg2MzQ4NzgyNTE2MDY0MzA2.GYfRNO.KFrTvoK5EZUOfDTaJGmioUtCSMeQw8ZGSe_mZU')