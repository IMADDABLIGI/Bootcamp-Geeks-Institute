const users = { user1: 18273, user2: 92833, user3: 90315 }

const arrUsers = Object.entries(users);

console.log(arrUsers)

arrUsers.forEach((user, key, arr) => {
    // arr[key][1] *= 2
    user[1] *= 2
})

console.log(arrUsers);