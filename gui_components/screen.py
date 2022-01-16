from gui_components.component import Component


class Screen:
    components = []
    is_visible = True

    def get_components(self):
        return self.components

    def setup(self):
        pass

    def run(self):
        pass

    def un_setup(self):
        pass
