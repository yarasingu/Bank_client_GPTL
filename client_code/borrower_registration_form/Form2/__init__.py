from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_7')

  def button_2_click(self, **event_args):
    open_form('borrower_registration_form.Form3')

  def home_borrower_registration_form_click(self, **event_args):
    open_form('bank_users.user_form')

    

