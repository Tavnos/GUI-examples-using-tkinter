class CG():
    spd = {'k':{'b':[0,3,chr(9818)],'w':[7,4,chr(9812)]},
           'q':{'b':[0,4,chr(9819)],'w':[7,3,chr(9813)]},
           'b_1':{'b':[0,2,chr(9821)],'w':[7,2,chr(9815)]},
           'b_2':{'b':[0,5,chr(9821)],'w':[7,5,chr(9815)]},
           'k_1':{'b':[0,1,chr(9822)],'w':[7,1,chr(9816)]},
           'k_2':{'b':[0,6,chr(9822)],'w':[7,6,chr(9816)]},
           'r_1':{'b':[0,0,chr(9820)],'w':[7,0,chr(9814)]},
           'r_2':{'b':[0,7,chr(9820)],'w':[7,7,chr(9814)]},
           'p_1':{'b':[1,0,chr(9823)],'w':[6,0,chr(9817)]},
           'p_2':{'b':[1,1,chr(9823)],'w':[6,1,chr(9817)]},
           'p_3':{'b':[1,2,chr(9823)],'w':[6,2,chr(9817)]},
           'p_4':{'b':[1,3,chr(9823)],'w':[6,3,chr(9817)]},
           'p_5':{'b':[1,4,chr(9823)],'w':[6,4,chr(9817)]},
           'p_6':{'b':[1,5,chr(9823)],'w':[6,5,chr(9817)]},
           'p_7':{'b':[1,6,chr(9823)],'w':[6,6,chr(9817)]},
           'p_8':{'b':[1,7,chr(9823)],'w':[6,7,chr(9817)]}}
    def rps(self):
        self.pd = self.spd
    def dbb(self):
        self.cl = []
        for f in range(9):
            self.cl += [[chr(11035)]*8]
        for i in range(9):
                self.cl[i] += [chr(11035)]
        for f in range(9):
            for i in range(9):
                if ((i+1)/2)==int((i+1)/2) and ((f+1)/2)==int((f+1)/2):
                    self.cl[f][i] = chr(11036)
                elif ((i+2)/2)==int((i+2)/2) and ((f+2)/2)==int((f+2)/2):
                    self.cl[f][i] = chr(11036)
        for i in enumerate((('.A'),('  B'),(' C'),('  D'),(' E'),('  F'),(' G'),('  H.'))):
            self.cl[i[0]][8] = str(8-(i[0]))
            self.cl[8][i[0]] = str(i[1])
        self.cl[8].pop()
    def aps(self):
        for i in range(9):
            for f in range(9):
                for p in self.pd:
                    for c in self.pd[p]:
                        if self.pd[p][c][0] == f and self.pd[p][c][1] == i:
                            self.cl[f][i] = self.pd[p][c][2]
    def rb(self):
        self.cs = ''
        for i in range(9):
            self.cs = self.cs + ''.join(self.cl[i])
            self.cs = self.cs + ''.join('\n')
        print(self.cs)
ic = CG()
ic.rps()
ic.dbb()
ic.rb()
ic.aps()