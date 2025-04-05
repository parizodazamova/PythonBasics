list_numbers = list(range(150,1001))
players = ['charles', 'marina', 'michael', 'florance', 'eli', 'john', 'mark', 'marie']
print(players[1])

# players = ['charles', 'marina', 'michael', 'florance', 'eli']
print(players[0:4]) # partial list, from 0 to 3rd index
first3_players = players[0:4]

# ['florance', 'eli', 'john']
print(players[3:6])

# ['john', 'mark', 'marie']
print(players[5:8])
print(players[5:])

print(players[:]) # ? whole list, usually used to copy list
copy_players = players[:]

# wrong way of copying
players2 = players # is not a copy, second reference to the same list
print(copy_players)
print(players2)

print("\n***** appending a value to players *****")
players.append('atanas')
print(players)
print(players2)
print(copy_players)

print("\n***** looping *****")
for player in players[3:6]:
    print(player)

# HW 4-10 AND 4-11
