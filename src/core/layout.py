from typing import Any
from core.singleton import Singleton

class Layout(metaclass=Singleton):
    def __init__(self) -> None:
        self.sf_nav = "navbar navbar-expand-lg navbar-dark bg-dark py-1"
        self.sf_nav_container = "container-fluid px-1 px-lg-2"
        self.sf_nav_brand = "navbar-brand"
        self.sf_nav_icon = "text-white fa-solid fa-house px-2"
        self.sf_nav_sb_toggle = "btn btn-primary"
        self.sf_nav_toggle = "navbar-toggler"
        self.sf_nav_toggle_icon = "navbar-toggler-icon"
        
        self.sf_nav_menu_collapse = "collapse navbar-collapse"
        self.sf_nav_menu = "navbar-nav ms-auto mb-0"
        self.sf_nav_menu_item = "nav-item"
        self.sf_nav_menu_item_active = "nav-link active"
        self.sf_nav_menu_item_inactive = "nav-link"

        self.sf_footer = "bg-dark mt-auto"
        self.sf_footer_container = "container px-1 px-lg-2 pt-1"
        self.sf_footer_text = "m-0 text-center text-white"
