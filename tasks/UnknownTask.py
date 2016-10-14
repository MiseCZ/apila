from Task import Task

class UnknownTask(Task):
  def __init__(self, params, double_task, unknown_attributes):
    self.params = params
    self.double_task = double_task
    self.unknown_attributes = unknown_attributes

  def validate(self, errors):
    errors.append('Unknown command in def %s.' % str(self.params))

  def __str__(self):
    return 'Unknown command in def %s.' % str(self.params)

