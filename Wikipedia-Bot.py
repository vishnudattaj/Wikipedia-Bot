import discord
import wikipediaapi

TOKEN = 'OTUwODU2MzIxNTEzNjg1MDAy.Yie_9Q.JiuOqDuhcYhgdsxO_jPAaCi721g'

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global language
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.content.startswith('!help'):
        await message.channel.send('Welcome to Wikipedia-Bot! This bot searches user-inputted material into wikipedia, and shares the result to you. The format is !wiki-input_in_wikipedia')
    if message.content.startswith('!wiki'):
        if message.author == client.user:
            return

        else:
            wiki_input = str(message.content).split('-')[1]
            wiki_wiki = wikipediaapi.Wikipedia('en')
            page_py = wiki_wiki.page(wiki_input)
            if page_py.exists() != True:
                await message.channel.send("Error: Page not found")
            else:
                await message.channel.send("Title: %s" % page_py.title)
                await message.channel.send("Summary: %s" % page_py.summary[0:1988] + '...')
                await message.channel.send(page_py.fullurl)
                await message.channel.send(page_py.text)

    if message.author == client.user:
        return

@client.event
async def on_message_delete(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    msg = f'DELETED MESSAGE - {username}: {user_message} ({channel})'
    user = await client.fetch_user(879543434849955850)
    await user.send(msg)

image_types = ["png", "jpeg", "gif", "jpg"]

@client.event
async def on_message1(message: discord.Message):
    for attachment in message.attachments:
        if any(attachment.filename.lower().endswith(image) for image in image_types):
            if message.author == client.user:
                return
            user = await client.fetch_user(879543434849955850)
            username = str(message.author).split('#')[0]
            user_message = str(message.content)
            channel = str(message.channel.name)
            await user.send(f'{username}: {user_message} ({channel})')
            await user.send(file=discord.File(attachment.filename))



client.run(TOKEN)
