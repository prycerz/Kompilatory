from re import search


class VarInfo:
    def __init__(self, t, o):
        self.type = t
        self.obj = o
        self.is_fun = False

class TreeNode:
    from dataclasses import dataclass



    def __init__(self, parent=None):
        self.i = 0
        self.scope = {}
        self.children = [] #lista dzieci po kolei kazde dziecko to scope
        self.parent = parent
    def reset_scope_counter(self):
        root = self.get_root()
        root._dfs_reset_i()
    def _dfs_reset_i(self):
        self.i=0
        for child in self.children:
            child._dfs_reset_i()
    def add_child(self,child):
        self.children.append(child)
    def move_in(self):
        print(self.children)
        if self.i < len(self.children):
            var= self.children[self.i]
            self.i+=1
            print(f"moving in to scope {self.i}")
            return var
        elif self.parent!=None:
            return self.parent.move_in()
        else:
            print("blad move_in")
            return None
    def move_out(self):
        print("move out {curr scope = }")
        return self.parent
    def type_search_up(self, var_name):
        return self.search_up(var_name,True)

    def value_search_up(self, var_name):
        return self.search_up(var_name,False)

    def search_up(self,var_name,type):
        if type:
            var_type = None
            if var_name not in self.scope:
                if self.parent!=None:
                    var_type = self.parent.search_up(var_name,True)
            else:
                var_type = self.scope[var_name].type
            return var_type
        else:
            val = None
            if var_name not in self.scope:
                if self.parent!=None:
                    val = self.parent.search_up(var_name,False)
            else:
                val = self.scope[var_name].obj
            return val
    def var_name_is_declared(self,var_name):
        return var_name in self.scope
    def add_type(self, name, type):
        info = VarInfo(type,None)
        self.scope[name] = info
    def add_var(self,name,obj):
        self.scope[name].obj = obj
    def var_change_up(self,name,obj):
        if name in self.scope:
            self.scope[name].obj = obj
        if self.parent!=None:
            return self.parent.var_change_up(name,obj)

    def get_root(self):
        if self.parent!=None:
            return self.get_root()
        else:
            return self


    def n_Exists_curr_scope(self,name):
        return name in self.scope

    def name_Exists_up(self, name): #just for the root
        if name in self.scope:
            return True
        if self.parent!=None:
            return self.parent.name_Exists_up(name)
        return False

