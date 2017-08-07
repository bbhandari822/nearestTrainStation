#!/usr/bin/env python
#


import philly_location_find

pos = philly_location_find.getLoc()

print "Got this position from getLoc:", pos
print "Lat:", pos[0]
print "Long:", pos[1]
