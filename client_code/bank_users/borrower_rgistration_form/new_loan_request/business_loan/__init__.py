from ._anvil_designer import business_loanTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class business_loan(business_loanTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    open_form('bank_users.borrower_rgistration_form.new_loan_request.loan_type')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert('saved successfully!')
    open_form('bank_users.borrower_rgistration_form.new_loan_request.check_out_form')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form.new_loan_request')
