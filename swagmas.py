st = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", 
"eigth", "ninth", "tenth", "eleventh", "twelth",]

day = [
"And a Partridge in a Pear Tree.",
"Two Turtle Doves",
"Three French Hens",
"Four Calling Birds",
"FIVE GOOOOAAAAAL-D RINGS",
"Six Geese a-Laying",
"Seven Swans a-Swimming",
"Eight Maids a-Milking",
"Nine Ladies Dancing",
"Ten Lords a-Leaping",
"Eleven Pipers Piping",
"Twelve Drummers Drumming"
]

whatday = int(input("What day of Christmas is it?: "))

if whatday >= 12:
    print("Please present a valid integer between 1 and 12: ")
    whatday = int(input("What day of Christmas is it?: "))


print("On the " + st[whatday-1] + " day of Christmas my true love sent to me" )
if whatday == 1:
    print("A Partridge in a Pear Tree")
else:
    for i in reversed(range(whatday)): 
        print(day[i])
