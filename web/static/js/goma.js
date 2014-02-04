function loadInnerContent(elem) {
    $.ajax({
        type: "GET",
        url: $(elem).attr('data-url'),
        success: function(data) {
            $('#app-body').html(data.html);
            $('#content-title').html(data.title);
        }
    });
}
