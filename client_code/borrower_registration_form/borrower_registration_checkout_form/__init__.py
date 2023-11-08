from ._anvil_designer import borrower_registration_checkout_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class borrower_registration_checkout_form(borrower_registration_checkout_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_borrower_registration_form_click(self, **event_args):
    open_form('bank_users.user_form')

  def prev_borrower_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass



  
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass




