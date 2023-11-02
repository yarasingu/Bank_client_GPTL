from ._anvil_designer import application_trackerTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class application_tracker(application_trackerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    data = tables.app_tables.user_profile.search()
    name = []
    email = []
    mobile = []
    status = []
    for i in data:
      name.append(i['name'])
      email.append(i['email'])
      mobile.append(i['mobile'])
      status.append(i['status'])

    if self.text_box_1.text in customer_id:
      index = customer_id.index(self.text_box_1.text)
      print(index)
      self.label_4.text = name[index]
      self.label_6.text = email[index]
      self.label_8.text = mobile[index]
      self.label_10.text = status[index]
      self.content_panel_1.visible = True