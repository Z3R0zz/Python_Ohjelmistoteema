room_class = input("Syötä hyttiluokka: ").lower()

if room_class == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif room_class == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif room_class == "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif room_class == "c":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")

"""
# better solution, but using if/elif/else is mandatory
rooms = {
  "lux": "LUX on parvekkeellinen hytti yläkannella.",
  "a": "A on ikkunallinen hytti autokannen yläpuolella.",
  "b": "B on ikkunaton hytti autokannen yläpuolella.",
  "c": "C on ikkunaton hytti autokannen alapuolella."
}

room_class = input("Syötä hyttiluokka: ").lower()

if room_class not in rooms:
    print("Virheellinen hyttiluokka")
    exit()

print(rooms[room_class])
"""
