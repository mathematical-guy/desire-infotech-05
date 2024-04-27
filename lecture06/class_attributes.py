class Robot:
    processor = 'i3'
    ram = '8 GB'
    color = "grey"

x = Robot()
y = Robot()
z = Robot()
a = Robot()
b = Robot()
c = Robot()
d = Robot()
e = Robot()

print(x.processor)
print(y.processor)
print(z.processor)

Robot.processor = False

print(a.processor)
print(b.processor)
print(c.processor)
print(d.processor)
print(e.processor)