from PIL import Image
from itertools import product
from utils import reflect_diagonal


def translation_combiner(building_block, dimensions=(4,4)):
    bbx, bby = building_block.size[0], building_block.size[1]
    size = (bbx * dimensions[0], bby * dimensions[1])
    wallpaper = Image.new('RGB', size, color = 'black')
    for piece in product(range(0, dimensions[0]), range(0, dimensions[1])):
        coordinate = (piece[0] * bbx, piece[1] * bby)
        wallpaper.paste(building_block, coordinate)
    return wallpaper

def reflection_combiner(building_block, dimensions=(4,4)):
    bbx, bby = building_block.size[0], building_block.size[1]
    size = (bbx * dimensions[0], bby * dimensions[1])
    wallpaper = Image.new('RGB', size, color = 'black')
    for piece in product(range(0, dimensions[0]), range(0, dimensions[1])):
        coordinate = (piece[0] * bbx, piece[1] * bby)
        pasting_image = building_block
        if piece[0] % 2 == 1:
            pasting_image = pasting_image.transpose(Image.FLIP_LEFT_RIGHT)
        if piece[1] % 2 == 1:
            pasting_image = pasting_image.transpose(Image.FLIP_TOP_BOTTOM)
        wallpaper.paste(pasting_image, coordinate)
    return wallpaper

def reflection_diagonal_combiner(building_block, dimensions=(4,4)):
    bbx, bby = building_block.size[0], building_block.size[1]
    size = (bbx * dimensions[0], bby * dimensions[1])
    wallpaper = Image.new('RGB', size, color='black')
    for piece in product(range(0, dimensions[0]), range(0, dimensions[1])):
        coordinate = (piece[0] * bbx, piece[1] * bby)
        pasting_image = building_block
        if piece[0] % 2 == 1:
            pasting_image = reflect_diagonal(pasting_image)
        if piece[1] % 2 == 1:
            pasting_image = reflect_diagonal(pasting_image)
        wallpaper.paste(pasting_image, coordinate)
    return wallpaper

def star_combiner(building_block, dimensions=(4,4)):
    bbx, bby = building_block.size[0], building_block.size[1]
    size = (bbx * dimensions[0], bby * dimensions[1])
    wallpaper = Image.new('RGB', size, color = 'black')
    for piece in product(range(0, dimensions[0]), range(0, dimensions[1])):
        coordinate = (piece[0] * bbx, piece[1] * bby)
        pasting_image = building_block
        if piece[1] % 2 == 1:
            pasting_image = pasting_image.transpose(Image.FLIP_LEFT_RIGHT)
        wallpaper.paste(pasting_image, coordinate)
    return wallpaper

# def cross_combiner(building_block, dimensions=(4,4)):
#     bbx, bby = building_block.size[0], building_block.size[1]
#     size = (bbx * dimensions[0], bby * dimensions[1])
#     wallpaper = Image.new('RGB', size, color = 'black')
#     for piece in product(range(0, dimensions[0]), range(0, dimensions[1])):
#         coordinate = (piece[0] * bbx, piece[1] * bby)
#         pasting_image = building_block
#         if piece[0] % 2 ==1:
#             pasting_image = pasting_image.transpose(Image.FLIP_TOP_BOTTOM)
#         if piece[1] % 2 == 1:
#             pasting_image = pasting_image.transpose(Image.FLIP_TOP_BOTTOM)
#         wallpaper.paste(pasting_image, coordinate)
#     return wallpaper

