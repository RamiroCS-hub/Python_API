from Errors.databaseError import DatabaseError
from Errors.logicError import LogicError
from Errors.notFoundError import NotFoundError
def message_and_status(e):
  if(isinstance(e, DatabaseError)):
    return { 'status': 503, 'message': e.message }
  if(isinstance(e, LogicError)):
    return { 'status': 500, 'message': e.message } 
  if(isinstance(e, NotFoundError)):
    return { 'status': 404, 'message': e.message }
  return {'status': 500, 'message': f'Error not defined: {e}'}