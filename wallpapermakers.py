from PIL import Image

from builders import build_copy
from builders import build_2gyration
from builders import build_4gyration
from builders import build_6reflection
from builders import build_vertical_2reflection
from builders import build_diagonal_2reflection
from builders import build_diagonal_2gyration

from combiners import reflection_combiner
from combiners import translation_combiner
from combiners import star_combiner
from combiners import reflection_diagonal_combiner


def star_442(im, dim=(4, 4)):
    return reflection_combiner(build_diagonal_2reflection(im), dim)


def blue_442(im, dim=(4, 4)):
    return translation_combiner(build_4gyration(im, quarter='r'), dim)


def star_2222(im, dim=(4, 4)):
    return reflection_combiner(build_vertical_2reflection(im, half='r'), dim)


def blue_2222(im, dim=(4, 4)):
    return translation_combiner(build_2gyration(im), dim)


def wandering(im, dim=(4, 4)):
    return translation_combiner(build_copy(im), dim)


def star_cross(im, dim=(4, 4)):
    return translation_combiner(build_diagonal_2reflection(im), dim)


def star_star(im, dim=(4, 4)):
    return translation_combiner(build_vertical_2reflection(im, half='l'), dim)


def blue4_star2(im, dim=(4, 4)):
    return reflection_combiner(build_4gyration(im, quarter='l'), dim)


def cross_cross(im, dim=(4, 4)):
    return star_combiner(im.resize((100, 100)), dim)


def blue22_star(im, dim=(4, 4)):
    return star_combiner(build_2gyration(im), dim)


def blue22_cross(im, dim=(4, 4)):
    return reflection_diagonal_combiner(build_diagonal_2gyration(im), dim)


def blue2_star22(im, dim=(4, 4)):
    return reflection_combiner(build_2gyration(im), dim)


def star_632(im, dim=(4, 4)):
    return reflection_combiner(build_6reflection(im), dim)

wallpapermakers = {
    'star_442': star_442,
    'blue_442': blue_442,
    'star_2222': star_2222,
    'blue_2222': blue_2222,
    'wandering': wandering,
    'star_cross': star_cross,
    'star_star': star_star,
    'blue4_star2': blue4_star2,
    'cross_cross': cross_cross,
    'blue22_star': blue22_star,
    'blue22_cross': blue22_cross,
    'blue2_star22': blue2_star22,
    'star_632': star_632,
    }

group_names = (
    'star_442',
    'blue_442',
    'star_2222',
    'blue_2222',
    'wandering',
    'star_cross',
    'star_star',
    'blue4_star2',
    'cross_cross',
    'blue22_star',
    'blue22_cross',
    'blue2_star22',
    'star_632',
    )


def wallpapermaker(group, image, dim=(4, 4)):
    return wallpapermakers[group](image, dim)
