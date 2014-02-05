function addClass(data) {
    setupAjax();
    var request = $.ajax({
        type    :'post',
        url     :'/api/klasses',
        data    :data,
        processData : false,
        contentType : 'application/json',
    })
}

function convertDateFormat(dateString) {
    date = new Date(dateString);
    newString = date.getFullYear() + '-' + date.getMonth() + '-' + date.getDate();
    return newString;
}
function save() {
    form = $('#add-class-form');
    classname = form.find('input[name=classname]').val();
    dates = form.find('input[name=classdaterangepicker]').val();
    colour = form.find('select[name=class-colour-picker]').val();
    dates = dates.split(' - ');
    start = convertDateFormat(dates[0]);
    end = convertDateFormat(dates[1]);
    data = {
        'title' : classname,
        'start' : start,
        'end'   : end,
        'teacher' : 1,
        'colour': colour
    }
    addClass(JSON.stringify(data));
 }

$(function(){
        'use strict';

        $('#classdaterangepicker').daterangepicker(
            {
                format: 'YYYY-MM-DD',
                buttonClasses: 'btn btn-ion'
            }
        );

        // colorpicker
        $('#class-colour-picker').simplecolorpicker({
            theme: 'glyphicons'
        });

        $('#add-class-form').validate({
            errorElement: 'div',
            errorClass: 'help-block',
            focusInvalid: false,
            rules: {
                classname : {
                    required: true,
                },
            },
            messages: {
                classname : {
                    required: "Please provide a class name."
                },
            }
        });

    })