import warnings

class CustomerRequestWarning(Warning):
  pass

def calculate_remaining_time(km):
  '''
  This function estimates the remaining flight time when given the kilometers that remain for this flight. The function assumes an average speed of 15 km per minute and rounds down when calculating minutes. It returns a tuple of hours and then minutes remaining. 
  '''
  total_minutes = int(km / 15)
  minutes = total_minutes % 60
  hours = int(total_minutes / 60)
  return (hours, minutes)

def request_flight_attendant():
  '''
  This function raises a CustomerRequestWarning to let the flight attendants know that they are requested. 
  '''
  warnings.warn('A customer has requested attention!', CustomerRequestWarning)
