let out;
let charts = [];
        $("#formPredict form").submit(function(e){
            e.preventDefault()

            $('.page3').fadeIn()
            $('#result #overlay').show()
            setTimeout(function(){
                $('#result #overlay #loader2').addClass('change')
            }, 8000)
            scrollToElem($('#result'))
            var formData = {
                tanggal: $("#formPredict form [name='tanggal']").val(),
                bulan: $("#formPredict form [name='bulan']").val(),
                tahun: $("#formPredict form [name='tahun']").val(),
                lokasi: $("#formPredict form [name='lokasi']").val(),
            }

            $.ajax({
                type: "POST",
                url:  "/app/machinery",
                data: formData,
                dataType: "JSON",
                encode: true,
                success: function(response){
                    $('#result #overlay').hide()
                    var partikulat = response['partikulat'] 
                    console.log(response)
                    if (charts.length > 0){
                        charts.forEach(chart => {
                            chart.destroy()
                        });
                    }
                    charts[0] = showChart(partikulat['pm10'], 'pm10', 420)
                    charts[1] = showChart(partikulat['so2'], 'so2', 1250)
                    charts[2] = showChart(partikulat['co'], 'co', 60)
                    charts[3] = showChart(partikulat['o3'], 'o3', 300)
                    charts[4] = showChart(partikulat['no2'], 'no2', 600)
                    charts[5] = showChart(partikulat['pm25'], 'pm25', 300)
                    showResultDesc(response)
                },
                error: function(response){
                    console.error(response)
                }
            });

        })

        function scrollToElem(elem){
            $('html, body').animate({
                scrollTop: elem.offset().top
            }, 1000);
        }