function Save(){
  let Na = document.getElementById("Name").value ;
  let id = document.getElementById("ID").value;
  let Em = document.getElementById("E").value ;
  let Ph = document.getElementById("Ph").value  ;
  let Gpa = document.getElementById("GPA").value  ;
  let Birth = document.getElementById("Dob").value ;

  const select = document.getElementById("g");
  let G = select.options[select.selectedIndex].value  ;

  let Lev = document.getElementById("Lev").value  ;

  let stat = document.getElementsByName('Status');
  let Stat ;
  for(let i = 0; i < stat.length; i++) {
    if(stat[i].checked) {
      Stat = stat[i].value;
    }
  }
  let Depart = document.getElementById("Depart").value  ;
  let Pass = document.getElementById("Pass").value  ;
  let PassConfirm = document.getElementById("PassConf").value  ;

  if (Na === "" || id === "" || Em === "" || Ph === "" || Gpa === "" ||
    Birth === "" || Lev === "" || Stat === "" || Depart === "" ||
    Pass === "" || PassConfirm === ""){
    swal("Empty fields", "Please enter all fields", "error", {
      button: "try again",
    });
  }
  else{
    if (Lev < 3 && Depart !== ""){
      swal("Low Level", "Department in Level 3 or above", "error", {
        button: "try again",
      });
    }
    else{
      let storageItems = localStorage.getItem(id);
      if (storageItems !== null) {
        swal("ID is already exist", "you should use an unique id", "error", {
          button: "Ok",
        });
      }
      else{
        if (Pass !== PassConfirm){
          swal("Passwords are not identical", "Please enter identical Passwords", "error", {
            button: "try again",
          });
        }
        else{
          let Stud = {
            Name: Na,
            ID: id,
            Email: Em,
            Phone: Ph,
            GPA: Gpa,
            birth: Birth,
            Gender: G,
            Level: Lev,
            Status: Stat,
            Department: Depart,
            Password: Pass
          }

          window.localStorage.setItem(id, JSON.stringify(Stud)) ;
          window.location.href = "../HTML/Login.html" ;
        }
      }
    }
  }
}
