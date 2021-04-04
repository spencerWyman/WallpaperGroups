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
    source_path = Path(argv[2])
    im = Image.open(source_path)
    save_path = source_path.parent / 'images'
    if not save_path.is_dir():
        save_path.mkdir()
    for tilename in group_names:
        print(tilename)
        image = wallpapermaker(tilename, im)
        image.save(f'images/{tilename}.png')

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
