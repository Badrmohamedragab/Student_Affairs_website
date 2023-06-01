function appear() {
    let ele2 = document.getElementById("label");
    if (ele2.value !== '') {
        if (!(document.getElementById("table-body").innerHTML === ''))
            document.getElementById("table").style.visibility = "visible";

        else
            document.getElementById("table").style.visibility = "hidden";

    }
}

function getSearchData() {
    const name = document.getElementById("label").value;
    var tableBody = document.getElementById("table-body");
    tableBody.innerHTML = "";
    if (name.trim() === "") {
        swal("Oops...", "Enter valid name.", "error", {
            button: "Ok",
        });
        return;
    }
    var found = false;

    for (let i = 0; i < localStorage.length; i++) {
        let key = localStorage.key(i);
        let student = JSON.parse(localStorage.getItem(key));
        if (student.Name.toLowerCase().includes(name.trim().toLowerCase())) {
            var row = document.createElement("tr");

            var nameCell = document.createElement("td");
            nameCell.innerHTML = student.Name

            var idCell = document.createElement("td");
            idCell.innerHTML = student.ID;

            var statusCell = document.createElement("td");
            statusCell.innerHTML = student.Status;

            var levelCell = document.createElement("td");
            levelCell.innerHTML = student.Level;

            var changeDepartmentCell = document.createElement("td");
            var changeDepartmentBtn = document.createElement("button");
            changeDepartmentBtn.innerHTML = "Change Department";
            changeDepartmentBtn.onclick = function () {
                if (student.Level >= 3) {
                    getRow(student.ID)
                }

                else {
                    swal("Oops...", "The level is less than 3", "error", {
                        button: "Ok",
                    });
                }
            };
            changeDepartmentCell.appendChild(changeDepartmentBtn);


            row.appendChild(nameCell);
            row.appendChild(idCell);
            row.appendChild(statusCell);
            row.appendChild(levelCell);
            row.appendChild(changeDepartmentCell);
            tableBody.appendChild(row);

            found = true;
        }
    }
    if (!found) {
        swal("Oops...", "No student with this name found.", "error", {
            button: "Ok",
        });
    }
}
function getRow(i) {
    window.location.href = "change department.html?id=" + i;
}
function SendID() {
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');
    let stu = JSON.parse(localStorage.getItem(id));
    document.getElementById("StdNam").value = stu.Name;
    document.getElementById("id").value = stu.ID;
    document.getElementById("Department").value = stu.Department;
}










