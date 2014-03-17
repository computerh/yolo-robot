name = 'Zed A. Shaw'
age= 35 # not a lie
height = 74.0 # inches
heightcm = height * 2.54 # convert his height to centimeters
weight = 180.0 # lbs
weightkg = weight / 2.2 # convert his weight to kilograms 
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d centimeters tall." % heightcm
print "He's %d pounds heavy." % weight
print "He's %r kilos heavy." % weightkg # %r prints exactly no rounding up
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)