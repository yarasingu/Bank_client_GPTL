from ._anvil_designer import borrower_rgistration_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..main_form import main_form_module
from ..user_form import user_module
class borrower_rgistration_form(borrower_rgistration_formTemplate):
  def __init__(self, **properties):
    email= main_form_module.email
    self.label_1.text = user_module.get_name(email)
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.borrower_rgistration_form.borrower_profile')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.borrower_rgistration_form.new_loan_request')

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.borrower_rgistration_form.application_tracker')

  def link_8_click(self, **event_args):
    """This method is called when the link is clicked"""
    alert("logout sucessfully")
    anvil.users.logout()
    open_form('bank_users.main_form')

  def home_borrower_registration_form_copy_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form')

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.borrower_rgistration_form.borrower_foreclosure_request')

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.borrower_rgistration_form.borrower_loan_close')

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.borrower_rgistration_form.borrower_discount_coupons')

  def faqs_borrower_home_main_form_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form.borrower_faqs')

  def about_borrower_registration_form__click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form.borrower_about')

  def location_borrower_main_form_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form.borrower_location')
