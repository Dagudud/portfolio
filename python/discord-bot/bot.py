import discord
import random

intents = discord.Intents.all()
Perm = discord.Permissions.all()
Perm.ban_members = True
Perm.kick_members = True
intents.members = True
intents.message_content = True

TOKEN = os.environ.get('DISCORD_TOKEN', '')

x = ['Привет', 'Здравствуй', 'О какие люди!', 'Привет, рад видеть', 'Наконец-то ты вернулся!', 'Привет, дружище', 'Салам брат', 'Салам', 'Сау']
ANSWERS = {
    '!поиграем?': 'Да! Но я не знаю, во что ты играешь',
    '!ты классный': 'Спасибо! Ты тоже классный',
    '!пока': 'Всё давай, пиши как сможешь'
}

HOWAREYOU = {
    '!все хорошо': 'Это хорошо, что всё хорошо',
    '!ок': 'Немногословно',
    '!плохо': 'Эх, хотел бы я помочь, но я всего лишь бот',
    '!так себе': 'Ну ничего, сейчас поиграешь с друзьями и твое настроение улучшится',
    '!замечательно': 'У замечательных людей и дела замечательны',
    '!великолепно': 'Отлично, я рад за тебя!'
}

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    hi = random.choice(x)
    channel = message.channel
    message.content = message.content.lower()
    if message.content.startswith('!прив'):
        await channel.send(hi)
    elif message.content.startswith('!салам'):
        await channel.send(hi)
    elif message.content.startswith('!сау'):
        await channel.send(hi)
    for key in ANSWERS.keys():
        if message.content.lower().startswith(key):
            await channel.send(ANSWERS[key])

    def checkfunc(m):
        return m.content.lower() in HOWAREYOU and m.channel == channel

    if message.content.lower().startswith('!как дела?'):
        await channel.send('У меня всё хорошо, а у тебя?')
        msg = await client.wait_for('message', check=checkfunc)
        await channel.send(HOWAREYOU[msg.content.lower()])

    if message.content.lower().startswith('!забанить'):
        list = message.content.split()
        for member in client.get_all_members():
            if str(member) == str(list[1]):
                await channel.send(f'{member} был забанен администратором {message.author}')
                await member.ban(reason='Забанен, потому что потому',
                                 delete_message_seconds=86400)
                
    if message.content.lower().startswith('!кикнуть'):
        list1 = message.content.split()
        for member in client.get_all_members():
            if str(member) == str(list1[1]):
                await channel.send(f'{member} был кикнут администратором {message.author}')
                await member.kick(reason='Кикнут, потому что потому')

client.run(TOKEN)