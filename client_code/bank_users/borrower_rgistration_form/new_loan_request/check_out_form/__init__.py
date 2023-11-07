from ._anvil_designer import check_out_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class check_out_form(check_out_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.names= 'K-12 Educational loan'
    user_request = app_tables.product_borrower.get(names=self.names)
    interest_rate = user_request['interest_rate']
    self.int_rate.text=f" Interest rate : {interest_rate} %"
    #processing_fee_percentage = 0.05  # 5% processing fee
   


    
    self.coustmer_id = 1000

       
        # Fetch the data for the specific user from your table
    user_request = app_tables.user_profile.get(coustmer_id=self.coustmer_id)
   
    
   
      
    if user_request:
            min_amount = float(user_request['min_amount'])  # Convert to float
            tenure = float(user_request['tenure'])  # Convert to float
            max_amount = float(user_request['max_amount'])  # Convert to float
            
            # Calculate total repayment amount using the specified formula
           # total_repayment_min = min_amount * (1 + interest_rate * tenure)
            #total_repayment_max = max_amount * (1 + interest_rate * tenure)
            #total_repayment = total_repayment_max + total_repayment_min
            total_repayment = min_amount + (min_amount * (interest_rate / 100) * tenure)

            # Display the total repayment in the 'rp_amount' label
            self.trp_amount.text = f"Total Repayment Amount : {total_repayment}"
            P = float(total_repayment)  # Convert to float
            r = float(interest_rate) / 12 / 100  # Convert to float and calculate monthly interest rate
            n = int(tenure)  # Convert to integer

         # Calculate EMI using the correct exponentiation operator (**) for raising to a power
            emi = P * r * (1 + r)**n / ((1 + r)**n - 1)
            processing_fee = min_amount * tenure * (interest_rate / 100)
            self.pro_fee.text = f" Processing fee : {processing_fee}"

          # Display EMI in a label
            self.emi_details.text = f"EMI Details: {emi:.2f}"  # Display EMI rounded to two decimal places

    else:
            self.trp_amount.text = f"User {self.user_id} not found or data not available."
            self.int_rate.text = f"Interest Rate :{interest_rate} pa" 
            self.pro_fee.text = f"Processing Fee : {processing_fee}"

    # Any code you write here will run before the form opens.

  def submit_click(self, **event_args):
    alert('your data was submitted')
    open_form('bank_users.borrower_rgistration_form')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form.new_loan_request.k12_loan')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form')
