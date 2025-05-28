class Parent{
    constructor(lastName){
        this.lastName = lastName;
    }

    callParent(){
        console.log("This is from Parent");
    }
}

class Child extends Parent{
    constructor(firstName, lastName){
        super(lastName);
        this.firstName = firstName;
    }
    
    callChild(){
        console.log("This is from Child");
    }

}

const child = new Child("Hmed", "Dokali");

child.callParent()
child.callChild()