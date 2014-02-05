function updateContentTitle(title) {
    $('#content-title').html(title);
}

function updateAppBody(elem) {
    $.ajax({
        type: "GET",
        url: $(elem).attr('data-url'),
        success: function(data) {
            // Set nav item as the only active
            $(elem).siblings().removeClass('active')
            $(elem).addClass('active');

            // Update content
            if (data.title) {
                updateContentTitle(data.title);
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
