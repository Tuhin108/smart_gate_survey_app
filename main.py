# main.py
# Main application file for the Smart Survey App (Android Focused)

import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.utils import platform

# Plyer is used to access hardware features like the camera
from plyer import camera

# Load the kv file for the UI design
Builder.load_file('survey.kv')

class HomeScreen(Screen):
    """
    The main screen of the application.
    Provides options to start a new survey for a sliding or swing gate.
    """
    pass

class GateSurveyScreen(Screen):
    """
    A base class for the survey screens.
    This will contain common functionality for both gate types.
    """
    gate_type = StringProperty('')
    image_path = StringProperty('a.png') # Default image
    recommendation = StringProperty('')

    def __init__(self, **kwargs):
        super(GateSurveyScreen, self).__init__(**kwargs)
        # Make sure your gate images (a.png, b.png, etc.) are in your project folder
        self.gate_images = ['a.png', 'b.png', 'c.png', 'd.png', 'e.png', 'f.png']
        self.current_gate_image_index = 0

    def on_enter(self, *args):
        """Called when the screen is displayed."""
        self.ids.site_image.source = 'placeholder.png' # Default placeholder
        self.ids.superimposed_gate.source = self.gate_images[self.current_gate_image_index]

    def take_picture(self):
        """
        Opens the device camera to capture an image using plyer.
        This will trigger the native camera app on Android.
        """
        try:
            # Define the path where the photo will be saved.
            # App.get_running_app().user_data_dir is a safe place to store app data.
            self.picture_path = os.path.join(App.get_running_app().user_data_dir, 'site_photo.jpg')
            camera.take_picture(filename=self.picture_path,
                                on_complete=self.camera_callback)
        except NotImplementedError:
            self.show_popup("Error", "Camera is not available on this device.")
        except Exception as e:
            self.show_popup("Error", f"An error occurred: {e}")

    def camera_callback(self, filepath):
        """
        Callback function that is called after the picture is taken.
        """
        # The filepath given by plyer might be cached, so we check our intended path.
        if os.path.exists(self.picture_path):
            self.ids.site_image.source = self.picture_path
            self.ids.site_image.reload() # Crucial to force Kivy to reload the image
        else:
            self.show_popup("Info", "No picture was taken or it was not saved correctly.")


    def next_gate_image(self):
        """Cycles to the next gate image for superimposition."""
        self.current_gate_image_index = (self.current_gate_image_index + 1) % len(self.gate_images)
        self.ids.superimposed_gate.source = self.gate_images[self.current_gate_image_index]

    def prev_gate_image(self):
        """Cycles to the previous gate image for superimposition."""
        self.current_gate_image_index = (self.current_gate_image_index - 1) % len(self.gate_images)
        self.ids.superimposed_gate.source = self.gate_images[self.current_gate_image_index]


    def get_recommendation(self):
        """
        Generates a gate recommendation based on the survey data.
        This is a simplified logic.
        """
        if self.gate_type == 'Sliding':
            try:
                clear_opening = float(self.ids.clear_opening.text)
                if clear_opening > 6:
                    self.recommendation = "Recommendation: Double Sliding Gate due to wide opening."
                else:
                    self.recommendation = "Recommendation: Single Sliding Gate is suitable."
            except ValueError:
                self.recommendation = "Please enter a valid clear opening."

        elif self.gate_type == 'Swing':
             try:
                opening_angle = float(self.ids.opening_angle.text)
                if opening_angle > 90:
                    self.recommendation = "Recommendation: Standard Swing Gate."
                else:
                    self.recommendation = "Recommendation: Consider a gate with special hinges for wider opening."
             except ValueError:
                self.recommendation = "Please enter a valid opening angle."

        self.show_popup("Gate Recommendation", self.recommendation)


    def show_popup(self, title, message):
        """Displays a popup message."""
        popup = Popup(title=title,
                      content=Label(text=message, halign='center'),
                      size_hint=(0.8, 0.3))
        popup.open()

    def save_survey(self):
        """Saves the survey data."""
        # In a real app, this would save to a database or a file.
        # For this example, we'll just show a confirmation popup.
        self.show_popup("Success", "Survey data has been saved!")


class SlidingGateScreen(GateSurveyScreen):
    """Screen for surveying sliding gates."""
    gate_type = StringProperty('Sliding')


class SwingGateScreen(GateSurveyScreen):
    """Screen for surveying swing gates."""
    gate_type = StringProperty('Swing')


class SurveyApp(App):
    """
    The main application class.
    """
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(SlidingGateScreen(name='sliding_gate'))
        sm.add_widget(SwingGateScreen(name='swing_gate'))
        return sm

if __name__ == '__main__':
    SurveyApp().run()
