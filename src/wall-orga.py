from PIL import Image
import sys, os

def prepare_dir(wall_dir):
    os.chdir(wall_dir)
    wall_list = [f for f in os.listdir('.') if (f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png'))]
    os.mkdir('./big')
    os.mkdir('./medium')
    os.mkdir('./small')
    os.mkdir('./else')
    return wall_list

def sort_images(wall_list):
    for wall in wall_list:
        im = Image.open(wall)
        width, height = im.size
        if width >= 3840 and height >= 2160:
            os.rename(wall, './big/' + os.path.basename(wall))
        elif width >= 1920 and height >= 1080:
            os.rename(wall, './medium/' + os.path.basename(wall))
        elif width >= 1600 and height >= 900:
            os.rename(wall, './small/' + os.path.basename(wall))
        else:
            os.rename(wall, './else/' + os.path.basename(wall))

if __name__ == "__main__":
    wall_dir = sys.argv[1]
    wall_list = prepare_dir(wall_dir)
    sort_images(wall_list)

