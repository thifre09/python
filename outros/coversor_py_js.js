function main() {
    let file_path = input(`Digite o caminho do arquivo:`)

}
class Conversor {

    constructor( lines) {
        this.lines = lines
        this.new_code = ``
        this.line_index = 0
        this.line = this.lines[this.line_index]
        this.spaces_previous = 0
        this.line_next = None
        this.lines.append(``)
        this.is_class = false

    }
    booleans() {
        if (this.line.find(`true`) !== -1) {
            this.line = this.line.replace(`true`, `true`)
        }
        if (this.line.find(`false`) !== -1) {
            this.line = this.line.replace(`false`, `false`)

        }
    }
    operators() {
        operator_py = [`===`, `!==`]
        operator_js = [`====`, `!====`]
        for (let index, in enumerate(operator_py)) {
            if (i in this.line) {
                this.line = this.line.replace(i, operator_js[index])

            }
        }
    }
    or_and_not() {
        list_py = [` && `, ` || `, `!`]
        list_js = [` && `, ` || `, `!`]
        for (let index, in enumerate(list_py)) {
            if (i in this.line) {
                this.line = this.line.replace(i, list_js[index])

            }
        }
    }
    type_func() {
        list_py = [`String(`, `Number(`, `Number(`, `Boolean(`]
        list_js = [`String(`, `Number(`, `Number(`, `Boolean(`]
        for (let index, in enumerate(list_py)) {
            if (i in this.line) {
                this.line = this.line.replace(i, list_js[index])

            }
        }
    }
    s() {
        this.line = this.line.replace(`this`, `this`)

    }
    strings() {
        this.line = this.line.replace(`(f\``, `(\``).replace(`\``,``)

    }
    variables() {
        this.tests()
        blocks = this.count_space()
        temp = this.line.lstrip()
        if (!this.is_class) {
            this.new_code += (blocks*4)*` ` + `let ` + temp + `\n`
        }
        else{
            this.new_code += (blocks*4)*` ` + temp + `\n`
        }
        this.next_line()

    }
    func() {
        this.tests()       
        if (!this.is_class) {
            temp = this.line.replace(`def`, `function`, 1).replace(`:`, ` `)
        }
        else{
            blocks = this.count_space()
            temp = this.line.replace(`def`, ``, 1).replace(`:`, ` `).lstrip().replace(`this`,``).replace(`,`, ``, 1)
            if (`__init__` in temp) {
                temp = temp.replace(`__init__`, `constructor`)
            }
            temp = (blocks*4)*` ` + temp
        }
        this.new_code += temp + `\n`
        this.next_line()

    }
    ifs( tipo) {
        if (tipo === 1) {
            this.tests()
            blocks = this.count_space()
            temp = this.line.replace(`:`, `) `).replace(`if`, ``, 1).lstrip()
            temp = `(` + temp
            temp = `if ` + temp
            temp = (blocks*4)*` ` + temp
            this.new_code += temp + `\n`
            this.next_line()
        }
        else if (tipo === 2) {
            this.tests()
            blocks = this.count_space()
            temp = this.line.replace(`:`, `) `).replace(`elif`, ``, 1).lstrip()
            temp = `(` + temp
            temp = `else if ` + temp
            temp = (blocks*4)*` ` + temp
            this.new_code += temp + `\n`
            this.next_line()
        }
        else if (tipo === 3) {
            this.tests()
            temp = this.line.replace(`:`, ``)
            this.new_code += temp + `\n`
            this.next_line()

        }
    }
    whiles() {
        blocks = this.count_space()
        this.tests()
        temp = this.line.replace(`:`, `) `).replace(`while`, ``, 1).lstrip()
        temp = `(` + temp
        temp = `while ` + temp
        temp = (blocks*4)*` ` + temp
        this.new_code += temp + `\n`
        this.next_line()

    }
    fors() {
        blocks = this.count_space()
        this.tests()
        temp = this.line
        if (`range` in temp) {
            v1 = String(temp.replace(`for`, ``).lstrip().split(maxsplit=1)[0])
            v2 = (temp.rstrip(`:`).split()[-1]).strip(` range()`).split(`,`)
            if (len(v2) === 1) {
                temp = f`for (let ${v1} = 0;${v1} < ${v2[0]};${v1}++) ` + ``
            }
            else if (len(v2) === 2) {
                temp = f`for (let ${v1} = ${v2[0]};${v1} < ${v2[1]};${v1}++) ` + ``
            }
            else if (len(v2) === 3) {
                temp = f`for (let ${v1} = ${v2[0]};${v1} < ${v2[1]};${v1} += ${v2[2]}) ` + ``


            }
        }
        else{
            v1 = String(temp.replace(`for`, ``).lstrip().split(maxsplit=1)[0])
            v2 = String(temp.replace(`for`, ``).lstrip().replace(`:`, ``).split()[-1])
            temp = f`for (let ${v1} in ${v2}) ` + ``

        }
        temp = (blocks*4)*` ` + temp
        this.new_code += temp + `\n`
        this.next_line()

    }
    classes() {
        this.is_class = true
        if (len(this.line.replace(`class`, ``, 1).replace(`) {`, ``).strip(` ()`).split()) === 1) {  
            temp = this.line.replace(`:`, ` `).replace(`()`, ``)
        }
        else{
            temp = this.line.replace(`(`, ` extends `).replace(`:`, ` `).replace(`)`, ``)
        }
        this.new_code += temp + `\n`
        this.next_line()

    }
    prints() {
        this.strings()
        temp = this.line.replace(`print`, `console.log`, 1)
        this.new_code += temp + `\n`
        this.next_line()

    }
    next_line() {
        this.spaces_previous = this.count_space()
        this.line_index += 1
        if (this.line_index <= len(this.lines)) {
            this.line = this.lines[this.line_index]

        }
        while (this.line.strip() === `` || this.line_index < len(this.lines)) {
            this.line_index += 1

            // # if this.line_index < len(this.lines):
            // #     this.line_next = this.line[this.line_index]
            // #     i = 0
            // #     while this.line_next.strip() === ``:
            // #         this.line_next = this.line[this.line_index+i]
            // #     this.spaces_next = this.count_space(this.line_next)

            this.new_code += `\n`
            if (this.line_index < len(this.lines)) {
                this.line = this.lines[this.line_index]

            }
        }
        if (this.count_space() === 0) {
            this.is_class = false

        }
        if (this.spaces_previous > this.count_space() || (this.spaces_previous - this.count_space()) === 1) {
            blocks = this.count_space()
            this.new_code += (blocks*4)*` ` + `}\n`
        }
        else if (this.spaces_previous > this.count_space()) {
            while (this.spaces_previous - this.count_space() !== 1) {
                this.spaces_previous -= 1
                blocks = this.spaces_previous
                this.new_code += (blocks*4)*` ` + `}\n`
            }
            blocks = this.count_space()
            this.new_code += (blocks*4)*` ` + `}\n`

        }
    }
    count_space( l=None) {
        if (l === None) {
            l = this.line
        }
        total = 0
        n1 = 0
        n2 = 4
        first4 = l
        while (first4 === `    `) {
            total += 1
            n1 += 4
            n2 += 4
            first4 = l

        }
        return total

    }
    identify() {
        a = this.line.lstrip()
        if a != -1 {
            this.prints()
        }
        else if (a.startswith(`def `)) {
            this.func()
        }
        else if (a.startswith(`if `)) {
            this.ifs(1)
        }
        else if (a.startswith(`elif `)) {
            this.ifs(2)
        }
        else if (a.startswith(`else) {`)) {
            this.ifs(3)
        }
        else if (a.startswith(`while `)) {
            this.whiles()
        }
        else if (a.startswith(`for `)) {
            this.fors()
        }
        else if (a.startswith(`class`)) {
            this.classes()
        }
        else if (a.find(` = `) !== -1) {
            this.variables()

        }
        else{
            blocks = this.count_space()
            this.tests()
            temp = this.line.lstrip()
            this.new_code += (blocks*4)*` ` + temp + `\n`
            this.next_line()

        }
    }
    tests() {
        this.booleans()
        this.operators()
        this.or_and_not()
        this.type_func()
        this.thiss()
        this.strings()


    }
}
if (__name__ === `__main__`) {
    main()

}
