from curtsies import Input
import sys


class player1:
    def __init__(self):
        self.sets = 0
        self.score = 0
        self.side = "left"

class player2:
    def __init__(self):
        self.sets = 0
        self.score = 0
        self.side = "right"

p1 = player1()
p2 = player2()
third_change = True

def set_zero_scores():
    global p1
    global p2
    p1.score = 0
    p2.score = 0

def court_change():
    global p1
    global p2
    place = p1.side
    p1.side = p2.side
    p2.side = place
    print("Change courts")
    print("player1 " + p1.side +","+"player2 " +p2.side)

def midgame_change():
    if p1.sets + p2.sets == 1:
        court_change()

def check_global_winner():
    if p1.sets == 2:
        print("PLAYER 1 WINS THE MATCH")
        sys.exit()
    if p2.sets == 2:
        print("PLAYER 1 WINS THE MATCH")
        sys.exit()

def scorechecks():
    global p1
    global p2
    global third_change
    if p1.score == 29 and p2.score == 30:
        p2.sets += 1
        check_global_winner()
        print("p2 wins set")
        print("p1 sets: {} p2 sets: {}".format(p1.sets, p2.sets))
        set_zero_scores()
        midgame_change()
        return
    if p1.score == 30 and p2.score == 29:
        p1.sets +=1
        check_global_winner()
        print("p1 wins set")
        print("p1 sets: {} p2 sets: {}".format(p1.sets, p2.sets))
        set_zero_scores()
        midgame_change()
        return
    if p1.score >= 20 and p2.score >= 20:
        if p1.score - p2.score == 2:
            p1.sets +=1
            check_global_winner()
            print("p1 wins set")
            print("p1 sets: {} p2 sets: {}".format(p1.sets, p2.sets))
            set_zero_scores()
            midgame_change()
            return
        if p2.score - p1.score == 2:
            p2.sets +=1
            check_global_winner()
            print("p2 wins set")
            print("p1 sets: {} p2 sets: {}".format(p1.sets, p2.sets))
            set_zero_scores()
            midgame_change()
            return
    if p1.score == 21 and p2.score <= 19:
        p1.sets +=1
        print("p1 wins set")
        print("p1 sets: {} p2 sets: {}".format(p1.sets, p2.sets))
        set_zero_scores()
        midgame_change()
        return
    if p2.score == 21 and p1.score <= 19:
        p2.sets +=1
        check_global_winner()
        print("p2 wins set")
        print("p1 sets: {} p2 sets: {}".format(p1.sets, p2.sets))
        set_zero_scores()
        midgame_change()
        return
    if p1.sets + p2.sets == 2:
        if((p1.score == 11 and p2.score < 11)or(p2.score == 11 and p1.score < 11))and third_change:
            third_change = False
            court_change()

def main():
    global p1
    global p2
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            if e == '1':
                p1.score += 1
                print("p1 score:"+ str(p1.score) +','+'p2_score' +str(p2.score))
                scorechecks()
            if e == '2':
                p2.score += 1
                print("p1 score:"+ str(p1.score) +','+'p2_score' +str(p2.score))
                scorechecks()
                    
        

if __name__ == '__main__':
    main()