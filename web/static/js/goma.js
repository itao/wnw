function updateContentTitle(title) {
    $('#content-title').html(title);
}

function updateAppBody(elem) {
    $.ajax({
        type: "GET",
        url: $(elem).attr('data-url'),
        success: function(data) {
            $(elem).siblings().removeClass('active')
            $(elem).addClass('active');
            if (data.title) {
                $('#content-title').html(data.title);
            }
            if (data.header) {
                $('#header-actions').html(data.header);
            }
            if (data.body) {
                $('#app-body').html(data.body);
            }
        }
    });
}
