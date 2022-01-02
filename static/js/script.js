$(document).ready(function () {
    // INITILIZATION
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();

    // UPLOAD PREVIEW
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#imagePreview').hide();
                $('#imagePreview').fadeIn(650);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        readURL(this);
    });

    // PREDICT
    $('.upload-label').click(function () {
        $('.webcam').hide();
    });
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);
        // SHOW LOADING ANIMATION
        $(this).hide();
        $('.loader').show();

        // MAKE PREDICTION BY CALLING API /PREDICT
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (predictions) {
                // GET AND DISPLAY THE RESULT
                $('#result').fadeIn(600);
                $('.loader').hide();
                if (predictions.length === 0) {
                    $('#result').text(' Result:  ' + 'No Landmarks Detected');
                } else {
                    $('.image-section').hide();
                    $('#result').html('<img src="data:image/png;base64,' + predictions + '"/>');
                }
                console.log('Success!');
            },
        });
    });
});

