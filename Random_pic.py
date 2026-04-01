import Random as r 
from randomuser import Randomuser
import pandas as pd
some_list=r.generateusers(10)
some_list
for user in some_list:
  print(user.get_picture())
