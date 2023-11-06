from ._anvil_designer import Form26Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...bank_users.borrower_rgistration_form import borrower_main_form_module

class Form26(Form26Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('borrower_registration_form.Form25')

  def button_2_click(self, **event_args):
    alert("Successfully Submitted!")
    user_id = borrower_main_form_module.userId
    print(user_id)
    user_profile_row = app_tables.user_profile.get(coustmer_id=user_id)
    if user_profile_row is not None:
      user_profile_row['usertype'] = 'borrower'
    open_form('bank_users.borrower_rgistration_form')
