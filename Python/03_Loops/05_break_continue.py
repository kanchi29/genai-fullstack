characters = ["John", "Finch", "Fusco", "Carter", "Agent Snow", "Zoe"]

for character in characters:
    print(f"{character} was in Person of Interest")
    if character == "Fusco":
        continue
    if character == "Agent Snow":
        break
    print(f"{character} was very much loved by the audience")

# continue will skip the rest of the code in the block for one iteration and go back to the beginning
# break will instantly break out of the loop block and ditch the rest of the code entirely