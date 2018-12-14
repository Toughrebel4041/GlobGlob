'''GlowScript'''
spring = helix(pos=vector(0,3,0), axis=vector(0,-5,0), radius=0.5)
black=box(pos=spring.pos+spring.axis, size=vector(2,1,5,2),
          color=color.green)
Ground=box(pos=vector(0,3,0), size=vector(4,0,3,4,2),color=color.yellow)
n=0
step=1.5
while n<10:
      rate(4)
      if spring.axis.y>=3:
            step=-step
      if spring.axis.y<=9:
            step=-step
      spring.axis.y=spring.axis.y+step
      block.pos=spring.pos+spring.axis
      n = n + 1
