function confirmStudentEnrollment(elem) {
    $.ajax({
        type: "GET",
        url: $(elem).attr('data-url'),
        success: function(data) {
            if (data.title) {
                $('#content-title').html(data.title);
            }
            if (data.header) {
                $('#app-header').html(data.header);
            }
            if (data.body) {
                $('#app-body').html(data.body);
            }
        }
    });
}

function updateStudentProfileBody(elem) {
    $.ajax({
        type: "GET",
        url: $(elem).attr('data-url'),
        success: function(data) {
            if (data.html) {
                $(elem).siblings().removeClass('active')
                $(elem).addClass('active');
                $('#student-profile-body').html(data.html);
            }
        }
    })
}
