from ._anvil_designer import star_1_borrower_registration_form_begin_4Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_4(star_1_borrower_registration_form_begin_4Template):
  def __init__(self,user_id, **properties):
    # Set Form properties and Data Bindings.
    self.userId = user_id
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_borrower_registration_form_copy_1_click(self, **event_args):
    open_form('bank_users.user_form')

  def submit_4_borrower_registration_form_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_5',userId=user_id)

 
    
    
    
    
