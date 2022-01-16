import pygame


class Window:
    """Shows everything onto the users screen through adding components to it and displaying those added components"""

    components = []
    screens = []
    background_color = (0, 0, 0)
    window = None
    
    def get_window(self):
        """ summary: Other functions from use this to put stuff on the screen like drawing and displaying text
            params: None
            returns: Gets the actual window of the window (from pygame.display.set_mode())
        """
        return self.window

    def __init__(self, length, height, title, background_color):
        """ summary: creates a window with the length, height, and title of the values given

            params:
                length: int; the length of the window
                height: int; the height of the window
                title: String; the title displayed of the window

            returns: None
        """

        self.components = []
        self.window = pygame.display.set_mode((length, height))
        pygame.display.set_caption(title)
        self.background_color = background_color

    def add(self, component):
        """ summary: adds the component to the window

            params: 
                component: Component; the component that is going to be added to the window

            returns: None
        """

        self.components.append(component)

    def add_all(self, components):
        """ summary: adds all the components to the window - calls Window.add() for each component in components

            params: 
                components: list of Component; the components that are going to be added to the window

            returns: None
        """

        for component in components:
            self.components.append(component)

    def remove(self, component):
        """ summary: removes the component from the window

            params: 
                component: Component; the component that is going to be removed from the window

            returns: None
        """

        self.components.remove(component)

    def component_is_selected(self, component):
        is_selected = False
        try:
            if component.got_clicked():
                is_selected = True

        # Not all components are of type ClickableComponent, so this catches that error
        # Needs to be ClickableComponent since code calls got_clicked(), which only ClickableComponent has
        except AttributeError:
            print(type(component))
        return is_selected

    def run(self):
        """ summary: calls Component.run() for every component in Window.components and only calls Component.render() if the component is_visible
            params: None
            returns: None
        """
        self.get_window().fill(self.background_color)
        selected_component = None
        all_components = []
        for screen in self.screens:
            if screen.is_visible:
                screen.run()

            all_components += screen.get_components()
            for component in screen.get_components():
                component.is_visible = screen.is_visible
                if self.component_is_selected(component):
                    selected_component = component

                if component.is_runnable:
                    component.run()

                if screen.is_visible:
                    component.render()

        for component in self.components:
            # Only visible components should be displayed onto the screen
            if component.is_visible:
                component.render()

            if component.is_runnable:
                component.run()

            if self.component_is_selected(component):
                selected_component = component

        for component in all_components + self.components:
            if selected_component is not None:
                component.is_selected = False

        # All component's is_selected is set to False so this sets the selected_component.is_selected to True
        if selected_component is not None:
            selected_component.is_selected = True

        pygame.display.update()

    def set_visible(self, components, is_visible):
        """ summary: sets is_visible in all the components in components to the value passed in the parameter is_visible

            params:
                components: List of Component; the list of all the components that their visibility are going to be changed
                is_visible: boolean; the visibility of all the components in components are going to be set to this value

            returns: None
        """
        for component in components:
            component.is_visible = is_visible

    def display_screens(self, screens):
        """ summary: makes all screens disappear from the screen except the screen(s) in screen
            Also adds all screen in screens that aren't present in Window.screens

            params:
                screens: List of Screen; the screens that should be displayed on the screen

            returns: None
        """
        for component in self.components:
            component.is_visible = False

        for screen in self.screens:
            if not screens.__contains__(screen):
                screen.is_visible = False

            else:
                screen.is_visible = True

    def display_components(self, components):
        """ summary: makes everything on the screen disappear except the component(s) in components

            params:
                components: List of Component; the components that should be displayed on the screen

            returns: None
        """
        for component in self.components:
            if not components.__contains__(component):
                component.is_visible = False

            else:
                component.is_visible = True

    def add_screen(self, screen):
        """ summary: adds all the components from the screen to the window

            params: 
                screen: Screen; the screen which has the components which are going to be added to the screen
            
            returns: None
        """
        
        self.screens.append(screen)
    
    def set_screen_visible(self, screen, is_visible):
        """ summary: for each component in the screen it sets the component.is_visible to the value passed by the parameter is_visible

            params: 
                screen: Screen; the screen which has the components which their property is_visible is going to be modified
                is_visible: boolean; the value which all the components is_visible attribute are going to be set to
            
            returns: None
        """

        for component in screen.components:
            component.is_visible = is_visible
        screen.is_visible = is_visible
        
