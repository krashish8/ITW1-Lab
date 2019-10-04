'''
python code using module “uuid” to generate universally unique secure randon string id of
length 8.
'''

import uuid

print(str(uuid.uuid1())[:8])