import aux_functions

class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = []

  def deposit(self, am, desc = ''):
    self.ledger.append({"amount" : am, "description" : desc})

  def withdraw(self, am, desc = ''):
    if self.check_funds(am):
      self.ledger.append({"amount" : am * -1, "description" : desc})
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    
    for d in self.ledger:
      balance += d['amount']

    return balance

  def transfer(self, am, other):
    if self.check_funds(am):
        self.withdraw(am, f"Transfer to {other.category}")
        other.deposit(am, f"Transfer from {self.category}")
        return True
    else:
        return False

  def check_funds(self, am):
    if am > self.get_balance():
      return False
    else:
      return True

  def __str__(self):
    output = []
    title = self.category.center(30, '*')
    output.append(title)
    output.append('\n')

    for line in self.ledger:
      num = f"{float(line['amount']):.2f}"

      if len(line['description']) > 23:
        output.append(line['description'][:23])
        dif = 30 - len(line['description'][:23])
      else:
        output.append(line['description'])
        dif = 30 - len(line['description'])

      num = num.rjust(dif, ' ')
      output.append(num)
      output.append('\n')
    
    output.append(f"Total: {self.get_balance():.2f}")
      
    return f"{''.join(output)}"

def create_spend_chart(categories):
  print()
  gastos = aux_functions.get_percentages(categories)
  porcentagens = aux_functions.build_bars(gastos)
  nomes = aux_functions.get_category_names(categories)
  result = aux_functions.show_bars_and_category_names(nomes, porcentagens)

  return result