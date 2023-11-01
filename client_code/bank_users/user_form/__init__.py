from ._anvil_designer import user_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from . import user_module

class user_form(user_formTemplate):
  def __init__(self,email, **properties):
    self.init_components(**properties)
    # self.user_name_lable = user_module.get_name(email)[0]
    
  def logout_user_form_link_click(self, **event_args):
    anvil.users.logout()
    open_form('bank_users.main_form')

  # this function is use for new borrower signup and check the user already signup or not
  def borrower_user_form_link_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form')


  

  def lendor_user_form_link_click(self, **event_args):
    open_form('lendor_registration_form.star_1_lendor_rgistration_form')

  def view_profile_user_home_click(self, **event_args):
    open_form('bank_users.user_form.user_profile')


