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