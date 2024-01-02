const future_canvas = document.getElementById('future-chart')


$.ajax({
    type: "POST",
    url:  "/app/future-quality",
    success: function(response){
       
    },
    error: function(response){
        console.error(response)
    }
});


const stackedLine = new Chart(future_canvas, {
    type: 'line',
    data: {
        labels: [2025, 2026, 2027, 2028, 2029, 2030, 2031],
        datasets: [{
          label: 'PM10',
          data: [65, 59, 80, 81, 56, 55, 40],
          fill: false,
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.1
        }, {
            label: 'PM25',
            data: [34, 78, 43, 67, 81, 92, 21],
            borderColor: "rgb(237, 46, 12)",
            fill: false,
            cubicInterpolationMode: 'monotone',
            tension: 0.4
          }],
    },
    options: {
        scales: {
            y: {
                stacked: true
            }
        },
        responsive : true,
        maintainAspectRatio : false,
        aspectRatio : 1
    }
});