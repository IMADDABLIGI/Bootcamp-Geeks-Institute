const API_KEY = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My';
const API_URL = 'https://api.giphy.com/v1/gifs/search';

const searchForm = document.getElementById('searchForm');
const searchInput = document.getElementById('searchInput');
const gifContainer = document.getElementById('gifContainer');
const deleteAllBtn = document.getElementById('deleteAllBtn');
const loadingMessage = document.getElementById('loadingMessage');
const errorMessage = document.getElementById('errorMessage');

let gifCount = 0;

// Search form submission
searchForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const searchTerm = searchInput.value.trim();
    
    if (!searchTerm) return;
    
    await fetchRandomGif(searchTerm);
});

// Delete all GIFs
deleteAllBtn.addEventListener('click', () => {
    gifContainer.innerHTML = '';
    gifCount = 0;
    updateDeleteAllButton();
    hideError();
});

// Fetch a random GIF based on search term
async function fetchRandomGif(searchTerm) {
    showLoading();
    hideError();
    
    try {
        const response = await fetch(`${API_URL}?q=${encodeURIComponent(searchTerm)}&rating=g&api_key=${API_KEY}&limit=50`);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
        if (data.data && data.data.length > 0) {
            // Select a random GIF from the results
            const randomIndex = Math.floor(Math.random() * data.data.length);
            const randomGif = data.data[randomIndex];
            
            displayGif(randomGif, searchTerm);
        } else {
            showError(`No GIFs found for "${searchTerm}". Try a different search term!`);
        }
    } catch (error) {
        console.error('Error fetching GIF:', error);
        showError('Failed to fetch GIF. Please check your internet connection and try again.');
    } finally {
        hideLoading();
    }
}

// Display a GIF with delete button
function displayGif(gifData, searchTerm) {
    const gifItem = document.createElement('div');
    gifItem.className = 'gif-item';
    gifItem.dataset.gifId = gifData.id;
    
    // Get the GIF URL from the images object
    const gifUrl = gifData.images.fixed_height.url;
    const title = gifData.title || `GIF for "${searchTerm}"`;
    
    gifItem.innerHTML = `
        <img src="${gifUrl}" alt="${title}" loading="lazy">
        <div style="margin-top: 10px;">
            <p style="font-size: 14px; margin: 5px 0; opacity: 0.8;">${title}</p>
            <button class="delete-btn" onclick="deleteGif('${gifData.id}')">
                🗑️ DELETE
            </button>
        </div>
    `;
    
    gifContainer.appendChild(gifItem);
    gifCount++;
    updateDeleteAllButton();
    
    // Clear search input
    searchInput.value = '';
}

// Delete a specific GIF
function deleteGif(gifId) {
    const gifItem = document.querySelector(`[data-gif-id="${gifId}"]`);
    if (gifItem) {
        gifItem.remove();
        gifCount--;
        updateDeleteAllButton();
    }
}

// Update delete all button visibility
function updateDeleteAllButton() {
    deleteAllBtn.style.display = gifCount > 0 ? 'block' : 'none';
}

// Show loading message
function showLoading() {
    loadingMessage.style.display = 'block';
}

// Hide loading message
function hideLoading() {
    loadingMessage.style.display = 'none';
}

// Show error message
function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
}

// Hide error message
function hideError() {
    errorMessage.style.display = 'none';
}

// Make deleteGif function globally accessible
window.deleteGif = deleteGif;