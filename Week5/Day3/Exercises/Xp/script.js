const characterInfo = document.querySelector('div');

const fetchHomeworld = async (url) => {
    try {
        const response = await fetch(url);
        if (response.ok) {
            const data = await response.json();
            return data.result.properties.name;
        }
    } catch (err) {
        console.error('Error fetching homeworld:', err);
        return 'Unknown';
    }
}

const fetchCharacter = async (characterId) => {
    try {
        const response = await fetch(`https://www.swapi.tech/api/people/${characterId}`);
        if (!response.ok) {
            throw new Error('Character not found');
        }
        const data = await response.json();
        const character = data.result.properties;
        
        const homeworldName = await fetchHomeworld(character.homeworld);
        
        return {
            name: character.name,
            height: character.height,
            gender: character.gender,
            birthYear: character.birth_year,
            homeworld: homeworldName
        };
    } catch (err) {
        console.error('Error fetching character:', err);
        return null;
    }
}

const findSomeone = async () => {
    characterInfo.innerHTML = `
        <div class="fa-3x">
            <i class="fa-solid fa-circle-notch fa-spin"></i>
        </div>
    `;
    
    try {
        const randomNum = Math.floor(Math.random() * 83) + 1;
        const character = await fetchCharacter(randomNum);
        
        if (character) {
            characterInfo.innerHTML = `
                <h3>${character.name}</h3>
                <h3>Height: ${character.height} cm</h3>
                <h3>Gender: ${character.gender}</h3>
                <h3>Birth Year: ${character.birthYear}</h3>
                <h3>Home World: ${character.homeworld}</h3>
            `;
        } else {
            characterInfo.innerHTML = `
                <h3>Error loading character data</h3>
                <i class="fas fa-exclamation-triangle"></i>
            `;
        }
    } catch (err) {
        characterInfo.innerHTML = `
            <h3>Error loading character data</h3>
            <i class="fas fa-exclamation-triangle"></i>
        `;
        console.error('Error:', err);
    }
}