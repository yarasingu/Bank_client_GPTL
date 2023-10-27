from ._anvil_designer import star_1_borrower_registration_form_step_2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_step_2(star_1_borrower_registration_form_step_2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_borrower_registration_form_step1_click(self, **event_args):
    open_form('bank_users.user_form')

  def borrower_registration_star1_registration_prev_button_for_step_1_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form')

  def borrower_registration_star1_registration_next_button_for_step_3_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_step_3')

  def button_1_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form1')
    """This method is called when the button is clicked"""

  def button_2_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_step_3')
    """This method is called when the button is clicked"""
  

    




  


  

  


  


