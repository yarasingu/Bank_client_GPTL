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
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    aadhar= sel
    user_photo = self.borrower_registration_img_file_loader.file
    city = self.borrower_registration_cit_text.text
    user_id = self.userId
    if not gender or not user_photo or not city:
      Notification("Please Fill The All required fileds")
    else:
      anvil.server.call('add_borrower_step2',gender,user_photo,city,user_id)

