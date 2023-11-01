from ._anvil_designer import borrower_registration_main_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class borrower_registration_main_form(borrower_registration_main_formTemplate):
  def __init__(self,user_id, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_main_form_link_copy_1_click(self, **event_args):
    open_form('bank_users.borrower_registration_main_form')

  def contact_main_form_link_click(self, **event_args):
    open_form('bank_users.borrower_registration_main_form.new_loan_request')

  def about_main_form_link_click(self, **event_args):
    open_form('bank_users.borrower_registration_main_form.borrower_profile')
