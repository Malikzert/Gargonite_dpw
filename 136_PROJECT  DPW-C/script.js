$(function(){
    let tidur = 0;
    let air = 0;
    let olahraga = 0;
    let usia = 0;
    let gender = "";
    let langkah=0

    $('#health-form').submit(function (e){
        e.preventDefault();
        tidur = parseInt($('#tidur').val());
        air = parseInt($('#air').val());
        olahraga = parseInt($('#olahraga').val());
        usia = parseInt($('#usia').val());
        langkah = parseInt($('#langkah').val());
        gender = $("input[name='gender']:checked").val();
        pengingat();
    });
    $('#health-form').on('reset', function() {
        $('#reminder').empty();
    });

    function usia_jika() {
        let usia = parseInt($('#usia').val());
        $('#olahraga, #langkah').prop('required', usia >= 8);
    }
    $('#usia').change(usia_jika);    

    function pengingat(){
        let message = [];
        if(usia >= 1 && usia <= 2) {
            if(tidur < 11 || tidur > 14) {
                message.push("Harusnya Kebutuhan tidur Anda dalam sehari adalah 11-14 jam.");
            }
        } else if(usia >= 3 && usia <= 5) {
            if(tidur < 10 || tidur > 13) {
                message.push("Harusnya Kebutuhan tidur Anda dalam sehari adalah 10-13 jam.");
            }
        } else if(usia >= 6 && usia <= 13) {
            if(tidur < 9 || tidur > 11) {
                message.push("Harusnya Kebutuhan tidur Anda dalam sehari adalah 9-11 jam.");
            }
        } else if(usia >= 14 && usia <= 17) {
            if(tidur < 8 || tidur > 10) {
                message.push("Harusnya Kebutuhan tidur Anda dalam sehari adalah 8-10 jam.");
            }
        } else if(usia >= 18) {
            if(tidur < 7 || tidur > 9) {
                message.push("Harusnya Kebutuhan tidur Anda dalam sehari adalah 7-9 jam.");
            }
        }
        
        if(usia >= 1 && usia <= 3) {
            if(air < 800 || air > 1000) {
                message.push("Harusnya kebutuhan minum air Anda dalam sehari adalah 800-1000 ml.");
            }
        } else if(usia >= 4 && usia <= 8) {
            if(air < 1200 || air > 1600) {
                message.push("Harusnya kebutuhan minum air Anda dalam sehari adalah 1200-1600 ml.");
            }
        } else if(usia >= 9 && usia <= 13) {
            if(gender === "perempuan" && (air < 1600 || air > 2000)) {
                message.push("Harusnya kebutuhan minum air Anda dalam sehari adalah 1600-2000 ml.");
            } else if(gender === "lakilaki" && (air < 2000 || air > 2400)) {
                message.push("Harusnya kebutuhan minum air Anda dalam sehari adalah 2000-2400 ml.");
            }
        } else if(usia >= 14 && usia <= 18) {
            if(gender === "perempuan" && (air < 1800 || air > 2200)) {
                message.push("Harusnya kebutuhan minum air Anda dalam sehari adalah 1800-2200 ml.");
            } else if(gender === "lakilaki" && (air < 2200 || air > 3200)) {
                message.push("Harusnya kebutuhan minum air Anda dalam sehari adalah 2200-3200 ml.");
            }
        } else if(usia >= 19) {
            if(air < 2000 || air > 3000) {
                message.push("Harusnya kebutuhan minum air Anda dalam sehari adalah 2000-3000 ml.");
            }
        }
        if (usia >= 8) {
            if (langkah < 5000 ) {
                message.push("Anda termasuk sedentary. Perbanyak gerak tubuh anda.");
            } else if (langkah >= 5000 && langkah < 7500) {
                if (olahraga < 30) {
                    message.push("Anda termasuk sedikit aktif. Perbanyak jumlah langkah dan lakukan olahraga minimal 30 menit per hari.");
                } else if (olahraga >= 30 && olahraga <= 60) {
                    message.push("Anda termasuk sedikit aktif. Perbanyak jumlah langkah, dan Olahraga Anda cukup untuk hari ini.");
                } else if (olahraga > 60) {
                    message.push("Anda termasuk sedikit aktif. Perbanyak jumlah langkah, Anda mungkin terlalu banyak berolahraga.");
                }
            } else if (langkah >= 7500 && langkah < 10000) {
                if (olahraga < 30) {
                    message.push("Anda termasuk cukup aktif. Pastikan lakukan olahraga minimal 30 menit per hari.");
                } else if (olahraga >= 30 && olahraga <= 60) {
                    message.push("Anda termasuk cukup aktif. Olahraga Anda cukup untuk hari ini.");
                } else if (olahraga > 60) {
                    message.push("Anda termasuk cukup aktif. Perbanyak jumlah langkah, Anda mungkin terlalu banyak berolahraga.");
                }
            } else if (langkah >= 10000) {
                if (olahraga < 30) {
                    message.push("Anda termasuk aktif. Pastikan lakukan olahraga minimal 30 menit per hari.");
                } else if (olahraga >= 30 && olahraga <= 60) {
                    message.push("Anda termasuk aktif. Olahraga Anda cukup untuk hari ini.");
                } else if (olahraga > 60) {
                    message.push("Anda termasuk aktif. Anda mungkin terlalu banyak berolahraga.");
                }
            }
        }
        let messageContainer = $('#reminder');
        if (message.length > 0) {
            let reminderHTML = '<div class="bg-warning p-2 mt-2 fw-bold" >Pengingat hari ini :<br>'; 
            for(let i = 0; i < message.length; i++) {
                reminderHTML += message[i] + '<br>';
            }
            reminderHTML += '</div>';
            messageContainer.html(reminderHTML); 
        } else {
            messageContainer.html('<div class=" bg-success p-2 mt-2 fw-bold" >Anda sudah menjaga kondisi  dengan baik sekarang.</div>');
        }
    }
});