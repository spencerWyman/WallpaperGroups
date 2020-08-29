from PIL import Image
from PIL import ImageOps
from math import floor

def transformation_translation(img_and_coord, tfm, direction):
    """ tfm: Image -> Image. direction must be 'u', 'd', 'l', or 'r' """
    img, coord = img_and_coord[0], img_and_coord[1]
    h, w = img.size[0], img.size[1]
    direction_to_translation = {'u' : (0, -h),
                          'd' : (0, h),
                          'l' : (-w, 0),
                          'r' : (w, 0),
                          }
    translation = direction_to_translation[direction]
    new_coord = (coord[0] + translation[0], coord[1] + translation[1])
    new_img = tfm(img)
    return (new_img, new_coord)

def flip_translation(img_and_coord, direction):
    dir_to_flip = {'u' : Image.FLIP_TOP_BOTTOM,
                   'd' : Image.FLIP_TOP_BOTTOM,
                   'l' : Image.FLIP_LEFT_RIGHT,
                   'r' : Image.FLIP_LEFT_RIGHT,
                   }
    flip = dir_to_flip[direction]
    return transformation_translation(img_and_coord,
                                      lambda image: image.transpose(flip),
                                      direction)

def rotation_translation(img_and_coord, direction):
    return transformation_translation(img_and_coord,
                                      lambda image: image.rotate(-90),
                                      direction)

def halve_image(image, direction):
    """direction is 'u', 'd', 'l', or 'r' """
    imx, imy = image.size[0], image.size[1]
    direction_to_region = { 'u' : (0, 0, imx, int(imy/2)),
                            'd' : (0, int(imy/2), imx, imy),
                            'l' : (0, 0, int(imx/2), imy),
                            'r' : (int(imx/2), 0, imx, imy)
                            }
    return image.crop(direction_to_region[direction])

def quarter_image(image, direction):
    '''direction is 'u' = top left, 'l' = bottom left, 'r' = top right, 'd' = bottom right'''
    imx, imy = image.size[0], image.size[1]
    direction_to_region = { 'u' : (0, 0, int(imx/2), int(imy/2)),
                            'r' : (int(imx/2), 0, imx, int(imy/2)),
                            'l' : (0, int(imy/2), int(imx/2), imy),
                            'd' : (int(imx/2), int(imy/2), imx, imy)
                            }
    return image.crop(direction_to_region[direction])

def build_corners(image, image_builder, tfm_trnsl, square_size=100):
    building_block = Image.new('RGB', (square_size * 2, square_size * 2), color='black')
    top_left_corner = (image_builder(image, square_size), (0, 0))
    top_right_corner = tfm_trnsl(top_left_corner, 'r')
    bottom_right_corner = tfm_trnsl(top_right_corner, 'd')
    bottom_left_corner = rotation_translation(bottom_right_corner, 'l')
    corners = (top_left_corner, top_right_corner, bottom_left_corner, bottom_right_corner)

    for corner in corners:
        building_block.paste(corner[0], corner[1])
    return building_block

def transform_diagonal(image, tfm_left, square_size, tfm_right = -1):
    reflection = Image.new('RGB', (square_size, square_size))
    sized = image.resize((square_size, square_size))
    rotated = sized.rotate(-45, expand=1)
    right_half = halve_image(rotated, 'r')
    left_half = tfm_left(right_half)
    if tfm_right != -1:
        left_original = halve_image(rotated, 'l')
        right_half = tfm_right(left_original)
        rotated.paste(right_half, (int(rotated.size[0]/2), 0))
    rotated.paste(left_half, (0, 0))
    unrotated_with_blackspace = rotated.rotate(45, expand=1)
    region = (unrotated_with_blackspace.size[0]/4,
              unrotated_with_blackspace.size[1]/4,
              unrotated_with_blackspace.size[0]/4 + sized.size[0],
              unrotated_with_blackspace.size[1]/4 + sized.size[1])
    reflection = unrotated_with_blackspace.crop(region)
    return reflection

def reflect_diagonal(image, square_size=100):
    return transform_diagonal(image,
                              lambda im: im.transpose(Image.FLIP_LEFT_RIGHT),
                              square_size,
                              lambda im: im.transpose(Image.FLIP_LEFT_RIGHT))


def hexify(im, size=100):
    im = im.resize((2*size, floor((3**(0.5)) * size)))
    for _ in range(3):
        im = im.rotate(120, resample=0, fillcolor='black')
    return im

def three_cut(im, angle=30, size=100, right_copied=True, hexy=True):
    if hexy:
        hex_im = hexify(im, size)
    else:
        hex_im = im
    rotated = hex_im.rotate(angle, expand=1)
    if right_copied:
        right_half = halve_image(rotated, 'r')
        right_mirrored = ImageOps.mirror(right_half)
        rotated.paste(right_mirrored, (0, 0))
    else:
        left_half = halve_image(rotated, 'l')
        left_mirrored = ImageOps.mirror(left_half)
        rotated.paste(left_mirrored, (rotated.width//2, 0))
    unrotated_with_blackspace = rotated.rotate(-1 * angle, expand=1)
    region = (3**(0.5) * unrotated_with_blackspace.size[0]//8,
              2 * unrotated_with_blackspace.size[1]//8,
              3**(0.5) * unrotated_with_blackspace.size[0]//8 + hex_im.size[0],
              2 * unrotated_with_blackspace.size[1]//8 + hex_im.size[1])
    cut = unrotated_with_blackspace.crop(region)
    return cut
