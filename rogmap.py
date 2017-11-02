# -*- coding: utf-8 -*-
class rogmap:
    maplist = []
   # @staticmethod
    def init(self):
       # global maplist
        self.maplist.append(["-","-","-","-","-","-","#","-","-","-"])
        self.maplist.append(["-","-","-","-","-","-","#","-","-","-"])
        self.maplist.append(["-","-","-","-","-","-","-","-","-","-"])
        self.maplist.append(["-","-","#","#","#","#","#","-","-","-"])
        self.maplist.append(["-","-","-","-","-","-","#","-","-","-"])
        self.maplist.append(["-","-","-","-","-","-","#","-","-","-"])
        self.maplist.append(["-","-","-","-","-","-","-","-","-","-"])
        self.maplist.append(["-","-","-","-","-","-","-","-","-","-"])
        self.maplist.append(["-","-","-","-","-","-","-","-","-","-"])
        self.maplist.append(["-","-","-","-","-","-","-","-","-","-"])

   # @staticmethod
    def getmaplist(self):
     #   global maplist
     return(self.maplist)
