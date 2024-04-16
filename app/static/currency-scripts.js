// Function to render the plot using Plotly
function renderPlot() {
    if (typeof plotData !== 'undefined') {
        Plotly.newPlot('plot', plotData.data, plotData.layout);
    }
}

// Function to handle the submit button for fetching historical rates
document.getElementById('submitButton').addEventListener('click', function() {
    var date = document.getElementById('dateInput').value;
    if (date) {
        window.location.href = '/historical/' + date;
    } else {
        alert("Please enter a date.");
    }
});

// Function to toggle the visibility of the currency list
function toggleCurrencyList() {
    var list = document.getElementById('currencyList');
    if (list.style.display === 'none' || list.style.display === '') {
        list.style.display = 'block';
    } else {
        list.style.display = 'none';
    }
}

// Function to filter the currency list based on input
function filterCurrencies() {
    var input = document.getElementById('searchBox');
    var filter = input.value.toUpperCase();
    var ul = document.getElementById('currencyList');
    var li = ul.getElementsByTagName('li');

    for (var i = 0; i < li.length; i++) {
        var txtValue = li[i].textContent.toUpperCase() || li[i].innerText.toUpperCase();
        if (txtValue.startsWith(filter)) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}

// Initialize the plot after the document is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    renderPlot();
});
