// const APIKEY = "e2a7c3d9d3b607eb997bb83c"

// const getAllCurrencies = async () => {
//     try {
//         // const response = await fetch(`https://v6.exchangerate-api.com/v6/${APIKEY}/codes`);
//         const response = await fetch(`https://v6.exchangerate-api.com/v6/${APIKEY}/latest/USD`);
//         if (response.ok){
//             const responseData = await response.json();
//             return responseData;
//         }
//         else
//             throw new Error("Error fetching");
//     } catch (err) {
//         console.error(err)
//     }
// }

// getAllCurrencies()
//     .then((result)=>console.log(result))
//     .catch((err)=>console.error(err.message));


// const currencies = getAllCurrencies();
// console.log(currencies);

const API_KEY = "e2a7c3d9d3b607eb997bb83c"

const fromCurrencySelect = document.getElementById('fromCurrency');
const toCurrencySelect = document.getElementById('toCurrency');
const amountInput = document.getElementById('amount');
const convertBtn = document.getElementById('convertBtn');
const resultDiv = document.getElementById('result');
const loadingDiv = document.getElementById('loading');
const errorDiv = document.getElementById('error');
const resultAmount = document.getElementById('resultAmount');
const resultText = document.getElementById('resultText');
const exchangeRate = document.getElementById('exchangeRate');
const errorMessage = document.getElementById('errorMessage');

// Load available currencies on page load
document.addEventListener('DOMContentLoaded', loadCurrencies);

async function loadCurrencies() {
    try {
        showLoading(true);
        hideError();
        
        const response = await fetch(`https://v6.exchangerate-api.com/v6/${API_KEY}/codes`);
        const data = await response.json();
        
        if (data.result === 'success') {
            populateCurrencySelects(data.supported_codes);
            // Set default currencies
            fromCurrencySelect.value = 'USD';
            toCurrencySelect.value = 'EUR';
        } else {
            throw new Error(data['error-type'] || 'Failed to load currencies');
        }
    } catch (error) {
        showError('Failed to load currencies: ' + error.message);
    } finally {
        showLoading(false);
    }
}

function populateCurrencySelects(currencies) {
    // Clear existing options except the first one
    fromCurrencySelect.innerHTML = '<option value="">Select currency...</option>';
    toCurrencySelect.innerHTML = '<option value="">Select currency...</option>';
    
    // Add currency options
    currencies.forEach(([code, name]) => {
        const option1 = new Option(`${code} - ${name}`, code);
        const option2 = new Option(`${code} - ${name}`, code);
        fromCurrencySelect.add(option1);
        toCurrencySelect.add(option2);
    });
}

convertBtn.addEventListener('click', convertCurrency);

async function convertCurrency() {
    const fromCurrency = fromCurrencySelect.value;
    const toCurrency = toCurrencySelect.value;
    const amount = parseFloat(amountInput.value);

    // Validation
    if (!fromCurrency || !toCurrency) {
        showError('Please select both currencies');
        return;
    }

    if (!amount || amount <= 0) {
        showError('Please enter a valid amount');
        return;
    }

    try {
        showLoading(true);
        hideError();
        hideResult();

        const response = await fetch(`https://v6.exchangerate-api.com/v6/${API_KEY}/latest/${fromCurrency}`);
        const data = await response.json();

        if (data.result === 'success') {
            const rate = data.conversion_rates[toCurrency];
            if (rate) {
                const convertedAmount = amount * rate;
                showResult(amount, fromCurrency, convertedAmount, toCurrency, rate);
            } else {
                throw new Error(`Conversion rate not found for ${toCurrency}`);
            }
        } else {
            throw new Error(data['error-type'] || 'Conversion failed');
        }
    } catch (error) {
        showError('Conversion failed: ' + error.message);
    } finally {
        showLoading(false);
    }
}

function showResult(originalAmount, fromCurrency, convertedAmount, toCurrency, rate) {
    resultAmount.textContent = `${convertedAmount.toFixed(2)} ${toCurrency}`;
    resultText.textContent = `${originalAmount} ${fromCurrency} equals`;
    exchangeRate.textContent = `Exchange rate: 1 ${fromCurrency} = ${rate.toFixed(4)} ${toCurrency}`;
    resultDiv.classList.remove('hidden');
}

function hideResult() {
    resultDiv.classList.add('hidden');
}

function showLoading(show) {
    if (show) {
        loadingDiv.classList.remove('hidden');
        convertBtn.disabled = true;
        convertBtn.classList.add('opacity-50', 'cursor-not-allowed');
    } else {
        loadingDiv.classList.add('hidden');
        convertBtn.disabled = false;
        convertBtn.classList.remove('opacity-50', 'cursor-not-allowed');
    }
}

function showError(message) {
    errorMessage.textContent = message;
    errorDiv.classList.remove('hidden');
}

function hideError() {
    errorDiv.classList.add('hidden');
}

// Add swap functionality
const swapBtn = document.createElement('button');
swapBtn.innerHTML = '🔄';
swapBtn.className = 'absolute right-4 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-gray-600 text-xl';
swapBtn.title = 'Swap currencies';

// Add swap button to the currency selects container
const currencyContainer = document.createElement('div');
currencyContainer.className = 'relative';
toCurrencySelect.parentNode.insertBefore(currencyContainer, toCurrencySelect);
currencyContainer.appendChild(toCurrencySelect);
currencyContainer.appendChild(swapBtn);

swapBtn.addEventListener('click', () => {
    const temp = fromCurrencySelect.value;
    fromCurrencySelect.value = toCurrencySelect.value;
    toCurrencySelect.value = temp;
});