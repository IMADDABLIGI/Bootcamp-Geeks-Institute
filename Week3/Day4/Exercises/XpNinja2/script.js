// Get DOM elements
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');
const signInForm = document.getElementById('signInForm');
const signUpForm = document.getElementById('signUpForm');

// Add event listeners for switching between forms
signUpButton.addEventListener('click', () => {
    container.classList.add('right-panel-active');
});

signInButton.addEventListener('click', () => {
    container.classList.remove('right-panel-active');
});

// Handle form submissions
signInForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    // Get form data
    const email = signInForm.querySelector('input[type="email"]').value;
    const password = signInForm.querySelector('input[type="password"]').value;
    
    // Basic validation
    if (!email || !password) {
        showMessage('Please fill in all fields', 'error');
        return;
    }
    
    if (!isValidEmail(email)) {
        showMessage('Please enter a valid email address', 'error');
        return;
    }
    
    // Simulate login process
    showMessage('Signing in...', 'info');
    
    setTimeout(() => {
        showMessage('Sign in successful!', 'success');
        // Here you would typically send the data to your server
        console.log('Sign In Data:', { email, password });
        
        // Reset form
        signInForm.reset();
    }, 1500);
});

signUpForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    // Get form data
    const name = signUpForm.querySelector('input[type="text"]').value;
    const email = signUpForm.querySelector('input[type="email"]').value;
    const password = signUpForm.querySelector('input[type="password"]').value;
    
    // Basic validation
    if (!name || !email || !password) {
        showMessage('Please fill in all fields', 'error');
        return;
    }
    
    if (!isValidEmail(email)) {
        showMessage('Please enter a valid email address', 'error');
        return;
    }
    
    if (password.length < 6) {
        showMessage('Password must be at least 6 characters long', 'error');
        return;
    }
    
    // Simulate registration process
    showMessage('Creating account...', 'info');
    
    setTimeout(() => {
        showMessage('Account created successfully!', 'success');
        // Here you would typically send the data to your server
        console.log('Sign Up Data:', { name, email, password });
        
        // Reset form and switch to sign in
        signUpForm.reset();
        setTimeout(() => {
            container.classList.remove('right-panel-active');
        }, 2000);
    }, 1500);
});

// Utility function to validate email
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Function to show messages to the user
function showMessage(message, type = 'info') {
    // Remove any existing messages
    const existingMessage = document.querySelector('.toast-message');
    if (existingMessage) {
        existingMessage.remove();
    }
    
    // Create message element
    const messageDiv = document.createElement('div');
    messageDiv.className = `toast-message fixed top-5 right-5 px-6 py-4 rounded-lg shadow-lg z-50 max-w-sm transition-all duration-300 transform translate-x-full`;
    
    // Set message style based on type
    switch (type) {
        case 'success':
            messageDiv.style.backgroundColor = '#10b981';
            messageDiv.style.color = 'white';
            break;
        case 'error':
            messageDiv.style.backgroundColor = '#ef4444';
            messageDiv.style.color = 'white';
            break;
        case 'info':
            messageDiv.style.backgroundColor = '#3b82f6';
            messageDiv.style.color = 'white';
            break;
        default:
            messageDiv.style.backgroundColor = '#6b7280';
            messageDiv.style.color = 'white';
    }
    
    messageDiv.textContent = message;
    
    // Add to DOM
    document.body.appendChild(messageDiv);
    
    // Animate in
    setTimeout(() => {
        messageDiv.style.transform = 'translateX(0)';
    }, 100);
    
    // Remove after 4 seconds
    setTimeout(() => {
        messageDiv.style.transform = 'translateX(100%)';
        setTimeout(() => {
            if (messageDiv.parentNode) {
                messageDiv.remove();
            }
        }, 300);
    }, 4000);
}

// Add input focus effects
document.querySelectorAll('input').forEach(input => {
    input.addEventListener('focus', function() {
        this.style.backgroundColor = '#fff';
        this.style.boxShadow = '0 0 0 2px #8b5cf6';
    });
    
    input.addEventListener('blur', function() {
        if (this.value === '') {
            this.style.backgroundColor = '#eee';
            this.style.boxShadow = 'none';
        }
    });
    
    // Handle input animation
    input.addEventListener('input', function() {
        if (this.value !== '') {
            this.style.backgroundColor = '#fff';
        }
    });
});

// Add keyboard navigation support
document.addEventListener('keydown', (e) => {
    // Press Tab + Shift to switch between forms
    if (e.key === 'Tab' && e.shiftKey && e.ctrlKey) {
        e.preventDefault();
        if (!container.classList.contains('right-panel-active')) {
            container.classList.add('right-panel-active');
        } else {
            container.classList.remove('right-panel-active');
        }
    }
    
    // Press Escape to go back to Sign In
    if (e.key === 'Escape') {
        container.classList.remove('right-panel-active');
    }
});

// Button hover effects
const buttons = document.querySelectorAll('.btn, .btn-transparent');
buttons.forEach(button => {
    button.addEventListener('mouseenter', function() {
        this.style.transform = 'scale(1.05)';
    });
    
    button.addEventListener('mouseleave', function() {
        this.style.transform = 'scale(1)';
    });
    
    button.addEventListener('mousedown', function() {
        this.style.transform = 'scale(0.95)';
    });
    
    button.addEventListener('mouseup', function() {
        this.style.transform = 'scale(1.05)';
    });
});

// Initialize the form
document.addEventListener('DOMContentLoaded', () => {
    // Ensure we start in sign-in mode
    container.classList.remove('right-panel-active');
    
    // Add loading animation
    container.style.opacity = '0';
    container.style.transform = 'scale(0.9)';
    
    setTimeout(() => {
        container.style.transition = 'all 0.3s ease';
        container.style.opacity = '1';
        container.style.transform = 'scale(1)';
    }, 100);
});

// Add smooth scrolling for mobile
if (window.innerWidth <= 768) {
    document.body.style.overflow = 'hidden';
}

// Handle window resize
window.addEventListener('resize', () => {
    if (window.innerWidth <= 768) {
        document.body.style.overflow = 'hidden';
    } else {
        document.body.style.overflow = 'auto';
    }
});