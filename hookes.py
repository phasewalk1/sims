GlowScript 3.2 VPython

"""Using SI units!!"""
g = 9.8
mass = 0.2
spring_k = 2
equil_length = 0.16

TABLE_SIDES = 0.5
TABLE_DEPTH = 0.05
ORIGIN = vector(0,0,0)
    

# construct a table
table = box (
    pos = ORIGIN,
    size = vector(TABLE_SIDES, TABLE_SIDES, TABLE_DEPTH),
    opacity = 1
)

# place a post in the table's center
post = cylinder (
    pos = ORIGIN,
    axis = vector(0,0,0.1),
    radius = 0.01,
    color = color.blue
)

# define a sliding object with a starting position
sliding_cube = box (
    pos = vector(0.15, 0.15, 0.05),
    size = vector(0.05, 0.05, 0.05),
    color = color.red,
    opacity = 1,
)
sliding_cube.m = mass
sliding_cube.p = vector(-0.1,0,0)

# Attach a trail 
attach_trail(sliding_cube, color=color.blue)

# Compute the correct axis for the helix
def set_helix_axis(post, sliding_obj):
  return post.pos + sliding_obj.pos - vector(0,0,0.05)
  

# define a helix
spring = helix(
    pos=vector(0,0,0.05),
    radius = 0.02,
    axis=set_helix_axis(post, sliding_cube),
    coils=10
)

# spring params
spring.l = 0.16
spring.k = 2
spring.displacement = mag(spring.axis) - spring.l

delta_t = 0.05

while True:
  # rate of animation
  rate(100)
  
  # update the springs axis to match the objects movement
  spring.axis = set_helix_axis(post, sliding_cube)
  
  # determine the force that the spring applies on the sliding object
  Fs = spring.displacement * (-spring.k * hat(spring.axis))
  sliding_cube.p += Fs * delta_t
  
  # update the sliding objects position
  sliding_cube.pos += sliding_cube.p * delta_t / sliding_cube.m
  
  spring.axis = set_helix_axis(post, sliding_cube)
