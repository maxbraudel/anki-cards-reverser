from aqt import gui_hooks
from aqt import mw
from anki.hooks import wrap
from aqt.reviewer import Reviewer
from aqt.utils import showInfo
from aqt.qt import *

# Global state to track the current mode
card_order_mode = "normal"

def add_enabled_div(html, card, context):
    if card_order_mode == "reversed":
        # Add the "reversed" class to elements with class "card"
        html = html.replace('class="prettify-flashcard"', 'class="prettify-flashcard reversed-mode"')
        
        # Create a div with "enabled" text and append it to the card's HTML
        enabled_div = "<div class='enabled-marker'>Ordre inversé</div>"
        return html + enabled_div
    return html

# Add CSS to style the enabled div
def append_css_to_head():
    css = """
    <style>
        .enabled-marker {
            position: fixed;
            bottom: 10px;
            right: 10px;
            background-color: #4CAF50;
            color: white;
            padding: 5px 10px;
            border-radius: 3px;
            font-size: 12px;
            font-family: Arial, sans-serif;
        }
    </style>
    """
    return css

# Wrap the _init_web_view method to inject CSS
def on_web_view_init(web_content, context):
    if isinstance(context, Reviewer):
        web_content.head += append_css_to_head()

def set_card_order_mode(mode):
    global card_order_mode
    card_order_mode = mode
    mw.reset()  # Refresh the current card display

def setup_menu():
    # Create Cards Order menu
    cards_order_menu = QMenu("Ordre des faces", mw)
    mw.form.menubar.addMenu(cards_order_menu)
    
    # Create action group for mutually exclusive options
    mode_group = QActionGroup(mw)
    
    # Normal mode action
    normal_action = QAction("Normal (Recto > Verso)", mw)
    normal_action.setCheckable(True)
    normal_action.setChecked(True)
    normal_action.triggered.connect(lambda: set_card_order_mode("normal"))
    mode_group.addAction(normal_action)
    cards_order_menu.addAction(normal_action)
    
    # Reversed mode action
    reversed_action = QAction("Inversé (Verso > Recto)", mw)
    reversed_action.setCheckable(True)
    reversed_action.triggered.connect(lambda: set_card_order_mode("reversed"))
    mode_group.addAction(reversed_action)
    cards_order_menu.addAction(reversed_action)

# Register the hooks
gui_hooks.card_will_show.append(add_enabled_div)
gui_hooks.webview_will_set_content.append(on_web_view_init)

# Setup the menu when Anki starts
setup_menu()