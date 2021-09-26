class Armor():
  def __init__(self, name, price, con, atk):
    self.name = name
    self.price = int(price)
    self.con = int(con)
    self.atk = int(atk)
    
  def __repr__(self):
    return self.name + ': ' + str(self.con) + ' concealment, ' + str(self.atk) + ' attack'
