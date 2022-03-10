import discord
import wikipediaapi

TOKEN = "OTUwODU2MzIxNTEzNjg1MDAy.Yie_9Q.JuBcAZWDmgDC9JTBFZmzz5L6FTQ"

client = discord.Client()


@client.event
async def on_ready():
    await message.channel.send(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.content.startswith('!help'):
        await message.channel.send(
            'Welcome to Wikipedia-Bot! This bot searches user-inputted material into wikipedia, and shares the result to you. The format is !wiki-input_in_wikipedia')
    if message.content.startswith('!wiki'):
        if message.author == client.user:
            return

        else:
            wiki_input = str(message.content).split('-')[1]
            wiki_wiki = wikipediaapi.Wikipedia('en')
            page_py = wiki_wiki.page(wiki_input)
            if not page_py.exists():
                await message.channel.send("Error: Page not found")
            else:
                await message.channel.send("Title: %s" % page_py.title)
                await message.channel.send("Summary: %s" % page_py.summary[0:1988] + '...')
                await message.channel.send(page_py.fullurl)
                await message.channel.send(page_py.text)




@client.event
async def on_message_delete(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    msg = f'DELETED MESSAGE - {username}: {user_message} ({channel})'
    master = await client.fetch_user(879543434849955850)
    await master.send(msg)
    

@client.event
async def on_image_sent(message):
    file = await message.attachments[0].to_file()
    await message.channel.send(file=file, embed=embed)
    




client.run(TOKEN)
