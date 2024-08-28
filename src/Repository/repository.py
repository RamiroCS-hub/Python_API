from db.db import get_db
import os
from Errors.databaseError import DatabaseError
from Errors.notFoundError import NotFoundError
class Repository:

  def __init__(self):
    self.db = get_db().cursor()
    if(os.environ.get('FIRST_SITUATION_ID') is None):
      self.firstSituationId = '1'
    else:
      self.firstSituationId = os.environ.get('FIRST_SITUATION_ID') 

  def get_first_situation(self):
    try:
      self.db.execute('SELECT * FROM Situations WHERE id = ?', (self.firstSituationId,))
      situation = self.db.fetchone()
      if situation is None:
        raise NotFoundError(f'There is no situation with id: {self.firstSituationId}')
      return situation
    except NotFoundError as e:
      raise e
    except Exception as e:
      raise DatabaseError(e)

  
  def get_options_id(self, situationId):
    try:
      self.db.execute('SELECT * FROM Choises_Situations WHERE situations_id = ?', (situationId,))
      choises = self.db.fetchall()
      if choises is None:
        raise NotFoundError(f'There is no options for situation with id: {situationId}')
      return choises
    except NotFoundError as e:
      raise e
    except Exception as e:
      raise DatabaseError(e)

  def get_options_by_id(self, options_ids):
    try:
      self.db.execute('SELECT id, description FROM Choises WHERE id IN ({})'.format(', '.join('?' * len(options_ids))), options_ids)
      return self.db.fetchall()
    except NotFoundError as e:
      raise e
    except Exception as e:
      raise DatabaseError(e)

  def get_situation_by_option_id(self, optionId):
    try:
      self.db.execute('SELECT * FROM Choises WHERE id = ?', (optionId,))
      situation = self.db.fetchone()
      if(situation is None):
        raise NotFoundError(f'There is no option with id: {optionId}')
      return situation
    except NotFoundError as e:
      raise e
    except Exception as e:
      raise DatabaseError(e)

  def get_situation_by_id(self, situationId):
    try:
      self.db.execute('SELECT * FROM Situations WHERE id = ?', (situationId,))
      situation = self.db.fetchone()
      if situation is None:
        raise NotFoundError(f'There is no situation with id: {situationId}')
      return situation
    except NotFoundError as e:
      raise e 
    except Exception as e:
      raise DatabaseError(e)