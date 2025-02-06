import curses


def g(stdscr: curses.window):
    from app import field, worker

    stdscr.clear()
    stdscr.keypad(True)

    field = worker.init_field(field)

    stdscr.addstr(0, 0, field.__repr__())
    stdscr.refresh()

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP:
            # Move up
            stdscr.clear()
            field.move_up()
            stdscr.addstr(0, 0, field.__repr__())
        elif key == curses.KEY_DOWN:
            # Move down
            stdscr.clear()
            field.move_down()
            stdscr.addstr(0, 0, field.__repr__())
        elif key == curses.KEY_LEFT:
            # Move left
            stdscr.clear()
            field.move_left()
            stdscr.addstr(0, 0, field.__repr__())
        elif key == curses.KEY_RIGHT:
            # Move right
            stdscr.clear()
            field.move_right()
            stdscr.addstr(0, 0, field.__repr__())
        elif key == ord("q"):
            # Quit
            stdscr.clear()
            stdscr.addstr(0, 0, field.__repr__())
            break
        stdscr.refresh()
