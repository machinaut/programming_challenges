#!/usr/bin/env python
import sys

### Helper Classes ###
class CargoUnit():
	"""Keep track of info related to our plane's cargo"""
	def __init__(self, SKU, weight, value):
		"""Basic initialize that takes in the:
			SKU: Stock Keeping Unit
			weight: in pounds
			cost: in dollars
			
			it also sets the "cost" to the
			ratio of value to weight.
			"""
		
		self.SKU = SKU
		self.weight = weight
		self.value = value
		self.cost = float(value)/weight
	
	def __str__(self):
		return "SKU: %s, weight:%s, value: %s, cost: %s" %\
				(self.SKU, self.weight, self.value, self.cost)

class Manifest(dict):
	def cost(self):
		pass

### Functional Logic ###
def fit_cost(weight, manifest):
	"""Takes the weight to drop and the cargo manifest
		and returns a dict of "Number To Drop" indexed by SKU.
		
		This assumes that the manifest is sorted from least
		to greatest cost.
		"""
	
	drop = {}
	drop[manifest[0].SKU] = int(weight/cargo.weight)+1
	for cargo in manifest[1:]:
		
### Main Block ###
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "Please provide a filename."
		exit(1)
	f = open(sys.argv[1])
	
	weight_to_drop = int(f.readline().strip())
	
	manifest = []
	for line in f:
		line_tokens = line.split()
		manifest.append(CargoUnit(line_tokens[0], *map(int, line_tokens[1:])))
	
	cargo_cmp = lambda x,y: int(x.cost - y.cost)
	manifest.sort(cargo_cmp)
	
	for cargo in manifest:
		print cargo
