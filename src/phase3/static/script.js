var cities = {
    'Shoreline': '98133',
    'Kent': '98042',
    'Bellevue': '98008',
    'Redmond': '98052',
    'Seattle': '98115',
    'LakeForestPark': '98155',
    'Sammamish': '98074',
    'Auburn': '98106',
    'DesMoines': '98007',
    'NorthBend': '98092',
    'Bothell': '98198',
    'FederalWay': '98045',
    'Kirkland': '98006',
    'NormandyPark': '98102',
    'FallCity': '98011',
    'Renton': '98125',
    'Woodinville': '98003',
    'Snoqualmie': '98136',
    'Issaquah': '98033',
    'MapleValley': '98117',
    'Duvall': '98034',
    'Burien': '98107',
    'Covington': '98166',
    'InglewoodFinnHill': '98116',
    'Carnation': '98024',
    'Kenmore': '98055',
    'Newcastle': '98077',
    'BlackDiamond': '98059',
    'ClydeHill': '98065',
    'MercerIsland': '98199',
    'Algona': '98027',
    'Skykomish': '98058',
    'Tukwila': '98122',
    'Vashon': '98103',
    'SeaTac': '98112',
    'Enumclaw': '98005',
    'SnoqualmiePass': '98029',
    'Pacific': '98075',
    'Ravensdale': '98118',
    'BeauxArtsVillage': '98177',
    'Preston': '98105',
    'Milton': '98023',
    'Medina': '98004',
    'YarrowPoint': '98038'
};

var cityDropdown = document.getElementById('CITY');
var zipInput = document.getElementById('ZIP');

cityDropdown.addEventListener('change', function () {
    const selectedCity = this.value;
    if (cities[selectedCity]) {
        zipInput.value = cities[selectedCity];
    } else {
        zipInput.value = '';
    }
});

document.querySelectorAll('.rating').forEach((rating) => {
    rating.addEventListener('click', (event) => {
        const selectedStar = event.target;
        const ratingValue = parseInt(selectedStar.getAttribute('data-rating'));
        const stars = rating.querySelectorAll('span');
        stars.forEach((star) => {
            const starValue = parseInt(star.getAttribute('data-rating'));
            if (starValue <= ratingValue) {
                star.classList.add('active');
            } else {
                star.classList.remove('active');
            }
        });
    });
});

document.getElementById('prediction-form').addEventListener('submit', function (event) {
    event.preventDefault();
    // Collect form data
    const formData = new FormData(this);
    // Convert form data to JSON format
    var jsonData = {};
    for (const [key, value] of formData.entries()) {
        jsonData[key] = value;
    }
    // Add view rating from the dataset
    const viewRating = parseInt(document.querySelector('#view-rating > span.active').getAttribute('data-rating'));
    jsonData['VIEW_RATING'] = viewRating;
    // Add condition rating from the dataset
    const conditionRating = parseInt(document.querySelector('#condition-rating > span.active').getAttribute('data-rating'));
    jsonData['CONDITION_RATING'] = conditionRating;
    console.log(jsonData)
    // Send data to server for prediction
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
        .then(response => response.json())
        .then(data => {
            // Display prediction result
            document.getElementById('result').innerHTML = `<p>Predicted Price: ${data.price}</p>`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
});