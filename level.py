import sys

class node(object):
    def __init__(self, parent = None):
        self.data = {}
        self.children = []
        self.parent=parent
    
    def _view(self, level):
        print('|___' * level, end='')
        print(self.data)
        for child in self.children:
            child._view(level+1)

class ATree(object):
    def __init__(self):
        self.root = None

    def insert(self, data = None):
        if self.root == None:
            self.root=node()
            self.root.data = {}
            return self.root
        else:
            self._insert(self.root)
    
    def _insert(self, cur_node):
        cur_node.children += [node()]
        return cur_node.children[-1]

    # here is the only place
    def view(self, level=0):
        if self.root == None:
            print("in order to print a tree there must be a tree")
            exit()
        print('|___' * level, end='')
        print(self.root)
        for child in self.root.children:
            child._view(level+1)

    def addData(self, data, position):
        if self.root == None:
            print("in order to add data to a tree there must be a tree")
            exit()
        prepped_data = add_data_prep(data)
        node = self.goto_node(self.root, position, 0)
        new_node = self._insert(node)
        new_node.data = prepped_data

    def goto_node(self, node, position, index):
        index += 1
        if check_valid_index(position, index):
            node = node.children[position[index]]
            return self.goto_node(node, position, index)
        return node
    


def new_tree(stringy):
    tree = ATree()
    node = tree.insert()
    textind = 0
    while check_valid_index(stringy, textind):
        # empty node data and empty key placeholder
        newstring = ""
        # while no new start of node or end of node
        while stringy[textind] != "{" and stringy[textind] != "}":
            newstring += stringy[textind]
            textind += 1
        finaldata = chopdata(newstring)
        if finaldata != {}:
            node.data = finaldata
        if stringy[textind] == "{":
            textind +=1
            new_node = tree._insert(cur_node = node)
            textind = parse_text(stringy, textind, new_node, tree)
        print(textind)
        if not check_valid_index(stringy, textind):
            return tree
        
def parse_text(stringy, textind, node, tree):
    # while not at end of stringy
    while check_valid_index(stringy, textind):
        # empty node data and empty key placeholder
        newstring = ""
        # while no new start of node or end of node
        while stringy[textind] != "{" and stringy[textind] != "}":
            newstring += stringy[textind]
            textind += 1
        finaldata = chopdata(newstring)
        if finaldata != {}:
            node.data = finaldata
        if stringy[textind] == "{":
            textind +=1
            new_node = tree._insert(cur_node = node)
            textind = parse_text(stringy, textind, new_node, tree)
        elif stringy[textind] == "}":
            return textind + 1
    
def chopdata(stringy):
    chopind = 0
    workable_data = {}
    key_place = ""
    data_place = ""
    while check_valid_index(stringy, chopind):
        while stringy[chopind] != '"':
            chopind +=1
            if not check_valid_index(stringy, chopind):
                return workable_data
        if key_place == "":
            chopind +=1
            while stringy[chopind] != '"':
                key_place += stringy[chopind]
                chopind += 1
            chopind +=1
        else:
            chopind +=1
            while stringy[chopind] != '"':
                data_place += stringy[chopind]
                chopind += 1
            chopind += 1
            workable_data[key_place] = data_place
            key_place =""
            data_place =""

def add_data_prep(stringy):
    chopind = 0
    workable_data = {}
    key_place = ""
    data_place = ""
    while check_valid_index(stringy, chopind):
        while stringy[chopind] != '"':
            if stringy[chopind] == "{" and key_place != "" and data_place == "":
                key_place = ""
            chopind +=1
            if not check_valid_index(stringy, chopind):
                return workable_data
        if key_place == "":
            chopind +=1
            while stringy[chopind] != '"':
                key_place += stringy[chopind]
                chopind += 1
            chopind +=1
            
        else:
            chopind +=1
            while stringy[chopind] != '"':
                data_place += stringy[chopind]
                chopind += 1
            chopind += 1
            workable_data[key_place] = data_place
            key_place =""
            data_place =""

    

# checks if index exists in collection by failing if not
def check_valid_index(ar, i):
    try:
        ar[i]
        return True
    except IndexError:
        return False

if __name__ == "__main__":
    # Again the read and isatty and input functions are C implementations 
    # and needed to both check if there's a stream
    # and to be able to read said stream
    # https://github.com/python/cpython/blob/762f93ff2efd6b7ef0177cad57939c0ab2002eac/Modules/_io/bufferedio.c#L2555
    # https://github.com/python/cpython/blob/b64c2c66e5cfe6d138b342ee58ee3b13a8d7ef16/Objects/fileobject.c#L445 
    
    ins_data='"DataC": {    "name":"One nameC"    "Level": "One",    "Priority": "High",    }'

    if sys.__stdin__.isatty() == True:
        print("please provide a stream")
    else:
        stringy = sys.__stdin__.read()
        tree = new_tree(stringy)
        tree.view()
        if check_valid_index(sys.argv, 1):
            if sys.argv[1] == "insert_test":
                tree.addData(ins_data,[0,0])
                tree.view()
