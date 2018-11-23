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

for sub in graph.subjects():
    if not sub.startswith(args.base):
        print("skip")
        continue
    destTtl = sub.replace(str(args.base), "", 1) + ".ttl"
    destJson = sub.replace(str(args.base), "", 1) + ".json"
    print("{} write to {}".format(sub, destTtl))
    resGraph = rdflib.Graph()
    resGraph += graph.triples( (sub, None, None) )
    if not os.path.exists(os.path.dirname(destTtl)):
        os.makedirs(os.path.dirname(destTtl))
    try:
        resGraph.serialize(destTtl, format='turtle')
        systemCall = "rapper -i turtle -o json '{}'".format(destTtl)
        print(systemCall)
        exec(systemCall)
    except Exception as e:
        print(e)


print(resGraph.serialize(format='turtle'))
