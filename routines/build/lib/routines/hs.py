import argparse
import hashlib as hl
import os.path as path

def readTxt(file):
	with open(file) as f:
		try:
			return f.read().encode("utf8"), " %s" % file
		except (UnicodeDecodeError, UnicodeDecodeError):
			return False

def readByte(file):
	with open(file, "rb") as f:
		try:
			return f.read(), "*%s" % file
		except (UnicodeDecodeError, UnicodeDecodeError):
			return False

def computeHash(file, algorithm):
	if not path.exists(file):
		print("No such file: %s" % file)
		exit(1)
	if path.isdir(file):
		print("%s is a Directory" % file)
		exit(1)
	cont, m = readTxt(file) or readByte(file)
	
	hs = algorithm(cont)
	del cont
	try:
		dig = hs.hexdigest() 
	except TypeError:
		dig = hs.hexdigest(20)
	dig = dig + " " +  m
	del m
	print(dig)


def main():
	parser = argparse.ArgumentParser(description="Get the hash of any file")
	choices = {}
	for algo in hl.algorithms_guaranteed:
		choices[algo] = getattr(hl, algo)
	parser.add_argument("algorithm", type=str, help="The algorithm to use to compute the hash", choices=choices)
	parser.add_argument("file", metavar="file", type=str)
	args = parser.parse_args()
	algo = choices[args.algorithm]
	
	computeHash(args.file, algo)
