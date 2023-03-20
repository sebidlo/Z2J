import curses
# from curses import *


def main(stdscr):
    # Ustawiamy kursor konsoli na ukryty
    curses.curs_set(0)
    # Ustawiamy nieblokujący tryb klawiatury
    stdscr.nodelay(True)
    while True:
        # Pobieramy kod znaku naciśniętego przez użytkownika
        key = stdscr.getch()
        print(key)
        if key != curses.ERR:
            # Obsługujemy klawisze strzałek
            if key == curses.KEY_UP:
                stdscr.addstr(
                    0, 0, "Klawisz strzałki w górę został naciśnięty.")
            elif key == curses.KEY_DOWN:
                stdscr.addstr(
                    0, 0, "Klawisz strzałki w dół został naciśnięty.")
            elif key == curses.KEY_LEFT:
                stdscr.addstr(
                    0, 0, "Klawisz strzałki w lewo został naciśnięty.")
            elif key == curses.KEY_RIGHT:
                stdscr.addstr(
                    0, 0, "Klawisz strzałki w prawo został naciśnięty.")
                # obsługa innych klawiszy
            elif key == ord('a'):
                stdscr.addstr(0, 0, "Klawisz 'a' został naciśnięty.")
            elif key == ord('b'):
                stdscr.addstr(0, 0, "Klawisz 'b' został naciśnięty.")
        stdscr.refresh()


# Inicjujemy konsolę
curses.wrapper(main)
