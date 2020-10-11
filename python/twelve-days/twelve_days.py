
day = ["zero", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

true_love_gave = [
    "twelve Drummers Drumming",
    "eleven Pipers Piping",
    "ten Lords-a-Leaping",
    "nine Ladies Dancing",
    "eight Maids-a-Milking",
    "seven Swans-a-Swimming",
    "six Geese-a-Laying",
    "five Gold Rings",
    "four Calling Birds",
    "three French Hens",
    "two Turtle Doves",
    "a Partridge in a Pear Tree"
]

def recite(start_verse, end_verse):
    if start_verse < 1 or start_verse > 12:
        raise ValueError("Start verse needs to be within 1-12")
    elif end_verse < 1 or end_verse > 12:
        raise ValueError("End verse needs to be within 1-12")
    elif start_verse > end_verse:
        raise ValueError("Start verse cannot after end verse")
    return [get_lyric_line(i) for i in range(start_verse, end_verse + 1)]

def get_lyric_line(verse):
    return f"On the {day[verse]} day of Christmas my true love gave to me: {', '.join(true_love_gave[12-verse:])}.".replace(", a", ", and a")

