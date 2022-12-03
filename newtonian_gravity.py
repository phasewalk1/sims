GlowScript 3.2 VPython

G = 6.67e-11
M_E = 5.97e24
R_E = 6.4e6

EARTH_CENTER = vector(0,0,0)

earth = sphere(
    pos = vector(0,0,0),
    radius = R_E,
    texture = textures.earth
)

ball = sphere(
    pos = vector(3*R_E,0,0),
    radius = R_E/100,
    texture = textures.rough,
)

attach_trail(ball, radius=3*ball.radius, color=color.white)

earth.m = M_E
ball.m = 1
ball.p = ball.m*vector(0,0,4420)

t = 0
dt = 60


def get_r_vec(ball_pos):
  return (ball_pos - EARTH_CENTER)
  
  
def newtons_univ_grav(r):
  Fg = (-(G * M_E * ball.m) / mag(r)**2) * hat(r)
  return Fg
  

while mag(ball.pos) > R_E:
    rate(100)
    r = get_r_vec(ball.pos)
    F = newtons_univ_grav(r)
    ball.p = ball.p + F * dt
    ball.pos = ball.pos + ball.p * dt / ball.m
    t += dt
