# layer 0: Background Objects 배경
# layer 1: Foreground Objects 캐릭터, 에너미
# layer 2: Effect Objects 이펙트, 투사채
# layer 3: UI Objects UI 이미지
objects = [[], [], [], []]


def add_object(o, depth):
    objects[depth].append(o)

def add_objects(ol, depth):
    objects[depth] += ol

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            del o
            return
    raise ValueError('Trying destroy non existing object')


def remove_object(o):
    for layer in objects:
        try:
            layer.remove(o)
            del o
            return
        except:
            pass
    raise ValueError('Trying destroy non existing object')


def all_objects():
    for layer in objects:
        for o in layer:
            yield o


def clear():
    for o in all_objects():
        del o
    for layer in objects:
        layer.clear()



