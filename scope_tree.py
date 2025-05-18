class TreeNode:
    def __init__(self, parent):
        self.i = 0
        self.scope = {} #scope
        self.children = [] #lista dzieci po kolei kazde dziecko to scope
        self.parent = parent
    def add_child(self,child):
        self.children.append(child)
    def move_in(self):
        if self.i < len(self.children):
            self.i+=1
            return self.children[self.i]
        elif self.parent!=None:
            return self.parent.move_in()
        else:
            print("blad move_in")
            return None
    def move_out(self):
        return self.parent
    def search_up(self, var_name):
        var_type = None
        if var_name not in self.scope:
            if self.parent!=None:
                var_type = self.parent.search_up()
        else:
            var_type = self.scope[var_name]
        return var_type
    def var_name_is_declared(self,var_name):
        return var_name in self.scope



