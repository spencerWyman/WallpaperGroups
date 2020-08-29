from PIL import Image

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


star_442 = lambda im: reflection_combiner(build_diagonal_2reflection(im))
blue_442 = lambda im: translation_combiner(build_4gyration(im, quarter='r'))
star_2222 = lambda im: reflection_combiner(build_vertical_2reflection(im, half='r'))
blue_2222 = lambda im: translation_combiner(build_2gyration(im))
wandering = lambda im: translation_combiner(im)
star_cross = lambda im: translation_combiner(build_diagonal_2reflection(im))
star_star = lambda im: translation_combiner(build_vertical_2reflection(im, half='l'))
blue4_star2 = lambda im: reflection_combiner(build_4gyration(im, quarter='l'))
cross_cross = lambda im: star_combiner(im.resize((100, 100)))
blue22_star = lambda im: star_combiner(build_2gyration(im))
blue22_cross = lambda im: reflection_diagonal_combiner(build_diagonal_2gyration(im))
blue2_star22 = lambda im: reflection_combiner(build_2gyration(im))
star_632 = lambda im: reflection_combiner(build_6reflection(im))

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


def wallpapermaker(group, image):
    return wallpapermakers[group](image)
