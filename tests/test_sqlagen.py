import unittest
import os
from semsql.sqlutils.sqlagen import SQLAlchemyGenerator
from linkml.utils.schemaloader import load_raw_schema

cwd = os.path.abspath(os.path.dirname(__file__))
SCHEMA_DIR = os.path.join(cwd, '../src/schema')
OUTPUT_DIR = os.path.join(cwd, 'outputs')


class SQLAlchemyGeneratorTestCase(unittest.TestCase):
    def test_gen(self):
        path = os.path.join(SCHEMA_DIR, 'rdf.yaml')
        gen = SQLAlchemyGenerator(path)
        print(gen.serialize())

