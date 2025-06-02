// fetch("https://www.swapi.tech/api/starships/9/")
//     .then(response => response.json())
//     .then(objectStarWars => console.log(objectStarWars.result));



const fetching = async () => {
    try {
        const response = await fetch("https://www.swapi.tech/api/starships/9/");
        if (response.ok){
            const resData = await response.json();
            console.log(resData.result);
        }
        else
            console.error("Error Occured");
        
    } catch (error) {
        console.error(error);
    }
    // console.log("Finally Finished");
}

fetching()