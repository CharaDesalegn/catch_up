from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import *
class Groud(Entity):
    def __init__(self,x,z,y = 0,h = 100):
        super().__init__()
        self.model = "cube"
        self.texture = "brick"
        self.y = y
        self.color = color.rgb(h,h,h)
        self.collider = "box"
        self.x = x
        self.z = z
class Block(Entity):
    def __init__(self,x,scale):
        super().__init__()
        self.model = "cube"
        self.collider = "box"
        self.color = color.rgb(0, 0, 225)
        self.z = 30
        self.scale_x = scale
        self.scale_y = scale
        self.x = x
class Decorecoto(Entity):
    def __init__(self,x,scale, z = 30):
        super().__init__()
        self.model = "cube"
        self.shader = basic_lighting_shader

        self.x = x
        self.z = z
        self.thick = 1
        self.scale_y = scale
        self.color = color.rgb(random.randrange(1,224),random.randrange(1,224),random.randrange(1,224))



def update_Decorecoto():
    global is_thick 
    for thing in things:
        if thing.scale_y >= 10:
            is_thick = True 
        elif thing.scale_y <= 2:
            is_thick = False
        if is_thick:
            thing.scale_y -= 0.1
        else:
            thing.scale_y += 0.1
        thing.z -= 1
        if thing.z <= -35:
            if thing.x == 5:
                another_thing = Decorecoto(5,random.randrange(0,10))
                things.append(another_thing)
            else:
                another_thing = Decorecoto(0,random.randrange(0,10))
                things.append(another_thing)
            things.remove(thing)
            destroy(thing)
            
def update():
    global count,score,score_text,master_counter
    update_Decorecoto()
    if not count:
        block = Block(random.randrange(1,5),random.randrange(1,4))
        blocks.append(block)
        count = master_counter
        score += 1
        master_counter = 30
        score_text.y = 1
        score_text = Text(score,position = (-.01,.5),scale = 4,color = color.red,origion = (0,0),background = False)

    count -= 1
    for block in blocks:
        block.z -= 1
        if block.z <= -30:
            blocks.remove(block)
            destroy(block)
        hit_info = block.intersects()
        if hit_info.hit:
            sound.play()
            score = 0
            player.x = 3
    player.rotation_x += 10
    
def input(key):
    if key == "left arrow" and player.x > 1:
        player.x -= 1
        camera.x -= .1
        player.rotation_z -= 10

    if key == "right arrow" and player.x < 4:
        player.x += 1
        camera.x += .1
        player.rotation_z += 10

things = []
is_thick =  True
for i in range(30,-35,-1):
    thing = Decorecoto(5,random.randrange(0,10),i)
    things.append(thing)
    thing = Decorecoto(0,random.randrange(0,10),i)
    things.append(thing)
count = 0
master_counter = 40
blocks = []
score = 0

app = Ursina()
player = Entity(model = "sphere",texture = "ball_texture.png", collider = "box",scale = 0.7)
ground = Entity(model = "cube",scale = (5,1,65))
sound = Audio("song.mp4",loop = True,autoplay= True)
score_text = Text(score,position = (-.02,.5),scale = 4,color = color.red,origion = (0,0),background = True)

ground.x = 2
player.x = 3
ground.y = -1
camera.y = 2.4
camera.z = -40
player.z = -20
camera.x = 2.5
camera.rotation_x = 10
app.run()