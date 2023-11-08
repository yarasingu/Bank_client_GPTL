from ._anvil_designer import borrower_registration_checkout_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...bank_users.user_form import user_module

class borrower_registration_checkout_form(borrower_registration_checkout_formTemplate):
  def __init__(self, **properties):
    self.check_out_name_lable.text = "yarisingu Tarun"
    self.chekc_out_mail_lable.text = "yarisingutarun@gamil.com"
    self.check_out_mobile_lable.text = "9550634578"
    self.check_out_dob_lable.text = "2001-03-14"
    self.check_out_pan_lable.text = "BAMPY3901R"
    self.check_out_aadhaar_number_lable.text = "887358570572"
    
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_borrower_registration_form_click(self, **event_args):
    open_form('bank_users.user_form')

  def prev_borrower_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass



  
  def button_2_click(self, **event_args):
    alert("Successfully Submitted! wait  for Approvel")
    user = anvil.users.get_user()
    email = user['email']
    user_profile_row = app_tables.user_profile.get(email_user=email)
    if user_profile_row is not None:
      user_profile_row['usertype'] = 'borrower'
    open_form('bank_users.borrower_rgistration_form')


