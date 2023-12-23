from parameters import width, height
import random


def creat_sprite_list(amount, sprite_width, sprite_hight, speed, colors):
    sprits_list = []
    sprits_dict = {}
    retreat = sprite_width * 0.9
    retreat_of_border = 50 - retreat
    print(retreat_of_border, retreat)
    retreat_of_top = 0
    for i in range(amount):
        retreat_of_border += retreat
        retreat_of_top += sprite_hight
        sprits_dict["x"] = retreat_of_border + sprite_width/2
        sprits_dict["y"] = retreat_of_top + sprite_hight / 2
        sprits_dict["radius"] = sprite_width / 2
        sprits_dict["direction"] = "rith"
        sprits_dict["color"] = colors[i] #(random.uniform(0, 256), random.uniform(0, 256), random.uniform(0, 256))
        sprits_dict["speed"] = speed + speed*i*0
        sprits_list.append(sprits_dict)
        sprits_dict = {}
    return sprits_list

