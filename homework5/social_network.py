# Name: ...
# CSE 160
# Homework 5

import utils  # noqa: F401, do not remove if using a Mac
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter


###
#  Problem 1a
###

def get_practice_graph():
    """Builds and returns the practice graph
    """
    practice_graph = nx.Graph()

    # practice_graph.add_node("A")
    # practice_graph.add_node("B")
    # practice_graph.add_node("C")
    # practice_graph.add_node("D")
    # practice_graph.add_node("E")
    # practice_graph.add_node("F")
    practice_graph.add_nodes_from("ABCDEF")
    practice_graph.add_edge("A","B")
    practice_graph.add_edge("A","C")
    practice_graph.add_edge("B","C")
    practice_graph.add_edge("B","D")
    practice_graph.add_edge("C","D")
    practice_graph.add_edge("C","F")
    practice_graph.add_edge("D","F")
    practice_graph.add_edge("D","E") 
    # (Your code for Problem 1a goes here.)

    return practice_graph
    


def draw_practice_graph(graph):
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(graph)
    plt.show()


###
#  Problem 1b
###

def get_romeo_and_juliet_graph():
    """Builds and returns the romeo and juliet graph
    """
    rj = nx.Graph()
    # (Your code for Problem 1b goes here.)
    names={"Nurse","Juliet","Romeo","Friar Laurence","Capulet","Tybalt","Benvolio","Montague","Escalus","Paris", "Mercutio"}
    for name in names:
        rj.add_node(name)

    #relations1={}
    relations={("Nurse","Juliet"),("Juliet","Capulet"),("Tybalt","Juliet"),("Capulet","Tybalt"),
("Juliet","Friar Laurence"),("Romeo","Juliet"),("Romeo","Friar Laurence"),
("Romeo","Benvolio"),("Romeo","Montague"),("Romeo","Mercutio"),
("Benvolio","Montague"),
("Capulet","Escalus"),("Capulet","Paris"),
("Escalus","Montague"),("Escalus","Paris"),("Escalus","Mercutio"),("Mercutio","Paris")}
    for relation in relations:
        #print(relation)
        rj.add_edge(*relation)

    return rj


def draw_rj(graph):
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(graph)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()


###
#  Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))


def friends_of_friends(graph, user):
    """Find and return the friends of friends of the given user.

    Arguments:
        graph: the graph object that contains the user and others
        user: unique identifier

    Returns: a set containing the names of all of the friends of
    friends of the user. The set should not contain the user itself
    or their immediate friends.
    """
    #fof means friends if friends
    fof=set()
    f=friends(graph,user)
    for x in f:
       fof=fof | friends(graph,x)
    return fof-{user}-f


def common_friends(graph, user1, user2):
    """
    Finds and returns the set of friends that user1
    and user2 have in common.

    Arguments:
        graph:  the graph object that contains the users
        user1: a unique identifier representing one user
        user2: a unique identifier representing another user

    Returns: a set containing the friends user1 and user2 have in common
    """
    return friends(graph,user1) & friends(graph,user2)


def num_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping a person to the number of friends
    that person has in common with the given user. The map keys are the
    people who have at least one friend in common with the given user,
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "X"
    Here is what is relevant about my_graph:
        - "X" and "Y" have two friends in common
        - "X" and "Z" have one friend in common
        - "X" and "W" have one friend in common
        - "X" and "V" have no friends in common
        - "X" is friends with "W" (but not with "Y" or "Z")
    Here is what should be returned:
      num_common_friends_map(my_graph, "X")  =>   { 'Y':2, 'Z':1 }

    Arguments:
        graph: the graph object that contains the user and others
        user: unique identifier

    Returns: a dictionary mapping each person to the number of (non-zero)
    friends they have in common with the user
    """
    dic={}
    for x in list(graph.nodes):
       # not for user and user's friends
        if x not in ({user, } | friends(graph, user)):
            lcf=len(common_friends(graph,user,x))
       #none zero value for key
            if lcf:
                dic[x]=lcf
  

    return dic


def num_map_to_sorted_list(map_with_number_vals):
    """Given a dictionary, return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.

    Arguments:
        map_with_number_vals: a dictionary whose values are numbers

    Returns: a list of keys, sorted by the values in map_with_number_vals
    """
    # lambda is easy but we cannot use lambda
    #result = sorted(map_with_number_vals.keys(), key=lambda x: (-map_with_number_vals[x], x)) 

   #create a list for itemgetter use revealed in https://courses.cs.washington.edu/courses/cse160/22au/lectures/13-sorting-22au.pdf
    f = zip(map_with_number_vals.keys(), map_with_number_vals.values())
    sorted_list_by_name = sorted(f, key=itemgetter(0),reverse=False)
    sorted_list_by_num = sorted(sorted_list_by_name, key=itemgetter(1),reverse=True)
    rst = []
    for item in sorted_list_by_num:
        rst.append(item[0])
    return rst
    


def recs_by_common_friends(graph, user):
    """
    Returns a list of friend recommendations for the user, sorted
    by number of friends in common.

    Arguments:
        graph: the graph object that contains the user and others
        user: a unique identifier

    Returns: A list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """
    return num_map_to_sorted_list(num_common_friends_map(graph, user))


###
#  Problem 3
###

def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person to their
    influence score, with respect to the given user. The map only
    contains people who have at least one friend in common with the given
    user and are neither the user nor one of the users's friends.
    See the assignment writeup for the definition of influence scores.
    """
    dic = {}
    for x in graph.nodes:
        if x not in ({user, } | friends(graph, user)):
            cf_ = common_friends(graph, x, user)
            if cf_:
                dic[x] = sum([1/graph.degree[cf] for cf in cf_])
    return dic


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    return num_map_to_sorted_list(influence_map(graph, user))


###
#  Problem 5
###

def get_facebook_graph(filename):
    """Builds and returns the facebook graph
    Arguments:
        filename: the name of the datafile
    """
    # (Your Problem 5 code goes here.)
    pass


def test_get_facebook_graph(facebook, filename):
    if (filename == "facebook-links-small.txt"):
        pass
    else:
        assert len(facebook.nodes()) == 63731
        assert len(facebook.edges()) == 817090


def main():
    practice_graph = get_practice_graph()
    # Comment out this line after you have visually verified your practice
    # graph.
    # Otherwise, the picture will pop up every time that you run your program.
    draw_practice_graph(practice_graph)

    rj = get_romeo_and_juliet_graph()
    # Comment out this line after you have visually verified your rj graph and
    # created your PDF file.
    # Otherwise, the picture will pop up every time that you run your program.
    draw_rj(rj)

    ###
    #  Problem 4
    ###

    print("Problem 4:")
    print()

    # (Your Problem 4 code goes here.)

    ###
    #  Problem 5
    ###

    # (replace this filename with "facebook-links-small.txt" for testing)
    # fb_filename = "facebook-links.txt"

    # (Make sure to call get_facebook_graph)

    # test_get_facebook_graph(fb_graph, fb_filename)

    ###
    #  Problem 6
    ###
    print()
    print("Problem 6:")
    print()

    # (Your Problem 6 code goes here.)

    ###
    #  Problem 7
    ###
    print()
    print("Problem 7:")
    print()

    # (Your Problem 7 code goes here.)

    ###
    #  Problem 8
    ###
    print()
    print("Problem 8:")
    print()

    # (Your Problem 8 code goes here.)


if __name__ == "__main__":
    main()


###
#  Collaboration
###

# ... Write your answer here, as a comment (on lines starting with "#").
