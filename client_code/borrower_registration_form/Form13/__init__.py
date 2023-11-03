from ._anvil_designer import Form13Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form13(Form13Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('borrower_registration_form.Form12')
    """This method is called when the button is clicked"""

  def button_2_click(self, **event_args):
    open_form('borrower_registration_form.Form14')
    """This method is called when the button is clicked"""

  def home_borrower_registration_form_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
    

    

