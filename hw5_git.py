print("Hey there!")

joke = input("Tell me something funny.")
dad_jokes = []
if "what" in joke:
    print("what?")
    j1 = input()
    print("Ok, get outta here.")
    dad_jokes.append(joke)
    dad_jokes.append(j1)
else:
    if "why" in joke:
        print("Why?")
        j2 = input()
        print("bahaha!")
        dad_jokes.append(joke)
        dad_jokes.append(j2)

print(dad_jokes)