"""
Searching a path algorithm. yep, it is ugly for now
"""
class search_way:
    depth_maplist = []
    path =[]
    def add_depth(self, x, y, i):
        max_x, max_y = 10, 10
        if x > -1 and y > -1 and x < max_x and y < max_y  \
        and self.depth_maplist[y][x] == "-":
            self.depth_maplist[y][x] = str(i)
    def track_it_down(self, x, y):
        current_x = x
        current_y = y

        i = int(self.depth_maplist[y][x])
        while i > 0:
            self.path.append([current_x, current_y])
            i=i-1
            if current_x > -1 and  current_y > -1 and current_x + 1 < 10 \
            and current_y < 10 and self.depth_maplist[current_y][current_x + 1\
                                                      ] == str(i):
                current_x =current_x + 1
            elif current_x - 1> -1 and  current_y > -1 and current_x < 10 \
            and current_y < 10 and self.depth_maplist[current_y][current_x - 1\
                                                      ] == str(i):
                current_x =current_x - 1
            elif current_x > -1 and  current_y > -1 and current_x < 10 \
            and current_y+1 < 10 and self.depth_maplist[current_y+1][current_x\
                                                        ] == str(i):
                current_y =current_y+1
            elif current_x > -1 and  current_y -1 > -1 and current_x < 10 \
            and current_y < 10 and self.depth_maplist[current_y-1][current_x\
                                                      ] == str(i):
                current_y=current_y-1
            elif current_x > -1 and  current_y > -1 and current_x + 1 < 10 \
            and current_y+1 < 10 and self.depth_maplist[current_y+1][current_x + 1\
                                                      ] == str(i):
                current_x+=1
                current_y+=1
            elif current_x-1 > -1 and  current_y-1 > -1 and current_x < 10 \
            and current_y < 10 and self.depth_maplist[current_y-1][current_x - 1\
                                                      ] == str(i):
                current_x-=1
                current_y-=1
            elif current_x -1 > -1 and  current_y > -1 and current_x < 10 \
            and current_y+1 < 10 and self.depth_maplist[current_y+1][current_x-1\
                                                      ] == str(i):
                current_x-=1
                current_y+=1
            elif current_x  > -1 and  current_y-1 > -1 and current_x+1 < 10 \
            and current_y < 10 and self.depth_maplist[current_y-1][current_x+1\
                                                      ] == str(i):
                current_x+=1
                current_y-=1
        self.path.reverse()

    def wave(self, x1, y1, x2, y2, maplist):
        self.path.clear()
        self.depth_maplist = list(maplist[:])
        i = 1
        self.depth_maplist[y1][x1] = "0"
        self.add_depth(x1 + 1, y1, 1)
        self.add_depth(x1, y1 + 1, 1)
        self.add_depth(x1, y1, 1)
        self.add_depth(x1-1, y1, 1)
        self.add_depth(x1 + 1, y1 +1, 1)
        self.add_depth(x1, y1 -1, 1)
        self.add_depth(x1 - 1, y1 - 1, 1)
        self.add_depth(x1 + 1, y1 - 1, 1)
        self.add_depth(x1 - 1, y1 + 1, 1)

        for iii in range(0,9):
            ix=0
            for ix in range(0,9):
                iy=0
                for iy in range(0,9):
                    if self.depth_maplist[iy][ix] == str(i):
                        ii = i + 1
                        self.add_depth(ix+1, iy, ii)
                        self.add_depth(ix+1, iy+1, ii)
                        self.add_depth(ix, iy+1, ii)
                        self.add_depth(ix-1, iy, ii)
                        self.add_depth(ix-1, iy-1, ii)
                        self.add_depth(ix, iy-1, ii)
                        self.add_depth(ix+1, iy-1, ii)
                        self.add_depth(ix-1, iy+1, ii)
            i=i+1
        self.track_it_down(x2,y2)
