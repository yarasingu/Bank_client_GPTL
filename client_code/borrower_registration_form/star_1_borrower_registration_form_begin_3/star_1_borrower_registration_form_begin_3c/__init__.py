from ._anvil_designer import star_1_borrower_registration_form_begin_3cTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_3c(star_1_borrower_registration_form_begin_3cTemplate):
  def __init__(self,user_id, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.userId = user_id

    # Any code you write here will run before the form opens.

  def home_borrower_registration_form_copy_1_click(self, **event_args):
    open_form('bank_users.user_form')

  def button_1_copy_1_copy_1_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3b')

  def Profesion_borrower_registration_form_drop_down_change(self, **event_args):
    profession =self.Profesion_borrower_registration_form_drop_down.selected_value
    user_Id = self.userId
    if profession == 'Self Employee':
      anvil.server.call('add_borrower_step3c',profession,user_Id)
      open_form('borrower_registration_form.borrower_registration_checkout_form',user_id=user_Id)
    elif profession == 'Business':
      anvil.server.call('add_borrower_step3c',profession,user_Id)
      open_form('borrower_registration_form.borrower_registration_checkout_form',user_id=user_Id)
    else:
      anvil.server.call('add_borrower_step3c',profession,user_Id)
      open_form('borrower_registration_form.borrower_registration_checkout_form',user_id=user_Id)
        
      
      
    