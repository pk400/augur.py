#! /usr/bin/env python

import asyncio

from augur import AugurPy

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  augur = AugurPy()
  loop.run_until_complete(augur.open_connection())
  loop.run_until_complete(
    augur.get_categories(
      universe='0x02149d40d255fceac54a3ee3899807b0539bad60'))
  
