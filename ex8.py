with open("note.txt","w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")

with open("note.txt","r", encoding="utf-8") as f:
    content = f.read()

print("读到的内容：")
print(content)
with open("note.txt","a", encoding="utf-8") as f:
    f.write("追加的第四行\n")

with open("note.txt","r", encoding="utf-8") as f:
    print(f.read())