from ._anvil_designer import star_2_borrower_registration_form_step_1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_2_borrower_registration_form_step_1(star_2_borrower_registration_form_step_1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_borrower_registration_form_step3_click(self, **event_args):
    open_form('bank_users.user_form')

  def back_borrower_user_home_registertion_button_click(self, **event_args):
    open_form('borrower_registration_form.step2_borrower_registration_form')

  def button_2_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_step_3')
    """This method is called when the button is clicked"""

  def button_1_click(self, **event_args):
    open_form('borrower_registration_form.star_2_borrower_registration_form_step_2')
    """This method is called when the button is clicked"""
    

    

