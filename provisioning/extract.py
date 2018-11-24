#!/usr/bin/env python3

import rdflib
import argparse
import os

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--endpoint', dest='endpoint')
parser.add_argument('--file', dest='file')
parser.add_argument('--base', dest='base', help="The base for generating the files")

args = parser.parse_args()
print(args.endpoint)
print(args.file)
print(args.base)

if args.endpoint:
    print("Sorry endpoint not yet supported")

if not args.file or not args.base:
    raise Exception("You need to specify a file and a base.")

graph = rdflib.Graph()
graph.parse(args.file, format="turtle")

i = 0
for sub in graph.subjects():
    i += 1
    if not sub.startswith(args.base):
        print("skip")
        continue
    destTtl = sub.replace(str(args.base), "", 1) + ".ttl"
    destJson = sub.replace(str(args.base), "", 1) + ".json"
    if i > 50:
        print("{} write to {}".format(sub, destTtl))
        i = 0
    resGraph = rdflib.Graph()
    resGraph += graph.triples( (sub, None, None) )
    if not os.path.exists(os.path.dirname(destTtl)):
        os.makedirs(os.path.dirname(destTtl))
    try:
        resGraph.serialize(destTtl, format='turtle')
    except Exception as e:
        print(e)
