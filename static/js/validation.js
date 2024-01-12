const today = new Date()

function isInvalid(data){

    tanggal = data['tanggal']
    bulan = data['bulan']
    tahun = data['tahun']

    console.log(bulan)

    if (bulan < 1 || bulan > 12){
        return "Bulan Tidak Valid"
    }

    if( tahun < today.getFullYear()){
        return "masukkan tahun di masa depan"
    }

    if (bulan == 2){
        if( tanggal < 1 || tanggal > 28){
            return "bulan tidak valid"
        }
    }else{
        if(tanggal < 1 || tanggal > 31){
            return "bulan tidak valid"
        }
    }

    return false
}