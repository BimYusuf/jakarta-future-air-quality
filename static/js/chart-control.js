
    function indexColor(p, j){
        var baik = { 'warna' : "rgb(164, 240, 13)", 'level' : 'baik'}
        var sedang = { 'warna' : "rgb(236, 240, 13)", 'level' : 'sedang'}
        var tidak_sehat = { 'warna' : "rgb(255, 196, 0)", 'level' : 'tidak sehat'}
        var sangat_tidak_sehat = { 'warna' : "rgb(206, 41, 0)", 'level' : 'sangat tidak sehat'}
        var berbahaya = { 'warna' : "rgb(82, 16, 0)", 'level' : 'berbahaya'}
        switch (j) {

            case "pm25":
                if(p >= 0 && p <= 25) return baik
                else if(p > 25 && p <= 75 ) return sedang
                else if(p > 75 && p <= 200) return tidak_sehat
                else if(p > 200 && p <= 300) return sangat_tidak_sehat
                else if(p > 300) return berbahaya
                break;
            case "pm10":
                if(p >= 0 && p < 50) return baik
                else if(p >= 50 && p <= 150) return sedang
                else if(p > 150 && p <= 350) return tidak_sehat
                else if(p > 350 && p <= 420) return sangat_tidak_sehat
                else if(p > 420) return berbahaya
                break;
            case "so2":
                if(p >= 0 && p <= 350) return baik
                else if(p > 350 && p <= 750) return sedang
                else if(p > 750 && p <= 1250) return tidak_sehat
                else if(p > 1250 && p <= 1250) return sangat_tidak_sehat
                else if(p > 1250) return berbahaya
                break;
            case "co":
                if(p >= 0 && p <= 10) return baik
                else if(p > 10 && p <= 35) return sedang
                else if(p > 35 && p <= 60) return tidak_sehat
                else if(p > 60 && p <= 60) return sangat_tidak_sehat
                else if(p > 60) return berbahaya
                break
            case "o3":
                if(p >= 0 && p <= 100) return baik
                else if(p > 100 && p <= 200) return tidak_sehat
                else if(p > 200 && p <= 300) return sangat_tidak_sehat
                else if(p > 300) return berbahaya
                break
            case "no2":
                if(p >= 0 && p <= 200) return baik
                else if(p > 200 && p <= 400) return tidak_sehat
                else if(p > 400 && p <= 600) return sangat_tidak_sehat
                else if(p > 600) return berbahaya
                break
            default:
                break;
        }
    }

    const elem_chart = {
        'pm10' : document.getElementById('pm10-chart'),
        'so2' : document.getElementById('so2-chart'),
        'co' : document.getElementById('co-chart'),
        'o3' : document.getElementById('o3-chart'),
        'no2' : document.getElementById('no2-chart'),
        'pm25' : document.getElementById('pm25-chart'),
    }

    function showChart(p, j, ar){

        let chart = new Chart(elem_chart[j], {
            type: 'bar',
            data: {
                labels : [j+' µg/m³'],
                datasets: [{
                    label: indexColor(p, j)['level'],
                    data: [p],
                    backgroundColor : [
                        indexColor(p, j)['warna'],
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                plugins: {
                    legend: {
                        labels: {
                            boxWidth : 20,
                            boxHeight : 20
                        }
                    }
                },
                responsive : true,
                scales: {
                    y: {
                    beginAtZero: true,
                    max : ar,
                    },
                },
                maintainAspectRatio: false,
                aspectRatio: 1
            }
        });

        return chart
    }

    function showResultDesc(data){
        
        var cat_color = {
            BAIK : "rgb(164, 240, 13)",
            SEDANG : "rgb(236, 240, 13)",
            "TIDAK SEHAT": "rgb(255, 196, 0)",
            "SANGAT TIDAK SEHAT" : "rgb(206, 41, 0)",
            "BERBAHAYA" : "rgb(82, 16, 0)"
        }

        $('#result-desc #level-flag ').css('background-color', cat_color[data['cat']])
        $('#result-desc #level-flag h1').html(data['cat'])
        $('#result-desc p span#date').html(data['date'] +' '+ data['bulan'] +' '+ data['year'])
        $('#result-desc p span#prediksi').html(data['prediksi'] + '%')

    }

