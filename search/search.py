# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    q = Directions.SOUTH
    w = Directions.WEST
    return  [q, q, w, q, w, w, q, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start'q successors:", problem.getSuccessors(problem.getStartState())
    """
    q = util.Stack() # Stack serves as fringe in DFS (Stack contains paths)
    visited = set() # necessary for search in graph (to avoid examining same state multiple times)
    startState = problem.getStartState()
    q.push([(startState, "", 0)])
    
    while not q.isEmpty():
        path = q.pop()
        node = path[-1][0] # (x, y) of the last node of current path

        if node not in visited:
            visited.add(node)
            if problem.isGoalState(node):
                return [n[1] for n in path[1:]] # list of instructions
            for successor in problem.getSuccessors(node): # add all of the non-visited successors to fringe 
                if successor[0] not in visited:
                    newPath = list(path)
                    newPath.append(successor)
                    q.push(newPath)
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    q = util.Queue() # Queue serves as fringe in BFS (Queue contains paths)
    visited = set() # necessary for search in graph (to avoid examining same state multiple times)
    startState = problem.getStartState()
    q.push([(startState, "", 0)])
    
    while not q.isEmpty():
        path = q.pop()
        node = path[-1][0] # (x, y) of the last node of current path

        if node not in visited:
            visited.add(node)
            if problem.isGoalState(node):
                return [n[1] for n in path[1:]] # list of instructions
            for successor in problem.getSuccessors(node): # add all of the non-visited successors to fringe 
                if successor[0] not in visited:
                    newPath = list(path)
                    newPath.append(successor)
                    q.push(newPath)
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    
    # cost function to calculate the priority of path while enqueueing
    def costFunction(path):
        return problem.getCostOfActions([node[1] for node in path[1:]])

    q = util.PriorityQueueWithFunction(costFunction) # PriorityQueue serves as fringe in UCS (PriorityQueue contains paths)
    visited = set() # necessary for search in graph (to avoid examining same state multiple times)
    startState = problem.getStartState()
    q.push([(startState, "", 0)])
    
    while not q.isEmpty():
        path = q.pop()
        node = path[-1][0] # (x, y) of the last node of current path

        if node not in visited:
            visited.add(node)
            if problem.isGoalState(node):
                return [n[1] for n in path[1:]] # list of instructions
            for successor in problem.getSuccessors(node): # add all of the non-visited successors to fringe 
                if successor[0] not in visited:
                    newPath = list(path)
                    newPath.append(successor)
                    q.push(newPath)
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    
    # cost function to calculate the priority of path while enqueueing
    def costFunction(path):
        currentState = path[-1][0]
        return problem.getCostOfActions([node[1] for node in path[1:]]) + heuristic(currentState, problem)

    q = util.PriorityQueueWithFunction(costFunction) # PriorityQueue serves as fringe in UCS (PriorityQueue contains paths)
    visited = set() # necessary for search in graph (to avoid examining same state multiple times)
    startState = problem.getStartState()
    q.push([(startState, "", 0)])
    
    while not q.isEmpty():
        path = q.pop()
        node = path[-1][0] # (x, y) of the last node of current path

        if node not in visited:
            visited.add(node)
            if problem.isGoalState(node):
                return [n[1] for n in path[1:]] # list of instructions
            for successor in problem.getSuccessors(node): # add all of the non-visited successors to fringe 
                if successor[0] not in visited:
                    newPath = list(path)
                    newPath.append(successor)
                    q.push(newPath)
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
