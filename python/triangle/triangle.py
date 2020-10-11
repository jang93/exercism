def equilateral(sides):
    return validate_triange(sides) and len(set(sides)) == 1

def isosceles(sides):
    return validate_triange(sides) and len(set(sides)) < 3

def scalene(sides):
    return validate_triange(sides) and len(set(sides)) == 3

def validate_triange(sides):
    return 0 not in sides and max(sides)*2 <= sum(sides)
