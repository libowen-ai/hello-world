me = {
    "name": "libowen-ai",
    "age": 25,
    "goal": "做出能用的 AI 工具"
}

print(me["name"])

me["age"] = 26
me["city"] = "北京"

for k, v in me.items():
    print(k,":", v)