let map = L.map('map').setView([51.505, -0.09], 13);


    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap'
    }).addTo(map);

    let latlngs = [['39.277105911797', '-94.573555314885'], ['39.277129788807', '-94.573314917428'], ['39.277042649122', '-94.573300520356'], ['39.277042188595', '-94.573305170383'], ['39.277018793306', '-94.573540916807'], ['39.277105911797', '-94.573555314885']]
    let polygon = L.polygon(latlngs, {color: 'red'}).addTo(map);
    map.fitBounds(polygon.getBounds());

    function updateMap(polyString) {
        let myElement = document.getElementById(polyString)
        console.log(polyString)
        let myvalue = myElement.value;
        myvalue = myvalue.split('[[')[1]
        myvalue = myvalue.split(']]')[0]
        myvalue = myvalue.split('], [')
        let arr = []
        for (const element of myvalue) {
            let item = element.split(",")
            item = [item[0].split("'")[1], item[1].split("'")[1]]
            arr.push(item); 
        }
        console.log(arr)
        let latlngs = arr;
        let polygon = L.polygon(latlngs, {color: 'red'}).addTo(map);
        
        map.fitBounds(polygon.getBounds());
    }


    