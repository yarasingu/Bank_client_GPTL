from ._anvil_designer import star_1_borrower_registration_form_beginTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin(star_1_borrower_registration_form_beginTemplate):
  def __init__(self, user_id,**properties):
    self.userId = user_id
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def next_butto_for_step_2_click(self, **event_args):
    
    open_form('borrower_registration_form.star_1_borrower_registration_form1')

  def button_1_click(self, **event_args):
    open_form('bank_users.user_form')


    
 
