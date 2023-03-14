import openai
openai.api_key = "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"

def fetchAPI(input):
  print("组织语言中, 请稍后...")
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": input}
    ]
  )
  str = completion.choices[0].message.content
  str.encode("utf8").decode("utf8", "ignore")
  print(str)
print("您好，我是人工智能语言模型ChatGPT，有什么可以帮您的吗？[按Enter退出]")
str_in = input()
while(str_in):
  fetchAPI(str_in)
  print("您可以继续提问~[按Enter退出]")
  str_in = input()
print("Thanks for using! ♪(･ω･)ﾉ")