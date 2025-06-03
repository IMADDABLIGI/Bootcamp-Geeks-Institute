// someOne = {
//     name: '',
//     height: '',
//     gender: '',
//     birth: '',
//     homeWorld: ''
// }

// const fetchSomone = () => {
//     fetch(`https://www.swapi.tech/api/people/1`)
//     .then((response)=>{
    //     })
    //     .then((resData)=>{
        //         return  response.json()
//         console.log(resData.result.properties)
//         return(resData.result.properties);
//     })
//     .catch((err)=>console.log(err.message))
// } 


const div = document.querySelector('div');

const fetchSomone = async (randomNum) => {
    try {
        const response = await fetch(`https://www.swapi.tech/api/people/${randomNum}`);
        if (response.ok){
            const responseData = await response.json();
            console.log(responseData)
            return (responseData.result.properties)
        }
    } catch (err) {
        console.error(err)
    }
}

const findSomeone = async () => {
    div.innerHTML = `
        <div class="fa-3x">
            <i class="fa-solid fa-circle-notch fa-spin"></i>
        </div>
    `
    const randomNum = Math.floor(Math.random() * 9) + 1;
    const someone = await fetchSomone(randomNum);
    console.log(someone)
    if (someone){
        div.innerHTML = `
        <h3> ${someone.name} </h3>
        <h3> Height: ${someone.height} </h3>
        <h3> Gender: ${someone.gender} </h3>
        <h3> Birth Year: ${someone.birth_year} </h3>
        <h3> Home World: ${someone.skin_color} </h3>
        `
    }
    else
        div.innerHTML = `<h3> No data </h3>`
    
}

