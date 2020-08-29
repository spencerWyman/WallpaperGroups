from sys import argv
from PIL import Image
from wallpapermakers import wallpapermaker

command = argv[1]
group_name = argv[2]
image_path = argv[3]

im = Image.open(image_path)

if command == 'show':
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
