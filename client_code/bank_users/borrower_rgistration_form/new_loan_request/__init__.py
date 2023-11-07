from ._anvil_designer import new_loan_requestTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class new_loan_request(new_loan_requestTemplate):
  def __init__(self, **properties):
    self.userId=user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    min_amount=self.min_amount
    max_amount=self.max_amount
    tenure = self.tenure.selected_value
    anvil.server.call('add_user_profile', min_amount,max_amount,tenure,user_id)
   # self.coustmer_id = 1000
    #user_request = app_tables.user_profile.get(coustmer_id=self.coustmer_id)
    #max_amount = user_request['max_amount']
    #self.max_amount.text=f"{max_amount}"
  def button_1_copy_click(self, **event_args):
    if self.check_box_1.checked:
     open_form('bank_users.borrower_rgistration_form.new_loan_request.loan_type') 
    else:
      alert('Please select Terms and Conditions')
    def button_1_click(self, **event_args):
      open_form('bank_users.borrower_rgistration_form')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    alert('Agreements, Privacy Policy and Applicant should accept following:Please note that any information concealed (as what we ask for), would be construed as illegitimate action on your part and an intentional attempt to hide material information which if found in future, would attract necessary action (s) at your sole cost. Hence, request to be truthful to your best knowledge while sharing your details)')

   # max_amount = self.max_amount
    #min_amount = self.min_amount.text
    #tenure = self.tenure.selected_value
    #anvil.server.call('add_user_profile', min_amount, tenure, max_amount)