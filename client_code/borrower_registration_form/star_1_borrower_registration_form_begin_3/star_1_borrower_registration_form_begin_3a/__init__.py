from ._anvil_designer import star_1_borrower_registration_form_begin_3aTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_3a(star_1_borrower_registration_form_begin_3aTemplate):
  def __init__(self,user_id, **properties):
    # Set Form properties and Data Bindings.
    self.userId = user_id
    self.init_components(**properties)
    
  def home_borrower_registration_form_copy_1_click(self, **event_args):
    open_form('bank_users.user_form')

  # this is prew button 
  def button_1_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3',user_id = self.userId)
    
  def button_2_click(self, **event_args):
    father_name = self.father_name_br3a_text.text
    mother_name = self.mother_name_br3a_text.text
    father_age = self.father_age_br3a_text.text
    mother_age = self.mother_age_br3a_text.text
    user_Id = self.userId
    if not father_name or not mother_name or not father_age or not mother_age:
      Notification("please fill all the requred fields").show()
    else:
      anvil.server.call('add_borrower_step3a',father_name,mother_name,father_age,mother_age,user_Id)
      open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3b',user_id=user_Id)