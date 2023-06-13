$(document).ready(function () {
    $.validator.addMethod("passwordMatch", function (value) {
        let password = $("#Pass").val();
        return password === value;
    }, "Passwords do not match.");

    $.validator.addMethod("DepartmentValidate", function () {
        let L = $("#Lev").val();

        if (L >= 3) {
            $("#Depart").prop("readonly", false);
            $("#Depart").prop("required", true);
            return $("#Depart").val() !== "";
        }
        else {
            $("#Depart").prop("readonly", true);
            $("#Depart").prop("required", false);
            $("#Depart").val("General", true);
            return true;
        }
    });

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
                DepartmentValidate: true,
            },
            Password: {
                required: true,
                minlength: 8,
                maxlength: 15
            },
            PassConf: {
                required: true,
                passwordMatch: true
            }
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
            BirthDate: {
                required: "Please enter Birth date.",
            },
            Department: {
                required: "Department is required if Level is greater than or equal to 3.",
            },
            Level: {
                required: "Please enter Level.",
            },
            Password: {
                required: "Please enter a password.",
                minlength: "The password should be at least 8 characters.",
                maxlength: "The password should be at most 15 characters."
            },
            PassConf: {
                required: "Please confirm your password.",
            }
        },
        submitHandler: function (form) {
            swal({
                title: "Success!",
                icon: "success",
                text: "Your registration successed.",
                button: "ok",
            }).then(() => {
                form.submit()
            })
        }
    });
});