function updateContentTitle(title) {
    $('#content-title').html(title);
}

function updateAppBody(elem) {
    $.ajax({
        type: "GET",
        url: $(elem).attr('data-url'),
        success: function(data) {
            if (data.header) {
                $('#app-header').html(data.header);
            }
            if (data.body) {
                $('#app-body').html(data.body);
            }
        }
    });
}
