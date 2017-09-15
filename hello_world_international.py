# created by andre hazim
#created on Sept 2017
#created for ICS3U
#Creates a hello world gui in 3 ways
import ui

def english_touch_up_inside (sender):
    #displays the English version
    view['hello_world_label'].text = ('Hello, World!')
def French_touch_up_inside (sender):
    #displays the French version
    view['hello_world_label'].text = ('Bonjour, le Monde!')
def Spanish_touch_up_inside (sender):
    #displays the Spanish version
    view['hello_world_label'].text = ('Hola, Mundo!')

view = ui.load_view()
view.present('sheet')
