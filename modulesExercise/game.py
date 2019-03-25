# import the draw module
import draw  # import whole module
from draw import draw_game  # import a function in the module
from draw import *  # import all object from the module

visual_mode = True

# custom import name
if visual_mode:
    import draw_visual as draw2
else:
    import draw_textual as draw2


def play_game():
    return "playing"


def main():
    result = play_game()
    draw.draw_game(result)
    draw_game(result)
    draw2.draw_game(result)


# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()
