from re import search


class VarInfo:
    def __init__(self, t, o):
        self.type = t
        self.obj = o
        self.is_fun = False

class TreeNode:
    from dataclasses import dataclass



    def __init__(self, parent=None,isFun=False):
        self.i = 0
        self.scope = {}
        self.children = [] #lista dzieci po kolei kazde dziecko to scope
        self.parent = parent
        self.functions = {}
        self.isFun = isFun
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
    def type_search_up(self, var_name,jumps=0):
        return self.search_up(var_name,True,jumps)

    def value_search_up(self, var_name,jumps=0):
        return self.search_up(var_name,False,jumps)
    def obj_search_up(self, var_name,jumps=0):
        return self.search_up_obj(var_name, jumps)
    def search_up(self,var_name,type,jumps=0):
        if type:
            var_type = None
            if var_name not in self.scope:
                if self.parent!=None and not self.isFun:
                    var_type = self.parent.search_up(var_name,True,jumps)
            else:
                if (jumps == 0):
                    var_type = self.scope[var_name].type
                elif not self.isFun:
                    var_type = self.parent.search_up(var_name,True,jumps-1)
            return var_type
        else:
            val = None
            if var_name not in self.scope and not self.isFun:
                if self.parent!=None:
                    val = self.parent.search_up(var_name,False,jumps)
            else:
                if(jumps == 0):
                    val = self.scope[var_name].obj
                elif not self.isFun:
                    val = self.parent.search_up(var_name,False,jumps-1)
            return val
    def search_up_obj(self,var_name,jumps=0):
        val = None
        if var_name not in self.scope:
            if self.parent != None and not self.isFun:
                val = self.parent.search_up_obj(var_name, jumps)
        else:
            if (jumps == 0):
                val = self.scope[var_name]
            elif not self.isFun:
                val = self.parent.search_up_obj(var_name, jumps - 1)
        return val
    def var_name_is_declared(self,var_name):
        return var_name in self.scope
    def add_type(self, name, type):
        info = VarInfo(type,None)
        print(f"name {name} adding type {type}")
        self.scope[name] = info
    def add_var(self,name,obj,type = None):
        print(f"adding var {name}, val = {obj}")
        print(f"scope {self.scope}")
        if name not in self.scope:
            self.add_type(name,type)
        print(self.scope[name].type)
        self.scope[name].obj = obj
    def var_change_up(self,name,obj):
        if name in self.scope:
            self.scope[name].obj = obj
        if self.parent!=None and not self.isFun:
            return self.parent.var_change_up(name,obj)

    def end_road_up(self, name, obj,renderer):
        if name in self.scope:
            self.scope[name].obj.end(obj, renderer)
        if self.parent != None and not self.isFun:
            return self.parent.end_road_up(name, obj,renderer)
    def get_root(self):
        if self.parent!=None:
            return self.get_root()
        else:
            return self


    def n_Exists_curr_scope(self,name):
        return name in self.scope

    def name_Exists_up(self, name,jumps=0): #just for the root
        if jumps==None:
            jumps=0

        if name in self.scope:

            if jumps == 0:
                return True
            else:
                if self.parent != None and not self.isFun:
                    return self.parent.name_Exists_up(name,jumps-1)
                print("throwing false")
                return False
        if self.parent!=None and not self.isFun:
            return self.parent.name_Exists_up(name,jumps)
        return False

