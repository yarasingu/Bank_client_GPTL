from ._anvil_designer import user_profileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import user_module

class user_profile(user_profileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.get_user_name_lable.text = user_module.name
    self.get_email_lable.text = user_module.email

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('bank_users.user_form')

