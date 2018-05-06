#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 #####  #         ###
#     # #          #
#       #          #
#       #          #
#       #          #
#     # #          #
 #####  #######   ### Runner

"""

from docstring2md import main


if __name__ == '__main__':

    import time
    start_time = time.time()
    main.run()
    print("--- %s seconds ---" % (time.time() - start_time))
