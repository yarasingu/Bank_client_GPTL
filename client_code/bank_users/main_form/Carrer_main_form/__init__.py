from ._anvil_designer import Carrer_main_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Carrer_main_form(Carrer_main_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


  def login_sign_up_main_form_link_click(self, **event_args):
    anvil.users.login_with_form()
    email = app_tables.users.client_readable(email)
    print(email)
    open_form('bank_users.user_form')
