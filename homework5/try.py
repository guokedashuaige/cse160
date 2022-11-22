import networkx as nx
import matplotlib.pyplot as plt

rj = nx.Graph()

names={"Nurse","Juliet","Romeo","Friar Laurence","Capulet","Tybalt","Benvolio","Montague","Escalus","Paris", "Mercutio"}
for name in names:
    rj.add_node(name)

relations1={}
relations={("Nurse","Juliet"),("Juliet","Capulet"),("Tybalt","Juliet"),("Capulet","Tybalt"),
("Juliet","Friar Laurence"),("Romeo","Juliet"),("Romeo","Friar Laurence"),
("Romeo","Benvolio"),("Romeo","Montague"),("Romeo","Mercutio"),
("Benvolio","Montague"),
("Capulet","Escalus"),("Capulet","Paris"),
("Escalus","Montague"),("Escalus","Paris"),("Escalus","Mercutio"),("Mercutio","Paris")}
for relation in relations:
    #print(relation)
    rj.add_edge(*relation)


def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))

#print(friends(rj,"Benvolio"))

def friends_of_friends(graph, user):
    #fof means friends if friends
    fof=set()
    f=friends(graph,user)
    for x in f:
       fof=fof | friends(rj,x)
    return fof-{user}-f

#print(friends_of_friends(rj,"Benvolio"))

def common_friends(graph, user1, user2):
    return friends(graph,user1)&friends(graph,user2)

#print(common_friends(rj,"Escalus","Mercutio"))


def num_common_friends_map(graph, user):
    dic={}
    for x in list(graph.nodes):
       # print(common_friends(graph,user,x))
        dic[x]=len(common_friends(graph,user,x))
    # delete for user and user's friends
    del dic[user]
    for i in friends(graph,user):
        del dic[i]
    #delete zero key
    list1=[]
    list2=[]
    for k,v in dic.items():
        if v !=0:
            list1.append(k)
            list2.append(v)
    dic = dict(zip(list1,list2))
    return dic
    

print(num_common_friends_map(rj,"Nurse"))
#nx.draw_networkx(rj)
#plt.show()