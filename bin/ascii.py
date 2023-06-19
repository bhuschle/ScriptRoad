import os
import random
import time
import argparse
import curses

def get_text_files(directory):
    return [file for file in os.listdir(directory) if file.endswith('.txt')]

def shuffle_files(file_list):
    random.shuffle(file_list)

def display_file(file_name, color, delay, directory, stdscr):
    file_path = os.path.join(directory, file_name)
    if not os.path.isfile(file_path):
        stdscr.addstr(0, 0, f"File '{file_name}' not found in the directory '{directory}'. Skipping...")
        stdscr.refresh()
        return

    with open(file_path, 'r') as file:
        content = file.read()

    term_height, term_width = stdscr.getmaxyx()

    if term_width < 10 or term_height < 3:
        stdscr.addstr(0, 0, "Terminal window too small to display the file.")
        stdscr.refresh()
        return

    lines = content.split('\n')

    if color == 'disco':
        disco_colors = [curses.COLOR_RED, curses.COLOR_GREEN, curses.COLOR_YELLOW, curses.COLOR_BLUE, curses.COLOR_MAGENTA, curses.COLOR_CYAN]
        for i, line in enumerate(lines[:term_height - 1]):
            current_color = disco_colors[i % len(disco_colors)]
            stdscr.addstr(i, 0, line[:term_width], curses.color_pair(current_color))
            stdscr.refresh()
            time.sleep(delay)
    elif color == 'random':
        random_color = random.randint(1, curses.COLOR_PAIRS - 1)
        stdscr.attrset(curses.color_pair(random_color))
        for i, line in enumerate(lines[:term_height - 1]):
            stdscr.addstr(i, 0, line[:term_width])
            stdscr.refresh()
            time.sleep(delay)
    else:
        color_pair = getattr(curses, 'COLOR_' + color.upper())
        for i, line in enumerate(lines[:term_height - 1]):
            stdscr.addstr(i, 0, line[:term_width], curses.color_pair(color_pair))
            stdscr.refresh()
            time.sleep(delay)


def clear_screen(stdscr):
    stdscr.clear()
    stdscr.refresh()


def main(directory, delay, color, timer):
    try:
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        stdscr.timeout(0)

        curses.start_color()
        curses.use_default_colors()
        for i in range(min(curses.COLORS, curses.COLOR_PAIRS)):
            curses.init_pair(i + 1, i, -1)

        while True:
            txt_files = get_text_files(directory)
            shuffle_files(txt_files)

            try:
                for file in txt_files:
                    clear_screen(stdscr)
                    display_file(file, color, delay, directory, stdscr)
                    file_name = file[:-4].upper()
                    file_name_pos = (curses.LINES - 1, curses.COLS - len(file_name) - 1)
                    if color == 'disco':
                        file_name_color = curses.COLOR_CYAN
                    elif color == 'random':
                        file_name_color = random.randint(1, curses.COLOR_PAIRS - 1)
                    else:
                        file_name_color = getattr(curses, 'COLOR_' + color.upper())
                    stdscr.addstr(*file_name_pos, file_name, curses.color_pair(file_name_color))
                    stdscr.refresh()
                    time.sleep(timer)
            except KeyboardInterrupt:
                clear_screen(stdscr)
                break

    except KeyboardInterrupt:
        clear_screen(stdscr)

    finally:
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--delay', type=float, default=0.1, help='Time delay in seconds between each line')
    parser.add_argument('-c', '--color', default='white', help='Color of the displayed text')
    parser.add_argument('-t', '--timer', type=float, default=1.0, help='Time in seconds to wait between each file')
    args = parser.parse_args()

    directory = '/path/to/ascii/files/'
    delay = args.delay
    color = args.color.lower()
    timer = args.timer

    if color == 'disco':
        print("Running in disco color mode!")
    elif color == 'random':
        print("Running in random color mode!")

    main(directory, delay, color, timer)

