function validatee() {
    let username = document.getElementById("un").value;
    let password = document.getElementById("pass").value;
    let student = JSON.parse(localStorage.getItem(username));

    if (localStorage.getItem(username) !== null && username === student.ID && password === student.Password) {
        swal("Login successfully", "Welcome " + student.Name, "success", {
            button: "Continue",
        }).then(() => {
            window.location.href = "../HTML/Home-Registered.html";
        });
        return false;
    } else {

        swal("Login failed", "Please check your username and password", "error", { //sweet alert
            button: "try again",
        });
        return false;
    }
}