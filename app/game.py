import curses


def g(stdscr: curses.window):
    from app import field
    from app import worker
    stdscr.clear()
    stdscr.keypad(True)

    field = worker.init_field(field)

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP:
            # Move up
            stdscr.clear()
            stdscr.addstr(0, 0, "UP")
        elif key == curses.KEY_DOWN:
            # Move down
            stdscr.clear()
            stdscr.addstr(0, 0, "DOWN")
        elif key == curses.KEY_LEFT:
            # Move left
            stdscr.clear()
            stdscr.addstr(0, 0, "LEFT")
        elif key == curses.KEY_RIGHT:
            # Move right
            stdscr.clear()
            stdscr.addstr(0, 0, "RIGHT")
        elif key == ord("q"):
            # Quit
            stdscr.clear()
            stdscr.addstr(0, 0, "QUIT")
            break
        stdscr.refresh()
