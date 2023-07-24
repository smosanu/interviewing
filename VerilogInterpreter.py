# the Verilog netlist can be stored in a tree data structure
# here is a simple tree in Python that I will use to create
# an object representing the Verilog netlist
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def add_child(self, data):
        self.children.append(TreeNode(data))
    
    def add_subtree(self, subtree):
        self.children.append(subtree)

    def print_tree(self, level=0):
        print('  ' * level + self.data)
        for child in self.children:
            child.print_tree(level + 1)

    def dfs(self):
        print(self.data)
        for child in self.children:
            child.dfs()
    
    def count(self, name):
        count = 0
        if self.data == name:
            count = 1
        for child in self.children:
            count += child.count(name)
        return count

    def count_from(self, start, name):
        if self.data == start:
            return self.count(name)
        for child in self.children:
            result = child.count_from(start, name)
            if result is not None:
                return result

def trees_index(trees, treename):
    for i, tree in enumerate(trees):
        if tree.data == treename:
            return i
    return -1

# function takes original file and removes comments, inlines split lines
def SanitizeVerilogFile(Ofilename, Mfilename):
    Ofile = open(Ofilename, 'r') # original file
    Mfile = open(Mfilename, 'w') # modified file
    Ofilelines = Ofile.readlines()
    for line in Ofilelines:
        if (not line.startswith("//")) and (line != "\n"): # eliminate comment lines, empty lines
            if line.endswith(",\n"):
                line = line.strip("\n")
            Mfile.write(line)
    Mfile.close()

# function records modules in Verilog file
def Modules(VerilogFilename):
    Modules = []
    VerilogFile = open(VerilogFilename, 'r')
    VerilogFileLines = VerilogFile.readlines()
    for line in VerilogFileLines:
        if line.startswith('module'):
            words = line.split()
            Modules.append(words[1]) # takes the string following 'module'
    return Modules

# function records instances (types) in Verilog file
def Instances(VerilogFilename):
    Instances = []
    VerilogFile = open(VerilogFilename, 'r')
    VerilogFileLines = VerilogFile.readlines()
    for line in VerilogFileLines:
        words = line.split()
        # here the condition is that the 1st word is none of the keywords nor already accounted for
        if (words[0] not in ["module", "endmodule", "input", "output", "wire"]) and (words[0] not in Instances):
            Instances.append(words[0])
    return Instances

# function determines primitives in Verilog file (instances that are not modules)
def Primitives(VerilogInstances, VerilogModules):
    Primitives = []
    for i in VerilogInstances:
        if i not in VerilogModules:
            Primitives.append(i)
    return Primitives

# function generates list of trees of modules with their instances as children
def VerilogMITrees(VerilogFilename):
    VerilogFile = open(VerilogFilename, 'r')
    VerilogFileLines = VerilogFile.readlines()
    MITrees = []

    # as in Modules and Instances, record the module and instance (type) names
    # in addition, record when a module begins and ends = lines of a module
    # record each module as a tree root and append to a list
    # add instances as children of the last module in the list
    InModule = False
    for line in VerilogFileLines:
        words = line.split()
        if words[0] == "module":
            InModule = True
            MITrees.append(TreeNode(words[1]))
        if words[0] == "endmodule":
            InModule = False
        if InModule and (words[0] not in ["module", "endmodule", "input", "output", "wire"]):
            MITrees[-1].add_child(words[0])

    return MITrees

# function generates a single tree of the verilog modules and instances
# out of the list of module-instance trees
def VerilogTree(TopTree, MITrees, VerilogPrimitives):
    for idx, child in enumerate(TopTree.children):
        if (child.data not in VerilogPrimitives) and (not child.children):
            for dbchild in MITrees[trees_index(MITrees, child.data)].children:
                TopTree.children[idx].add_child(dbchild.data)
                VerilogTree(TopTree.children[idx], MITrees, VerilogPrimitives)#.print_tree()
    return TopTree


## main flow
# remove comments, new lines, line breaks, for easy processing
# generate a clean version of the original Verilog file
SanitizeVerilogFile('TopCell.v', 'CleanTopCell.v')
# record Verilog modules
VerilogModules = Modules('CleanTopCell.v')
print("Modules:", VerilogModules)
# record Verilog instances (types)
VerilogInstances = Instances('CleanTopCell.v')
print("Instances:", VerilogInstances)
# record Verilog primitives (difference between instances and modules)
VerilogPrimitives = Primitives(VerilogInstances, VerilogModules)
print("Primitives:", VerilogPrimitives)

# create a list of modules with their instances as tree structures
MITrees = VerilogMITrees('CleanTopCell.v')
# for tree in MITrees:
#     tree.print_tree()

TopTree = MITrees[0] # hard coded it, first module has to be top module
TopTree = VerilogTree(TopTree, MITrees, VerilogPrimitives)
print("=== Verilog Tree ===")
TopTree.print_tree() # will print the complete Verilog tree

print("cellB", "nand2N1    : ", TopTree.count_from("cellB", "nand2N1")) #    nand2N1    : 1 placements
print("cellB", "nor2N1     : ", TopTree.count_from("cellB", "nor2N1")) #     nor2N1     : 2 placements
print("cellB", "invN1      : ", TopTree.count_from("cellB", "invN1")) #      invN1      : 10 placements
print("cellB", "bufferCell : ", TopTree.count_from("cellB", "bufferCell")) # bufferCell : 4 placements

print("TopCell invN1 placements:", TopTree.count("invN1"))
print("TopCell nand2N1 placements:", TopTree.count("nand2N1"))
print("TopCell cellA placements:", TopTree.count("cellA"))
print("TopCell bufferCell placements:", TopTree.count("bufferCell"))