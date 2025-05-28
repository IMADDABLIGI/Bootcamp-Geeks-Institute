class Cars {
    constructor(name, mark){
        this.name = name,
        this.mark = mark
    }

    rev(){
        console.log(this.name, "is Revving it")
    }

    get details(){
        return (`${this.name} ${this.mark}`)
    }

}

const mer = new Cars("Mercedes", "A180");
mer.rev()

console.log(mer.details)