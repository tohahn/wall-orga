import pyglet, os, random, sys, time

def get_displays(display):
    displays = []
    
    for screen in display.get_screens():
        width = screen.width
        height = screen.height
        if width >= 3840 and height >= 2160:
            displays.append('big')
        elif width >= 2560 and height >= 1440:
            displays.append('medium')
        elif width >= 1920 and height >= 1080:
            displays.append('small')
        else:
            displays.append('tiny')

    return displays

def get_wallpapers(wall_dir):
    os.chdir(wall_dir)

    big = [f for f in os.listdir('./big') if (f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png'))]
    random.shuffle(big)
    medium = [f for f in os.listdir('./medium') if (f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png'))]
    random.shuffle(medium)
    small = [f for f in os.listdir('./small') if (f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png'))]
    random.shuffle(small)
    tiny = [f for f in os.listdir('./tiny') if (f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png'))]
    random.shuffle(tiny)

    return (big, medium, small, tiny)

def set_wall(wall_dir):
    platform = pyglet.window.get_platform()
    display = platform.get_default_display()

    displays = get_displays(display)
    
    big, medium, small, tiny = get_wallpapers(wall_dir)

    command = "feh --bg-fill"
    for dsp in displays:
        if dsp == 'big':
            command += " " + wall_dir + "/big/" + big.pop()
        elif dsp == "medium":
            command += " " + wall_dir + "/medium/" + medium.pop()
        elif dsp == "small":
            command += " " + wall_dir + "/small/" + small.pop()
        else:
            command += " " + wall_dir + "/tiny/" + tiny.pop()
    os.system(command)
    time.sleep(900)

if __name__ == "__main__":
    wall_dir = sys.argv[1]
    while True:
        set_wall(wall_dir)
