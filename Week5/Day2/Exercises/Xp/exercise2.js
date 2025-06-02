// fetch("https://api.giphy.com/v1/gifs/search?q=sun&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My")
fetch("https://api.giphy.com/v1/gifs/search?q=sun&limit=10&offset=2&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My")
    .then((response)=>{
        // throw new Error("Error here")
        return response.json();
    })
    .then((obj) => console.log(obj))
    .catch((error)=>console.error(error.message));