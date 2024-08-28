import json
import os
from db.db import get_db


class Seeder():

  def __init__(self):
    self.db = get_db()

  def seed_situations(self):
    with open('db/situations.json', 'r') as arch:
      data = json.load(arch)
      flag = False
      for row in data:
        try:
          self.db.execute('INSERT INTO Situations (description, id) VALUES (?, ?)', (row['description'], row['id']))
          # Set the first situation id in a enviroment variable
          if(flag != True):
            os.environ['FIRST_SITUATION_ID'] = str(row['id'])
            flag = True
        except Exception as e:
          print(f'An error ocurred filing the situations table: {e}')
          exit(1)
      self.db.commit()
      print('Situations seeded successfully!')

  def seed_choises(self):
    with open('db/choises.json', 'r') as arch:
      data = json.load(arch)

      for row in data:
        try:
          self.db.execute('INSERT INTO Choises (description, next_id) VALUES (?, ?)', (row['description'], row['situation']))
        except Exception as e:
          print(f'An error ocurred filing the choises table: {e}')
          exit(1)
      self.db.commit()
      print('Choises seeded successfully!')

  def seed_choises_situations(self):
    with open('db/situations.json', 'r') as arch:
      data = json.load(arch)
      for row in data:
        try:
          for choise in row['choices']:
            self.db.execute('INSERT INTO Choises_Situations (choises_id, situations_id) VALUES (?, ?)', (choise, row['id']))
          self.db.commit()
        except Exception as e:
          print(f'An error ocurred filing the choises_situations table: {e}')
          exit(1)
    print('Choises_situations seeded successfully!')