$("#id_door_type").change(function () {
    let door_type_id = $(this).val();  // get the selected country ID from the HTML input
    $.ajax({                       // initialize an AJAX request
        url: '/ajax/load-locks',                    // set the url of the request
        data: {
            'door_type': door_type_id       // add the country id to the GET parameters
        },
        success: function (data) {
            $("#id_lock").html(data);

        }
    });
    $.ajax({                       // initialize an AJAX request
        url: "/ajax/load-hinges",                    // set the url of the request
        data: {
            'door_type': door_type_id       // add the country id to the GET parameters
        },
        success: function (data) {
            $("#id_hinges").html(data);
        }
    });
    $.ajax({                       // initialize an AJAX request
        url: "/ajax/load-engravings",                    // set the url of the request
        data: {
            'door_type': door_type_id       // add the country id to the GET parameters
        },
        success: function (data) {
            $("#id_engraving").html(data);
        }
    });
});

