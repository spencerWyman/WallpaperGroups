from sys import argv
from os import path
from pathlib import Path
from PIL import Image
from wallpapermakers import wallpapermaker
from wallpapermakers import group_names
from random import randint

command = argv[1]

if command == 'show':

    group_name = argv[2]
    image_path = argv[3]
    im = Image.open(image_path)
    wallpapermaker(group_name, im).show()

elif command == 'saveall':
    tilings = [
        ('star_442', wallpapermaker('star_442', im)),
        ('blue_442', wallpapermaker('blue_442', im)),
        ('star_2222', wallpapermaker('star_2222', im)),
        ('blue_2222', wallpapermaker('blue_2222', im)),
        ('wandering', wallpapermaker('wandering', im)),
        ('star_cross', wallpapermaker('star_cross', im)),
        ('star_star', wallpapermaker('star_star', im)),
        ('blue4_star2', wallpapermaker('blue4_star2', im)),
        ('cross_cross', wallpapermaker('cross_cross', im)),
        ('blue22_star', wallpapermaker('blue22_star', im)),
        ('blue22_cross', wallpapermaker('blue22_cross', im)),
        ('blue2_star22', wallpapermaker('blue2_star22', im)),
    ]
    for [tilename, image] in tilings:
        image.save('images/tilename')

elif command == 'make_training_set':
    source_path = Path(argv[2])
    images = [Image.open(im_path) for im_path in source_path.iterdir()]

    # create a directory for each tiling
    for group in group_names:
        tiling_path = source_path.parent / group
        if not tiling_path.is_dir():
            tiling_path.mkdir()

    # create the tilings for each image and save to the created directories
    for im in images:

        for group in group_names:
            random_size = randint(4, 10)
            random_dimension = (random_size, random_size)
            im_name = path.basename(im.filename)
            tiling_path = source_path.parent / group / (group + im_name)
            tiling = wallpapermaker(group, im, random_dimension)
            tiling.save(tiling_path)
