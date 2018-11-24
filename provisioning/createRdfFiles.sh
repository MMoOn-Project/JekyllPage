#!/bin/sh
EXTRACT = $PWD/../provisioning/extract.py
INVENTORY = $PWD/../_data/heb_inventory.ttl
SCHEMA_FOLDER = $PWD/schema/oh/
INVENTORY_FOLDER = $PWD/inventory/oh/

$EXTRACT --file $INVENTORY --base "http://mmoon.org/lang/heb/"
echo "Convert schema TTLs to JSON+RDF"
cd $SCHEMA_FOLDER
for res in *.ttl; rapper -i turtle -o json $res > ${res%.ttl}.json 2> /dev/null ; done
echo "Convert inventory TTLs to JSON+RDF"
cd $INVENTORY_FOLDER
for res in *.ttl; rapper -i turtle -o json $res > ${res%.ttl}.json 2> /dev/null ; done
