// 1 We will get an error bcs U cant reassign a const variable

// 2 We will get an error bcs U cant reassign a const variable AGAIN :/


function funcFour() {
    window.a = "hello";
}


function funcFive() {
    alert(`inside the funcFive function ${a}`);
}

// #3.1 - run in the console:
funcFour()
funcFive()

// 4 it will work because the vaiable is being declared both in global and local scope

// 5 it will work because the vaiable is being declared both in global and local scope AGAIN :/
