from controller import TestController
from view import TestView
from model import TestModel

import flet as ft


def main(page):
    # MVC set-up
    model = TestModel()
    controller = TestController(page, model)
    model.controller = controller  # important to set controller in model (in needed) before view
    view = TestView(controller, model)

    # Settings

    # NOTE: adding in setting, but remember controller has access to page too; so
    # you can set this values in a function of the controller, which I recommend to do.
    page.appbar = view.app_bar
    page.overlay.append(view.audio)
    page.overlay.append(view.bottom_sheet)
    page.overlay.append(view.file_picker)
    # page.banner = view.banner
    page.overlay.append(view.banner)
    # page.snack_bar = view.snack_bar
    page.overlay.append(view.snack_bar)
    page.floating_action_button = view.fab

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.on_keyboard_event = controller.on_keyboard
    page.theme_mode = "light"
    page.padding = 20
    # page.window_width = 600
    page.window.width = 600 # Updated to use Page.window.width
    # page.window_always_on_top = True
    page.window.always_on_top = True # Updated to use Page.window.always_on_top
    # page.window_resizable = False
    page.window.resizable = False # Updated to use Page.window.resizable
    # page.window_height = 500
    page.window.height = 500 # Updated to use Page.window.height

    # Debug: Print content before adding to page 
    print("view.content", view.content)

    # Ensure no None values are added to the page
    for item in view.content:
        if item is not None:
            print("item", item)
            if isinstance(item, ft.ListView):
                # Debug: Print child controls of ListView
                for child in item.controls:
                    if child is not None:
                        print("child", child)
                    else:
                        print("child is None")
            page.add(item)
        else:
            print("item is None")

    # Run
    # page.add(*view.content)


ft.app(target=main)
