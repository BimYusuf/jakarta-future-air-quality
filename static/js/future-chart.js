const future_canvas = document.getElementById('future-chart')


// $.ajax({
//     type: "POST",
//     url:  "/app/future-quality",
//     success: function(response){
       
//     },
//     error: function(response){
//         console.error(response)
//     }
// });


const stackedLine = new Chart(future_canvas, {
    type: 'line',
    data: {
        labels: [2025, 2026, 2027, 2028, 2029],
        datasets: [{
            label: 'data dummy',
            data: [65, 59, 80, 81, 83],
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.4
        }, {
            label: 'data dummy',
            data: [72, 78, 64, 89, 90],
            borderColor: "rgb(237, 46, 12)",
            fill: false,
            // cubicInterpolationMode: 'monotone',
            tension: 0.4
        },
        {
            label: 'data dummy',
            data: [34, 56, 76, 65, 67],
            borderColor: "rgb(211, 223, 55)",
            fill: false,
            // cubicInterpolationMode: 'monotone',
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