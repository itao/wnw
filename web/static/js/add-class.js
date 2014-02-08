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

function save() {
    form = $('#add-class-form');
    if (form.valid()) {
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


        jQuery.validator.addMethod('dateRange', function(value, element) {
            return true
        }, 'Please specify date range in format "MM/DD/YYYY - MM/DD/YYYY"');

        $('#add-class-form').validate({
            errorElement: 'div',
            errorClass: 'help-block',
            focusInvalid: false,
            rules: {
                classname : {
                    required: true,
                },
                classdaterangepicker : {
                    dateRange : true
                }
            },
            messages: {
                classname : {
                    required: "Please provide a class name."
                },
            }
        });


    })