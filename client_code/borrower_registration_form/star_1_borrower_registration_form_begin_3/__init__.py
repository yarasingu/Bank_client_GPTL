from ._anvil_designer import star_1_borrower_registration_form_begin_3Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_3(star_1_borrower_registration_form_begin_3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.userId = user_id
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    aadhar= self.borrower_registration_aadhar_text.text
    aadhar_card = self.borrower_registration_img_aadhar_file_loader
    pan = self.borrower_registration_pan_text.text
    pan_card=self.borrower_registration_img_pan_file_loader
    user_id = self.userId
    if not aadhar or not aadhar_card or not pan or not pan_card:
      Notification("Please Fill The All required fileds")
    else:
      anvil.server.call('add_borrower_step3',aadhar,aadhar_card,pan,pan_card,user_id)

