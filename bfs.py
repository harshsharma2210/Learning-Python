from puzzle import Puzzle;
import copy;

closed_list=[]
open_stack=[]

def checkClosedList(positions):
    if positions in closed_list:
        return False
    return True



def breadthFirstSearch(state):
    print("Initial State => ")
    state.displayState()

    open_stack.append(state)
    
    while len(open_stack) != 0 :
        node = open_stack.pop(0)
        closed_list.append(node.positions)


        if node.isGoalState():
            node.displayState()
            print("Closed List Length => ", len(closed_list))
            print("Open List Length => ", len(open_stack))
            break


        new_state_up = copy.deepcopy(node)
        if new_state_up.up() and  checkClosedList(new_state_up.positions) :
            open_stack.append(new_state_up)
        else:
            del new_state_up


        new_state_left = copy.deepcopy(node)
        if new_state_left.left() and   checkClosedList(new_state_left.positions) :
            open_stack.append(new_state_left)
        else:
            del new_state_left


        new_state_down = copy.deepcopy(node)
        if new_state_down.down() and  checkClosedList(new_state_down.positions) :
            open_stack.append(new_state_down)
        else:
            del new_state_down

     
        new_state_right = copy.deepcopy(node)
        if new_state_right.right() and  checkClosedList(new_state_right.positions) :
            open_stack.append(new_state_right)
        else:
            del new_state_right

puzzle = Puzzle([2,0,3,1,8,4,7,6,5],[1,2,3,8,0,4,7,6,5])
depthFirstSearch(puzzle)
