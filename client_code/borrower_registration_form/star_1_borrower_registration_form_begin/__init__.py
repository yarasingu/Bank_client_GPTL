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

  def home_borrower_registration_form_click(self, **event_args):
    open_form('bank_users.user_form')

  def next_butto_for_step_2_click(self, **event_args):
    full_name = self.borrower_full_name_test.text
    mobile_no = self.borrower_mobile_number_text.text
    dob = self.borrower_date_of_birth_date_picker.date
    user_id = self.userId
    if not full_name or not mobile_no or not dob:
      Notification("plz enter All Details For Proceed Next")
    else:
      anvil.server.call('add_borrower_step1',full_name,mobile_no,dob,user_id)
      Notification("step 1 form fill up submited sucessfull")
      open_form('borrower_registration_form.star_1_borrower_registration_form_begin_2',user_id = user_id)
    
    

  


    
 
