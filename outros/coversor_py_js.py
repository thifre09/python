def main():
    file_path = input("Digite o caminho do arquivo:")

    with open(file_path, "r", encoding='utf-8') as f:
        file = Conversor(f.read().splitlines())
        while file.line_index < len(file.lines)-1:
            file.identify()
            with open(file_path.replace(".py",".js"),"w", encoding="utf-8") as new_file:
                new_file.write(file.new_code)    

class Conversor:

    def __init__(self, lines: list):
        self.lines: list = lines
        self.new_code: str = ""
        self.line_index = 0
        self.line: str = self.lines[self.line_index]
        self.spaces_previous = 0
        self.line_next = None
        self.lines.append("")
        self.is_class = False
        self.is_func = False
        self.has_len = None
        self.variables_list = {}
        self.is_lambda = False

    # testes gerais / general tests

    def booleans(self):
        if self.line.find("True") != -1:
            self.line = self.line.replace("True", "true")
        if self.line.find("False") != -1:
            self.line = self.line.replace("False", "false")

    def operators(self):
        operator_py = ["==", "!="]
        operator_js = ["===", "!=="]
        for index, i in enumerate(operator_py):
            if i in self.line:
                self.line = self.line.replace(i, operator_js[index])
                
    def or_and_not(self):
        list_py = [" or ", " and ", " not "]
        list_js = [" && ", " || ", "!"]
        for index, i in enumerate(list_py):
            if i in self.line:
                self.line = self.line.replace(i, list_js[index])

    def type_func(self):
        list_py = ["str(", "int(", "float(", "bool(", "str ", "int ", "float ", "bool "]
        list_js = ["String(", "Number(", "Number(", "Boolean(", "String ", "Number ", "Number ", "Boolean "]
        for index, i in enumerate(list_py):
            if i in self.line:
                self.line = self.line.replace(i, list_js[index])

    def selfs(self):
        self.line = self.line.replace("self", "this")

    def strings(self):
        if "f\'" in self.line or "f\"" in self.line:
            self.line = self.line.replace("f\"", "\"").replace("f\'", "\'").replace("\"","`").replace("\'", "`").replace("{","${")

    def nones(self):
        self.line = self.line.replace("None", "null")

    def lambdas(self):
        if "lambda " in self.line:
            self.line = self.line.replace("lambda ", "(").replace(":", ") => {return")
            self.line += "}"
            self.is_lambda = True

    def coments(self):
        while True:
            if "#" in self.line:
                try:
                    if not "#" in self.line.split("\"")[1]:
                        self.line = self.line.replace("#", "//")
                        break
                except:
                    self.line = self.line.replace("#", "//")
                    break
                
                try:
                    if not "#" in self.line.split("\'")[1]:
                        self.line = self.line.replace("#", "//")
                        break
                except:
                    self.line = self.line.replace("#", "//")
                    break
            break

    def is_(self):
        self.line = self.line.replace(" is ", " === ").replace(" is not ", " !== ")

    def pass_(self):
        if self.line.strip().startswith("pass "):
            self.line = self.line.replace("pass ", "")

    # blocos de código / blocks of code

    def variables(self):
        self.tests()
        blocks = self.count_space()
        temp = self.line.lstrip()
        if self.is_class and not self.is_func:
            var = temp.split(maxsplit=1)[0].split("[")[0]
            self.new_code += (blocks*4)*" " + "static " + temp + "\n" if var not in self.variables_list and not self.is_lambda else (blocks*4)*" " + temp + "\n"
            self.variables_list[var] = self.count_space()

        elif self.is_func:
            var = temp.split(maxsplit=1)[0].split("[")[0]
            if temp.startswith("this."):
                (blocks*4)*" " + temp + "\n"
            else:
                self.new_code += (blocks*4)*" " + "let " + temp + "\n" if var not in self.variables_list and not self.is_lambda else (blocks*4)*" " + temp + "\n"
            self.variables_list[var] = self.last_def

        else:
            var = temp.split(maxsplit=1)[0].split("[")[0]
            self.new_code += (blocks*4)*" " + "let " + temp + "\n" if var not in self.variables_list and not self.is_lambda else (blocks*4)*" " + temp + "\n"
            self.variables_list[var] = -1

        self.next_line()

    def func(self):
        self.is_func = True
        self.last_def = self.count_space()
        self.tests()       
        if not self.is_class:
            temp = self.line.replace("def", "function", 1).replace(":", " {")
        else:
            blocks = self.count_space()
            temp = self.line.replace("def", "", 1).replace(":", " {").lstrip().replace("this","").replace(",", "", 1)
            if "__init__" in temp:
                temp = temp.replace("__init__", "constructor")
            temp = (blocks*4)*" " + temp
        var = self.line.replace("def", "").replace(":", "").replace(")", "").split("(")[-1]
        var = var.replace("this", "").replace(",", "", 1) if self.is_class else var
        self.variables_list[var] = self.count_space()
        self.new_code += temp + "\n"
        self.next_line()

    def ifs(self, tipo):
        self.tests()
        if tipo == 1:     
            blocks = self.count_space()
            temp = self.line.replace(":", ") {").replace("if", "", 1).lstrip()
            temp = "(" + temp
            temp = "if " + temp
            temp = (blocks*4)*" " + temp
            self.new_code += temp + "\n"
            self.next_line()
        elif tipo == 2:
            blocks = self.count_space()
            temp = self.line.replace(":", ") {").replace("elif", "", 1).lstrip()
            temp = "(" + temp
            temp = "else if " + temp
            temp = (blocks*4)*" " + temp
            self.new_code += temp + "\n"
            self.next_line()
        elif tipo == 3:
            temp = self.line.replace(":", " {")
            self.new_code += temp + "\n"
            self.next_line()

    def whiles(self):
        blocks = self.count_space()
        self.tests()
        temp = self.line.replace(":", ") {").replace("while", "", 1).lstrip()
        temp = "(" + temp
        temp = "while " + temp
        temp = (blocks*4)*" " + temp
        self.new_code += temp + "\n"
        self.next_line()

    def fors(self):
        blocks = self.count_space()
        self.tests()
        temp = self.line
        if "range" in temp:
            v1 = str(temp.replace("for", "").lstrip().split(maxsplit=1)[0])
            v2 = (temp.rstrip(":").split()[-1]).replace("range(", "").replace("range (", "").removesuffix(")").split(",")
            if len(v2) == 1:
                temp = f"for (let {v1} = 0;{v1} < {v2[0]};{v1}++) " + "{"
            elif len(v2) == 2:
                temp = f"for (let {v1} = {v2[0]};{v1} < {v2[1]};{v1}++) " + "{"
            elif len(v2) == 3:
                temp = f"for (let {v1} = {v2[0]};{v1} < {v2[1]};{v1} += {v2[2]}) " + "{"
            
        elif "enumerate" in temp:
            v1 = temp.replace("for", "").lstrip()[:temp.find(" in ")-4]
            v2 = temp.replace(")", "").replace(":", "")[temp.find("(")+1:]
            temp = f"for (const [{v1}] of {v2}.entries()) " + "{"
        else:
            v1 = str(temp.replace("for", "").lstrip().split(maxsplit=1)[0])
            v2 = str(temp.replace("for", "").lstrip().replace(":", "").split()[-1])
            temp = f"for (let {v1} in {v2}) " + "{"

        var = self.line.split()[1].split(",") if not ("enumerate" in temp) else v2.split(",")
        for v in var:
            v.lstrip()
            self.variables_list[v] = self.count_space()
        temp = (blocks*4)*" " + temp
        self.new_code += temp + "\n"
        self.next_line()

    def classes(self):
        self.is_class = True
        if len(self.line.replace("class", "", 1).replace(":", "").strip(" ()").split()) == 1:  
            temp = self.line.replace(":", " {").replace("()", "")
        else:
            temp = self.line.replace("(", " extends ").replace(":", " {").replace(")", "")
        self.new_code += temp + "\n"
        self.next_line()

    def trys(self):
        temp = self.line.replace(":", " {")
        self.new_code += temp + "\n"
        self.next_line()

    def excepts(self):
        temp = "catch(error) {"
        self.new_code += temp + "\n"
        self.next_line()

    def finallys(self):
        temp = self.line.replace(":", " {")
        self.new_code += temp + "\n"
        self.next_line()

    # funções e métodos/ functions and methods

    def prints(self):
        self.line = self.line.replace("print", "console.log", 1)

    def inputs(self):
        self.line = self.line.replace("input", "window.prompt")

    def lens(self):
        if ("len(" in self.line or "len (" in self.line) and self.has_len is None:
            self.has_len = -1
            len_func = """function len(x) {
    return x.length()
}
"""
            self.new_code = len_func + self.new_code

    def appends(self):
        self.line = self.line.replace(".append", ".push")
    
    def removes(self):
        self.line = self.line.replace(".remove", ".splice")

    def indexs(self):
        self.line = self.line.replace(".index", ".indexOf")
    # métodos principais / main methods

    def next_line(self):
        self.spaces_previous = self.count_space()
        self.line_index += 1
        if self.line_index <= len(self.lines):
            self.line = self.lines[self.line_index]

        while self.line.strip() == "" and self.line_index < len(self.lines):
            self.line_index += 1

            if self.line_index < len(self.lines):
                self.line_next: str = self.lines[self.line_index]
                i = 0
                while self.line_next.strip() == "" and self.line_index+i < len(self.lines):
                    self.line_next = self.lines[self.line_index+i]
                    i += 1
                self.spaces_next = self.count_space(self.line_next)
                if self.spaces_next < self.spaces_previous and (self.spaces_previous - self.spaces_next) == 1:
                    blocks = self.spaces_next
                    self.new_code += (blocks*4)*" " + "}\n"
                    self.spaces_previous = self.spaces_next
                elif self.spaces_next < self.spaces_previous:
                    while self.spaces_previous - self.spaces_next != 1:
                        self.spaces_previous -= 1
                        blocks = self.spaces_previous
                        self.new_code += (blocks*4)*" " + "}\n"
                    blocks = self.spaces_next
                    self.new_code += (blocks*4)*" " + "}\n"
                    self.spaces_previous = self.spaces_next

            self.new_code += "\n"
            if self.line_index < len(self.lines):
                self.line = self.lines[self.line_index]

        if self.count_space() == 0:
            self.is_class = False
            self.is_func = False

        if self.spaces_previous > self.count_space() and (self.spaces_previous - self.count_space()) == 1:
            blocks = self.count_space()
            self.new_code += (blocks*4)*" " + "}\n"
        elif self.spaces_previous > self.count_space():
            while self.spaces_previous - self.count_space() != 1:
                self.spaces_previous -= 1
                blocks = self.spaces_previous
                self.new_code += (blocks*4)*" " + "}\n"
            blocks = self.count_space()
            self.new_code += (blocks*4)*" " + "}\n"

        a = list(self.variables_list.keys())
        for g in a:
            if self.variables_list[g] >= self.count_space():
                del self.variables_list[g]

        self.is_lambda = False
 
    def count_space(self, l=None):
        if l is None:
            l = self.line
        total = 0
        n1 = 0
        n2 = 4
        first4 = l[n1:n2]
        while first4 == "    ":
            total += 1
            n1 += 4
            n2 += 4
            first4 = l[n1:n2]
        
        return total
    
    def identify(self):
        a = self.line.lstrip()
    
        if a.startswith("def "):
            self.func()
        elif a.startswith("if "):
            self.ifs(1)
        elif a.startswith("elif "):
            self.ifs(2)
        elif a.startswith("else:"):
            self.ifs(3)
        elif a.startswith("while "):
            self.whiles()
        elif a.startswith("for "):
            self.fors()
        elif a.startswith("class "):
            self.classes()
        elif a.startswith("try:"):
            self.trys()
        elif a.startswith("except ") or a.startswith("except:") or a.startswith("except(") or a.startswith("except ("):
            self.excepts()
        elif a.startswith("finally"):
            self.finallys()
        elif a.find("=") != -1:
            self.variables()
        else:
            blocks = self.count_space()
            self.tests()
            temp = self.line.lstrip()
            self.new_code += (blocks*4)*" " + temp + "\n"
            self.next_line()

    def tests(self, callbacks=None):
        if callbacks is None:
            callbacks = [self.prints, self.inputs, self.lens, self.appends, self.removes, self.indexs,
                         self.booleans, self.operators, self.or_and_not, self.type_func, self.selfs, 
                         self.strings, self.nones, self.lambdas, self.coments, self.is_]
            
        for callback in callbacks:
            if callable(callback):
                callback()
            
if __name__ == "__main__":
    main()