export class Program {

    constructor(time: string, name: string, description: string, hidden: boolean) {
        this.time = time
        this.name = name
        this.description = description
        this.hidden = hidden
    }

    time: string = ''
    name: string = ''
    description: string = ''
    hidden: boolean = false

}
