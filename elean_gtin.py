with open("product.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(*[i.split("\n")[-4] for i in text.split("—") if len(i.split("\n")) > 3][::-1], sep="\n")

