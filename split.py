#!/usr/bin/env python
"""This program takes an input file and separates it into input, training, development, and test sets."""


import argparse
from typing import Iterator, List
from math import floor
import random

#Generator
def read_tags(path: str) -> Iterator[List[List[str]]]:
    with open(path, "r") as source:
        lines = []
        for line in source:
            line = line.rstrip()
            if line:  # Line is contentful.
                lines.append(line.split())
            else:  # Line is blank.
                yield lines.copy()
                lines.clear()
    # Just in case someone forgets to put a blank line at the end...
    if lines:
        yield lines

#Write-to-filer
def write_to_file(filename: str, lines: list):
	myfile = open(filename,"w+")
	for sentence in lines[0:10]:
		for word in sentence:
			myfile.write(word[0] + " " + word[1] + " " + word[2] + " \n")
		myfile.write("\n")
	myfile.close()


def main(args: argparse.Namespace) -> None:

	args = vars(parser.parse_args())	#converts Namespace object into a dictionary
	myinput = args["input"]
	train = args["train"]
	dev = args["dev"]
	test = args["test"]
	seed = args["seed"]
	assert(seed), "You must add a seed."

	corpus = list(read_tags(myinput))
	random.seed(a=seed)
	random.shuffle(corpus)
	numsents = len(corpus)
	numtrain = floor(.8 * numsents)		#rounds number DOWN to the nearest integer
	numdev = floor(.9 * numsents)

	write_to_file(train, corpus[0:numtrain])
	write_to_file(dev, corpus[numtrain:numdev])
	write_to_file(test, corpus[numdev:numsents])


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--seed')
    parser.add_argument("input")
    parser.add_argument("train")
    parser.add_argument("dev")
    parser.add_argument("test")
    namespace = parser.parse_args()
    

    main(namespace)