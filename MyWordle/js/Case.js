class Case {
    constructor(col, row)
    {
        this.col = col
        this.row = row
        this.content = " "
        this.type = "text"
    }

    setContent(content)
    {
        this.content = content
    }

    setType(type)
    {
        this.type = type
    }

    display()
    {
        return '<div class="case ' + this.type + '">' + this.content + '</div>'
    }

}