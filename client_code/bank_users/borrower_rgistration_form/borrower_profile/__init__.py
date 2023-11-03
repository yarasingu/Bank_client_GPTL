from ._anvil_designer import borrower_profileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class borrower_profile(borrower_profileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('bank_users.borrower_registration_main_form.boorrower_edit_profile')

  def button_1_copy_click(self, **event_args):
    open_form('bank_users.borrower_rgistration_form')
