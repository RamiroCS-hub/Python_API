from Repository.repository import Repository
from Errors.databaseError import DatabaseError
from Errors.logicError import LogicError
from Errors.notFoundError import NotFoundError
class Service:
  def __init__(self):
    self.repo = Repository()
  def get_first_situation(self):
    return self.repo.get_first_situation()
  
  def get_options_by_situation_id(self, situationId):
    try:
      optionsSituationsIds = self.repo.get_options_id(situationId)
      optionsIds = []
      for optionsSituationIds in optionsSituationsIds:
        optionsIds.append(optionsSituationIds[0])
      return self.repo.get_options_by_id(optionsIds)
    except DatabaseError as e:
      raise e 
    except NotFoundError as e:
      raise e
    except Exception as e:
      raise LogicError(e)
  
  def get_situation_id_by_option_id(self, optionId):
    situationId = self.repo.get_situation_by_option_id(optionId)
    print(situationId)
    situation = self.repo.get_situation_by_id(situationId[2])
    return situation


  