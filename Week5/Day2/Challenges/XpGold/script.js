const form = document.getElementById('sunriseForm');
        const loadingDiv = document.getElementById('loading');
        const errorDiv = document.getElementById('error');
        const resultsDiv = document.getElementById('results');
        
        // Function to fetch sunrise data for a given location
        async function fetchSunriseData(lat, lng) {
            const url = `https://api.sunrise-sunset.org/json?lat=${lat}&lng=${lng}&formatted=0`;
            const response = await fetch(url);
            const data = await response.json();
            
            if (data.status !== 'OK') {
                throw new Error('Failed to fetch sunrise data');
            }
            
            return {
                lat,
                lng,
                sunrise: data.results.sunrise
            };
        }
        
        // Function to format UTC time to local time string
        function formatSunriseTime(utcTimeString) {
            const date = new Date(utcTimeString);
            return date.toLocaleTimeString([], { 
                hour: '2-digit', 
                minute: '2-digit',
                timeZoneName: 'short'
            });
        }
        
        // Function to get city name from coordinates (simplified)
        function getCityName(lat, lng) {
            // For Paris coordinates
            if (Math.abs(lat - 48.864716) < 0.1 && Math.abs(lng - 2.349014) < 0.1) {
                return 'Paris, France';
            }
            // For New York coordinates
            if (Math.abs(lat - 40.730610) < 0.1 && Math.abs(lng + 73.935242) < 0.1) {
                return 'New York, USA';
            }
            // Generic format for other coordinates
            return `Location (${lat.toFixed(4)}, ${lng.toFixed(4)})`;
        }
        
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            // Get input values
            const lat1 = parseFloat(document.getElementById('lat1').value);
            const lng1 = parseFloat(document.getElementById('lng1').value);
            const lat2 = parseFloat(document.getElementById('lat2').value);
            const lng2 = parseFloat(document.getElementById('lng2').value);
            
            // Validate inputs
            if (isNaN(lat1) || isNaN(lng1) || isNaN(lat2) || isNaN(lng2)) {
                showError('Please enter valid coordinates for both cities.');
                return;
            }
            
            // Show loading state
            loadingDiv.style.display = 'block';
            errorDiv.style.display = 'none';
            resultsDiv.style.display = 'none';
            
            try {
                // Use Promise.all to wait for both API calls to complete
                const [data1, data2] = await Promise.all([
                    fetchSunriseData(lat1, lng1),
                    fetchSunriseData(lat2, lng2)
                ]);
                
                // Display results only when both promises are resolved
                displayResults(data1, data2);
                
            } catch (error) {
                showError('Error fetching sunrise data. Please check your coordinates and try again.');
                console.error('Error:', error);
            } finally {
                loadingDiv.style.display = 'none';
            }
        });
        
        function displayResults(data1, data2) {
            const result1 = document.getElementById('result1');
            const result2 = document.getElementById('result2');
            
            // Format and display first city
            result1.innerHTML = `
                <div class="city-name">${getCityName(data1.lat, data1.lng)}</div>
                <div class="sunrise-time">${formatSunriseTime(data1.sunrise)}</div>
                <div class="coordinates">Lat: ${data1.lat}, Lng: ${data1.lng}</div>
            `;
            
            // Format and display second city
            result2.innerHTML = `
                <div class="city-name">${getCityName(data2.lat, data2.lng)}</div>
                <div class="sunrise-time">${formatSunriseTime(data2.sunrise)}</div>
                <div class="coordinates">Lat: ${data2.lat}, Lng: ${data2.lng}</div>
            `;
            
            resultsDiv.style.display = 'block';
        }
        
        function showError(message) {
            errorDiv.textContent = message;
            errorDiv.style.display = 'block';
            resultsDiv.style.display = 'none';
        }