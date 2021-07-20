#!/usr/bin/env python3

""" --__--------------------------------------------------------------------
 ____/ _|
|_  / |_   
 / /|  _|  editor   : F. Zicklam <git@zicklam.com>
/___|_|    last edit: 2021-07-20
----------------------------------------------------------------------------
 Simple way to use something similar to switch/case in python to call functions
 Python support switch/case above 3.9
"""

def switch(x):
  try:
    return {
      'create': lambda x: create_mehtod(),
      'delete': lambda x: delete_mehtod(),
    }[x](x)
  except KeyError:
    print(f"func '{x}' does not exist!")

# -------------------------------------------------------------------------
def create_mehtod():
  print("i can create things!")
  
def delete_mehtod():
  print("i destroya!")

# -- example usage --------------------------------------------------------  
switch('not_existent')
switch('create')
switch('delete')

# vim: set ts=4 sw=4 sts=4 tw=0 et :
