from ._anvil_designer import star_1_borrower_registration_form_begin_3bTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_3b(star_1_borrower_registration_form_begin_3bTemplate):
  def __init__(self,user_id, **properties):
    # Set Form properties and Data Bindings.
    self.userId = user_id
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_borrower_registration_form_copy_1_click(self, **event_args):
    open_form('bank_users.user_form')

  def button_1_copy_1_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3a',user_id = self.userId)

  def button_2_click(self, **event_args):
    mother_tounge = self.mother_tongue_text.text
    user_id = self.userId
    if not  mother_tounge:
      Notification("please enter you details").show()
    else:
      @anvil.server.call('',mother_tounge,user_id)
      open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3c',user_Id=user_id)