from ._anvil_designer import star_1_lendor_rgistration_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_lendor_rgistration_form(star_1_lendor_rgistration_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    open_form('lendor_registration_form.Form27')
    """This method is called when the button is clicked"""
  
