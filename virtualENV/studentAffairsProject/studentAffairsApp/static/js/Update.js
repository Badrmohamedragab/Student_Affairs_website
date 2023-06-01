function Remove() {
  const urlParams = new URLSearchParams(window.location.search);
  const id = urlParams.get('id');
  window.localStorage.removeItem(id);
}
function data(i) {
  window.location.href = "Update?id=" + i;
}
function showdata() {
  const urlParams = new URLSearchParams(window.location.search);
  const id = urlParams.get('id');
  let stu = JSON.parse(localStorage.getItem(id));
  document.getElementById("username").value = stu.Name;
  document.getElementById("ID").value = stu.ID;
  document.getElementById("E").value = stu.Email;
  document.getElementById("Ph").value = stu.Phone;
  document.getElementById("GPA").value = stu.GPA;
  document.getElementById("Dob").value = stu.birth;
  document.getElementById("Lev").value = stu.Level;
  document.getElementById("Depart").value = stu.Department;

  let Stat = document.getElementsByName("Status");

  for (let i = 0; i < Stat.length; i++) {
    if (Stat[i].value === stu.Status) {
      Stat[i].checked = true;
    }
  }
}

function Done() {

  const urlParams = new URLSearchParams(window.location.search);
  const id = urlParams.get('id');
  let Stud = JSON.parse(localStorage.getItem(id));

  Stud.Name = document.getElementById("username").value;
  Stud.ID = document.getElementById("ID").value;
  Stud.Email = document.getElementById("E").value;
  Stud.Phone = document.getElementById("Ph").value;
  Stud.GPA = document.getElementById("GPA").value;
  Stud.birth = document.getElementById("Dob").value;

  const select = document.getElementById("g");
  Stud.Gender = select.options[select.selectedIndex].value;

  Stud.Level = document.getElementById("Lev").value;

  const Stat = document.getElementsByName('Status');
  for (let i = 0; i < Stat.length; i++) {
    if (Stat[i].checked) {
      Stud.Status = Stat[i].value;
    }
  }
  Stud.Department = document.getElementById("Depart").value;
  window.localStorage.setItem(id, JSON.stringify(Stud));
  swal("Successful", "The information changed successfully", "success", { //sweet alert
    button: "ok",
  }).then(() => {
    window.location.href = "/Home-Registered";
  });
}
