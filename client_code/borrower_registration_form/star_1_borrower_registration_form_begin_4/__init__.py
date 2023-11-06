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
    mother_toung = self.borrower_registration_mother_tounge_text.text
    marital_status = self.marital_status_borrower_registration_dropdown.selected_value
    spouse_name = self.borrower_registration_spouse_name_text.text
    marrege_date = self.marriage_date_date_pickeer.date
    user_id = self.userId
    if not marital_status or not mother_toung or not spouse_name or not marrege_date
    
    
    
