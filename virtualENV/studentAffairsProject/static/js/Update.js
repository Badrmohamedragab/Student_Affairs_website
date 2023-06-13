$(document).ready(function () {
    $("#validateForm").validate({
        rules: {
            Name: {
                required: true,
                minlength: 3,
                numeric: false
            },
            Email: {
                email: true,
                required: true
            },
            Id: {
                required: true
            },
            Phone: {
                required: true,
                minlength: 11,
                maxlength: 11
            },
            GPA: {
                required: true
            },
            BirthDate: {
                required: true
            },
            Level: {
                required: true
            },
            Department: {
                required: true
            },
            Password: {
                required: true,
                minlength: 8,
                maxlength: 15
            },
            
        },
        messages: {
            Name: {
                required: "Please enter a valid name.",
                minlength: "Name must be at least 3 characters."
            },
            Email: {
                required: "Please enter an email.",
                email: "Please enter valid email."
            },
            Phone: {
                required: "Please enter a phone.",
                minlength: "Please enter valid phone (11 digits).",
                maxlength: "Please enter valid phone."
            },
            Id: {
                required: "Please enter an id.",
            },
            GPA: {
                required: "Please enter a valid GPA."
            },
            Department: {
                required: "Please enter Department.",
            },
            BirthDate: {
                required: "Please enter Birth date.",
            },
            Level: {
                required: "Please enter Level.",
            },
            Password: {
                required: "Please enter a password.",
                minlength: "The password should be at least 8 characters.",
                maxlength: "The password should be at most 15 characters."
            },
            
        },
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