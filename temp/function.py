    def click_left(x,y):
        if self.ismine :
            i,j = find_location(x,y)
            name = infer_type(i,j)
            print_mine(name,i,j)
            self.ismine = False
        if self.isrestart :
            restart()       
    def click_right(x,y):
        if self.ismine:
            i,j = find_location(x,y)
            self.Mine_Numb_now = self.Mine_Numb_now - 1;
            print_numb(self.Mine_Numb_now)
            if self.flag:
                print_mine('blank',i,j)
            else: 
                print_mine('flag',i,j)
    def find_area(x,y):
        if x in range(30,300) and y in range(150,420):
            self.ismine = True
        if x in range(140,190) and y in range(50,100):
            self.isrestart = True
    def find_location(x,y):
        xx = (x-30) // SQUARE_LENGTH
        yy = (y-150) // SQUARE_LENGTH
        return xx,yy
#    def find_neightbor(i,j):
#    def gameover():
#    def gamewin():
    def infer_type(i,j):
        if Mine[i][j] in range(1,9):
            return str(Mine[i][j])
        if Mine[i][j] == 9:
            return 
    def restart():
        new_game()
        self.isrestart = False       

    def new_game():
        new_screen()
#        Mine = new_mine()
        self.flag = False
        self.ismine = False

#    def new_mine():


