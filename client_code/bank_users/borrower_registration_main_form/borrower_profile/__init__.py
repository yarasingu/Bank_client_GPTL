from ._anvil_designer import borrower_profileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class borrower_profile(borrower_profileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    data=app_tables.borrower.search()
    full_name=[]
    email_id=[]
    mobile_no=[]
    date_of_birth=[]
    city=[]
    upload_pan_card=[]
    full_name=self.label_2.text
    email_id=self.label_4.text
    mobile_no=self.label_6.text
    date_of_birth=self.label_8.text
    city=self.label_10.text
    upload_pan_card=self.label_12.text