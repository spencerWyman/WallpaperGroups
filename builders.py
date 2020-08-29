from PIL import Image
from PIL import ImageOps
from PIL import ImageChops
from math import floor

from utils import halve_image
from utils import quarter_image
from utils import rotation_translation
from utils import transform_diagonal
from utils import three_cut

def build_copy(image, square_size=100):
    copy = Image.new('RGB', (square_size, square_size))
    sized = image.resize((square_size, square_size))
    copy.paste(sized, (0, 0))
    return copy

def build_2gyration(image, square_size=100, half='l'):
    gyration = Image.new('RGB', (square_size, square_size))
    sized = image.resize((square_size, square_size))
    left_half = halve_image(sized, half)
    right_half = left_half.transpose(Image.ROTATE_180)
    gyration.paste(left_half, (0, 0))
    gyration.paste(right_half, (int(square_size/2), 0))
    return gyration

def build_2gyration_rect(image, size=(200, 100), half='l'):
    gyration = Image.new('RGB', size)
    sized = image.resize(size)
    left_half = halve_image(sized, half)
    right_half = left_half.transpose(Image.ROTATE_180)
    gyration.paste(left_half, (0, 0))
    gyration.paste(right_half, (int(size[0]/2), 0))
    return gyration

def build_4gyration(image, square_size=100, quarter='u'):
    gyration = Image.new('RGB', (square_size, square_size))
    sized = image.resize((square_size, square_size))
    quartered = (quarter_image(sized, quarter), (0, 0))
    gyration.paste(quartered[0], quartered[1])
    for direction in ('r', 'd', 'l'):
        quartered = rotation_translation(quartered, direction)
        gyration.paste(quartered[0], quartered[1])
    return gyration

def build_vertical_2reflection(image, square_size=100, half='r'):
    '''will reflect the right half onto the left half, or vice versa'''
    reflection = (image.copy()).resize((square_size, square_size))
    half_to_coordinate = { 'r' : (0, 0),
                           'l' : (int(reflection.size[0]/2), 0)
                           }
    half_image = halve_image(reflection, half)
    half_image = half_image.transpose(Image.FLIP_LEFT_RIGHT)
    reflection.paste(half_image, half_to_coordinate[half])
    return reflection

def build_diagonal_2reflection(image, square_size=100):
    return transform_diagonal(image,
                              lambda im: im.transpose(Image.FLIP_LEFT_RIGHT),
                              square_size)

def build_diagonal_2gyration(image, square_size=100):
    return transform_diagonal(image,
                              lambda im: im.rotate(180),
                              square_size)

def build_6reflection(im, size=100):
    hex_im = three_cut(three_cut(im, 30, size), 60, size, False, False)
    right_half = halve_image(hex_im, 'r')
    top_right_corner = halve_image(right_half, 'u')
    size = top_right_corner.size
    background = Image.new('RGB', (floor(1.5*size[0]), size[1]), color='black')
    background.paste(top_right_corner, (0, 0))
    mirrored_corner = ImageOps.mirror(background)
    flipped_corner = ImageOps.flip(mirrored_corner)
    hex_box = ImageChops.difference(background, flipped_corner)
    return hex_box
