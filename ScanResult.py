#This class is the template for ScanResults objects

class ScanResult:
  #Constructor
  def __init__(self, source, ranking, engine, category, feedback):
    self.source = source
    self.ranking = ranking
    self.engine = engine
    self.category = category
    self.feedback = feedback