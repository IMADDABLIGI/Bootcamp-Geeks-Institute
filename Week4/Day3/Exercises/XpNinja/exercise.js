class Bird {
  constructor() {
    console.log("I'm a bird. 🦢");
  }
}

class Flamingo extends Bird {
  constructor() {
    console.log("I'm Flamingo. 🌸");
    super();
  }
}

const pet = new Flamingo();

// The first conole.log will be the child class than the parent class like every oop language
