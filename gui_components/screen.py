from gui_components.component import Component


class Screen:
    """Is the only thing that shows on the window at a time"""

    components = []
    is_visible = True

    def get_components(self):
        """ summary: gets all the screen's components
            params: None
            returns: all the screen's components
        """
        return self.components

    def setup(self):
        pass

    def run(self):
        pass

    def un_setup(self):
        pass
