symbol = "█"

color_red = "\033[91m"
color_purple = "\33[95m"
color_blue1 = "\33[34m"
color_blue2 = "\33[36m"
color_blue3 = "\33[96m"
color_green1 = "\033[92m"
color_green2 = "\033[32m"
color_brown = "\33[33m"
color_yellow = "\33[93m"
color_grey = "\33[37m"
color_default = "\033[0m"
color_list = (color_red, color_purple, color_blue1, color_blue2, color_blue3,
              color_green1, color_green2, color_yellow, color_brown, color_grey, color_default)


def print_variable_name(variable: object) -> None:
    for name, value in globals().items():
        if id(value) == id(variable):
            return name


def show_colors() -> None:
    for color in color_list:
        print(f"{color}{3 * symbol}", end="")

    print(color_default)

    for color in color_list:
        print(f"{color}{3 * symbol} {print_variable_name(color)}")

    input("")
