from routines import hs
import argparse
import hashlib as hl

def main():
	parser = argparse.ArgumentParser(description="Get the hash of any file")
	choices = {}
	for algo in hl.algorithms_guaranteed:
		choices[algo] = getattr(hl, algo)
	parser.add_argument("algorithm", type=str, help="The algorithm to use to compute the hash", choices=choices)
	parser.add_argument("file", metavar="file", type=str)
	args = parser.parse_args()
	algo = choices[args.algorithm]
	
	hs.computeHash(args.file, algo)
	