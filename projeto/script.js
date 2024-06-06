var map;
var iconcasa = L.icon({
    iconUrl: './imagens/home-address.png',
    iconSize: [50, 50], 
    iconAnchor: [25, 50],
    popupAnchor: [0, -50]
});

var iconongs = L.icon({
    iconUrl: './imagens/information-point.png',
    iconSize: [50, 50], 
    iconAnchor: [25, 50],
    popupAnchor: [0, -50]
});

function success(pos) {
    console.log(pos.coords.latitude, pos.coords.longitude);

    if (map == undefined) {
        map = L.map('map').setView([pos.coords.latitude, pos.coords.longitude], 13);
        map.locate({setView: true, maxZoom: 16});
    } else {
        map.setView([pos.coords.latitude, pos.coords.longitude], 13);
    }

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.marker([pos.coords.latitude, pos.coords.longitude], { icon: iconcasa }).addTo(map)
        .bindPopup('Você está aqui!')
        .openPopup();


    carregarDadosDasOngs();
}

function error(err) {
    console.log(err);
}

navigator.geolocation.watchPosition(success, error, {
    enableHighAccuracy: true
});

function carregarDadosDasOngs() {
    fetch('ongs_localizacao.csv')
        .then(response => response.text())
        .then(text => {
            const rows = text.split('\n').slice(1); 
            const ongs = rows.map(row => {
                const columns = row.split(',');
                return {
                    "Nome da ONG": columns[0],
                    "Latitude": parseFloat(columns[1]),
                    "Longitude": parseFloat(columns[2]),
                    "Região": columns[3]
                };
            });
            adicionarMarcadores(ongs);
        })
        .catch(error => console.error(error));
}

function adicionarMarcadores(ongs) {
    ongs.forEach(function(ong) {
        var popupContent = `
            <div>
                <h3>${ong["Nome da ONG"]}</h3>
                <p><b><i class="fa-solid fa-location-dot"></i> Região:</b> ${ong["Região"]}</p>
                <p><b><i class="fa-solid fa-phone"></i> Telefone:</b> (XX) XXXX-XXXX</p>
                <p><b> <i class="fa-brands fa-instagram"></i> Instagram:</b> @${ong["Nome da ONG"].toLowerCase().replace(/\s/g, '')}</p>
                <button class="alerta" onclick="emitirAlerta()">Emitir Alerta</button>
            </div>
        `;

        var marker = L.marker([ong.Latitude, ong.Longitude], { icon: iconongs }).addTo(map);
        
        marker.on('click', function() {
            marker.bindPopup(popupContent).openPopup();
        });
    });
}

function emitirAlerta() {
    alert("Alerta emitido! Por favor, aguarde por assistência.");
}
