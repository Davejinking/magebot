import asyncio
import discord
import os
import re

client = discord.Client()
# 봇이 구동되었을 때 동작되는 코드입니다.
@client.event
async def on_ready():
    print("Logged in as ") #화면에 봇의 아이디, 닉네임이 출력됩니다.
    print(client.user.name)
    print(client.user.id)
    print("===========")
    # 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
    # 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
    await client.change_presence(game=discord.Game(name="ㅋ이광민스토리", type=1))
# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content.startswith('!명령어'): #만약 해당 메시지가 '!커맨드' 로 시작하는 경우에는
        await client.send_message(channel, '!help')
    #else: #위의 if에 해당되지 않는 경우
        #메시지를 보낸사람을 호출하며 말한 메시지 내용을 그대로 출력해줍니다.
        #await client.send_message(channel, "<@"+id+"> 네놈이 \""+message.content+"\"라고 기침소리를 내었는가")

if message.content.startswith('!경고부여'): # '!경고부여' 으로 시작하는 명령어를 감지한다면,
  if message.content[6:].startswith('<@'): # in 구문을 써도 되지만, 우린 아직 안배웠습니다. 여하튼 디스코드의 언급은 "<@(유저 ID)>"의 형태라서 "<@"으로 시작하면 유저를 언급했다고 봐도 됩니다.
    mention_id = re.findall(r'\d+', message.content) # 아래와 같은 절차를 거쳐 경고를 부여할 유저의 ID를 추출합시다.(사실상 message.content라는 변수에서 숫자만 뽑아내는겁니다.) re라는 모듈에 대한 강좌는 추후 진행하겠습니다.
    mention_id = mention_id[0]
    mention_id = str(mention_id)
    # 파일명은 코드 짜는 사람 마음이지만, 우리는 "(서버 ID)_(유저 ID).txt" 로 짓겠습니다.
    if os.path.isfile(message.server.id + " _ " + mention_id + ".txt"): # 해당 유저의 경고파일이 없으면 만들어야 하기에, 경고 파일이 있는지 확인합시다.
      f = open(message.server.id + " _ " + mention_id + ".txt", 'r') # 대상 유저의 경고수를 먼저 받아옵시다.
      past_warn = f.read() # past_warn이라는 변수에 예전 경고를 집어넣습니다.
      f.close() # 파일을 닫아줍시다. 원래는 안써도 무방하지만, 닫는것이 낫습니다. 그 이유는 좀있다 설명하도록 합죠.
      now_warn = int(past_warn) + 1 # 그리고 1을 경고에 추가로 넣어줍시다.
      now_warn = str(now_warn) # 문자열 형태로 바꿔줍니다. 그 이유는 나중에 설명하겠습니다.
      f = open(message.server.id + " _ " + mention_id + ".txt", 'w') # 파일을 쓰기 권한으로 열어줍니다. (여담이지만, 쓰기 권한으로 열면 파일을 알아서 만듭니다. 그대신, 기존에 파일이 있으면 지우고 만들어버리니 주의합시다.)
      f.write(now_warn) # 현재 경고를 넣어줍니다.
      f.close()
      await app.send_message(message.channel, "<@" + message.author.id + "> 님이 <@" + mention_id + "> 님께 경고 1회를 부여했습니다!\n<@" + mention_id + "> 님의 경고는 `" + now_warn + "회` 입니다!") # 알림을 보냅시다. `<<이것은 마크다운이라고 하는 문법의 일종입니다. 이것을 채팅 칠 때 좌|우에 기입하면 박스가 생깁니다.
    else:
      f = open(message.server.id + " _ " + mention_id + ".txt", 'w') # 우선 만들고 시작해야죠. 쓰기 권한으로 열어봅시다.
      f.write("1") # 경고 1회를 추가합시다.
      f.close()
      await app.send_message(message.channel, "<@" + message.author.id + "> 님이 <@" + mention_id + "> 님께 경고 1회를 부여했습니다!\n<@" + mention_id + "> 님의 경고는 `1회` 입니다!") # 알림을 보냅니다.
  else: # 언급이 안되었다면,
    await app.send_message(message.channel, "유저를 언급하여 주세요!") # 유저를 언급해달라는 메시지를 보냅니다.


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
