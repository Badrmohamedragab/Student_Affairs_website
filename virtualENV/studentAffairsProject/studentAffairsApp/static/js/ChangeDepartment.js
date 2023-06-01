$(document).ready(function () {

    $("#validateForm").validate({
        submitHandler: function (form) {
            swal({
                title: "Success!",
                icon: "success",
                text: "Your registration successed.",
                button: "ok",

            }).then(() => {
                form.submit()
                window.location.href = "/Home-Registered" 
            })
        }
    });
});