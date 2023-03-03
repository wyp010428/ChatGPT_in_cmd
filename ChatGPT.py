import openai
from time import sleep
from os import system

# 防止控制台颜色失效
import os
os.system('')
from colorama import init
init(autoreset = True)

# 你自己的的API_KEY
openai.api_key = "YOUR_API_KEY"

# message是上传到模型的，history使用来打印输出的
message=[
        {"role": "system", "content": "You are a helpful assistant."},
        # {"role": "user", "content": "Who won the world series in 2020?"},
        # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        # {"role": "user", "content": "Where was it played?"}
    ]
history = []

# 调用ChatGPT的API
def answer_question(message):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0301",
    messages = message,
    temperature = 0.5
    )
    answer = response['choices'][0]['message']['content']
    return answer

# 打印初始画面
print("\033[1;36m   ________  ___  ___  ________  _________  ________  ________  _________   \n  |\   ____\|\  \|\  \|\   __  \|\___   ___\\   ____\|\   __  \|\___   ___\  \n  \ \  \___|\ \  \\\  \ \  \|\  \|___ \  \_\ \  \___|\ \  \|\  \|___ \  \_|  \n   \ \  \    \ \   __  \ \   __  \   \ \  \ \ \  \  __\ \   ____\   \ \  \   \n    \ \  \____\ \  \ \  \ \  \ \  \   \ \  \ \ \  \|\  \ \  \___|    \ \  \  \n     \ \_______\ \__\ \__\ \__\ \__\   \ \__\ \ \_______\ \__\        \ \__\ \n      \|_______|\|__|\|__|\|__|\|__|    \|__|  \|_______|\|__|         \|__| \033[0m\n")
sleep(1)
print("——"*40)
print(" "*25 + "\033[1m欢迎来到\033[1;36m ChatGPT \033[0m\033[1m智能聊天机器人")
print(" "*25 + "在问题后加\033[7m 空格 \033[0m\033[1m来进行连续对话~\033[0m")
print("——"*40)
sleep(1)

# 开始问答循环
while True:
    # 询问用户问题
    question = input("\n\033[2mType here: \033[0m\033[1m")
    print('\033[0m', end='') #恢复输入时的特殊字体

    # 根据问题结尾是否有空格来判断是否连续对话
    # 如果没有空格，就重置message，并在history中加入一行分界线
    if question[-1] != " ":
        history += [{"role": "\x1b[1A", "content": "——"*40}]
        message = [{"role": "system", "content": "You are a helpful assistant."}]

    # 将问题合并入message和history
    question = question.strip()
    message += [{"role": "user", "content": question}]
    history += [{"role": "User:      ", "content": question}]

    # 打印用户可见内容，为了排版美观，每次清空终端输出重新打印
    # 先打印到用户的问题，再调用ChatGPT获取答案再打印回答
    system("cls")
    print("\033[1;36m   ________  ___  ___  ________  _________  ________  ________  _________   \n  |\   ____\|\  \|\  \|\   __  \|\___   ___\\   ____\|\   __  \|\___   ___\  \n  \ \  \___|\ \  \\\  \ \  \|\  \|___ \  \_\ \  \___|\ \  \|\  \|___ \  \_|  \n   \ \  \    \ \   __  \ \   __  \   \ \  \ \ \  \  __\ \   ____\   \ \  \   \n    \ \  \____\ \  \ \  \ \  \ \  \   \ \  \ \ \  \|\  \ \  \___|    \ \  \  \n     \ \_______\ \__\ \__\ \__\ \__\   \ \__\ \ \_______\ \__\        \ \__\ \n      \|_______|\|__|\|__|\|__|\|__|    \|__|  \|_______|\|__|         \|__| \033[0m\n\n")
    for i in history:
        if i["role"] == "User:      ": # 打印用户的问题
            print("\033[1;32mUser:      \033[0m" + f"\033[1m{i['content']}\033[0m")
        elif i["role"] == "ChatGPT:   ": # 打印ChatGPT的回答
            print("\033[1;36mChatGPT:   \033[0m" + i['content'])
            print()
        else: # 打印分界线
            print(i["role"] + i["content"])

    # 获取ChatGPT的回答并加入message和history
    answer = answer_question(message)
    message += [{"role": "assistant", "content": answer}]
    history += [{"role": "ChatGPT:   ", "content": answer}]

    # 打印本次回答内容
    print("\033[1;36mChatGPT:   \033[0m" + answer)

    # 结束循环