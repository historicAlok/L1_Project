document.getElementById('priceForm').addEventListener('submit', function (e) {
e.preventDefault(); // Prevent form from submitting the default way

// Get form values
const bedrooms = document.getElementById('bedrooms').value;
const bathrooms = document.getElementById('bathrooms').value;
const livingArea = document.getElementById('living_area').value;
// const zipcode = document.getElementById('zipcode').value;
const location = document.getElementById('locationDropdown').value;

// Prepare data object
const formData = {
    bedrooms: parseInt(bedrooms),
    bathrooms: parseInt(bathrooms),
    living_area: parseFloat(livingArea),
    // zipcode: zipcode,
    location: location
};

// Print to console (for testing)
console.log('Form Data:', formData);

// Optional: Send data to backend via fetch
fetch('/predict', {
    method: 'POST',
    headers: {
    'Content-Type': 'application/json'
    },
    body: JSON.stringify(formData)
})
    .then(response => response.json())
    .then(data => {
    // Show result
    document.getElementById('result').innerText = `Predicted Price: ₹${data.price}`;
    })
    .catch(error => {
    console.error('Error:', error);
    document.getElementById('result').innerText = 'Error in predicting the price.';
    document.getElementById('result').style.color = 'red';
    });
});
