const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'reindeer'
}


let str = '';
for (x in details)
    str += `${x} ${details[x]} `

console.log(str)