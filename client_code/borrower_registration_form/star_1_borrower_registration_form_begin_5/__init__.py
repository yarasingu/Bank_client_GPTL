from ._anvil_designer import star_1_borrower_registration_form_begin_5Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_5(star_1_borrower_registration_form_begin_5Template):
  def __init__(self,userId, **properties):
    # Set Form properties and Data Bindings.
    self.user_id = userId
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_borrower_registration_form_home_button_click(self, **event_args):
    open_form('bank_users.user_form')

  def button_1_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_4',user=self.user_id)

  def button_for_next_begin_6_click(self, **event_args):
    spouse_mobile = self.borrower_registration_spouse_mobile_text.text
    spouse_company_name = self.borrower_company_name.text
    spouse_company_address = self.borrower_registration_company_adress_text.text
    spouse_profficen = self.borrower_spouse_profession.text
    user_id = self.user_id
    anvil.server.call('add_borrower_step5',spouse_mobile,spouse_company_name,spouse_company_address,spouse_profficen,user_id)
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_6',userId=user_id)