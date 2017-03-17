#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# Example module
# Copyright (C) 2014 Musikhin Andrey <melomansegfault@gmail.com>

import kivy
from kivy.config import Config
Config.set("input", "mouse", "mouse, disable_multitouch")
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button,Label
from kivy.uix.textinput import TextInput
from Table.Table import Table



class MainScreen(BoxLayout):
    """docstring for MainScreen"""
    def __init__(self,n):
        print("Mi n: "+str(n))
        super(MainScreen, self).__init__()
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.my_table = Table()
        self.my_table.cols = 3
        self.my_table.add_button_row('Xi', 'Xn' , "Random")
        for i in range(110):
            self.my_table.add_row(
                [Button, {'text': str(i), 'color_widget': [0, 0, 0.5, 1],'color_click': [0, 1, 0, 1]}],
                [TextInput, {'text': str(i+1),'color_click': [1, 0, .5, 1], 'readonly':True}],
                [TextInput, {'text': str(i*20), 'color_click': [1, 0, .5, 1], 'readonly': True}]
            )
        self.my_table.label_panel.visible = False
        self.my_table.label_panel.height_widget = 50
        self.my_table.number_panel.auto_width = False
        self.my_table.number_panel.width_widget = 100
        self.my_table.number_panel.visible = False
        self.my_table.grid.color = [1, 0, 0, 1]
        self.my_table.label_panel.color = [0, 1, 0, 1]
        self.my_table.number_panel.color = [0, 0, 1, 1]
        self.my_table.scroll_view.bar_width = 10
        self.my_table.scroll_view.scroll_type = ['bars']
        print("ROW COUNT:", self.my_table.row_count)
        self.add_widget(self.my_table)

    def _keyboard_closed(self):
        pass

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        """ Method of pressing keyboard  """
        if keycode[0] == 273:   # UP
            print(keycode)
            self.my_table.scroll_view.up()
        if keycode[0] == 274:   # DOWN
            print(keycode)
            self.my_table.scroll_view.down()
        if keycode[0] == 281:   # PageDown
            print(keycode)
            self.my_table.scroll_view.pgdn()
        if keycode[0] == 280:   # PageUp
            print(keycode)
            self.my_table.scroll_view.pgup()
        if keycode[0] == 278:   # Home
            print(keycode)
            self.my_table.scroll_view.home()
        if keycode[0] == 279:   # End
            print(keycode)
            self.my_table.scroll_view.end()



class App(App):
    """ App class """
    def build(self):
        return MainScreen(80)

    def on_pause(self):
        return True

App().run()