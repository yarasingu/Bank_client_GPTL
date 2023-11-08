from ._anvil_designer import main_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..user_form import user_module
from . import main_form_module
from ..borrower_rgistration_form import borrower_main_form_module

class main_form(main_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    


  #it is used to login or sign up the user
  def login_sign_up_main_form_link_click(self, **event_args):
    anvil.users.login_with_form()
    current_user = anvil.users.get_user()
    if current_user:
      user_email = current_user['email']
      print(user_email)
      check_user_already_exist = user_module.check_user_profile(user_email)
      print(check_user_already_exist)

      # this statement is used to check whether the user is new or old
      if check_user_already_exist == None:
        print("main if statement was executed")
        user_module.add_email_and_user_id(user_email)
        main_form_module.email=user_email
        main_form_module.flag=True
        open_form('bank_users.user_form')
      else:
        # then her check the user is completed borrower registration form or not 
        check_user_registration= user_module.check_user_registration_form_done_or_not_engine(user_email)
        print("main else statement was executed")
        if check_user_registration:
          main_form_module.email=user_email
          open_form('bank_users.borrower_rgistration_form')
        else:
          main_form_module.email=user_email
          main_form_module.flag=False
          open_form('bank_users.user_form')


  #form maping no need to change 
  def about_main_form_link_click(self, **event_args):
    open_form('bank_users.main_form.about_main_form')

  def contact_main_form_link_click(self, **event_args):
    open_form('bank_users.main_form.contact_main_form')

  def carrer_main_form_link_click(self, **event_args):
    open_form('bank_users.main_form.Carrer_main_form')

  def location_main_form_link_click(self, **event_args):
    open_form('bank_users.main_form.location_main_form')







