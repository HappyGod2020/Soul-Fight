from pygame import display, FULLSCREEN, event, QUIT, font
from core.settings import GUI_SETTINGS
from core.ManagerScreen import ManagerScreen
from GUI.MenuScreen import MenuScreen

class Game:
    def __init__(self):
        WIDTH = GUI_SETTINGS.WIDTH
        HEIGHT = GUI_SETTINGS.HEIGHT
        args = [(WIDTH, HEIGHT)]
        if GUI_SETTINGS.is_FullScreen:
            args.append(FULLSCREEN)
        self.screen = display.set_mode(*args)
        display.set_caption("Soul Fight DEMO")
        font.init()

        self.event_array = []

        self.manager_screen = ManagerScreen(self)  # Передача Game в ManagerScreen
        self.manager_screen.select_screen(MenuScreen)  # Установка стартового экрана

        self.update()

    def update(self):
        self.is_game = True
        while self.is_game:
            self.screen.fill((0, 0, 0))
            self.event_loop()
            self.manager_screen.current_screen.render()
            display.update()

    def event_loop(self):
        for e in event.get():
            if e.type == QUIT:
                self.is_game = False
            for fun in self.event_array:
                fun(e)
