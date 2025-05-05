function loginRedirect() {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
  
    if (username === "admin" && password === "1234") {
      window.location.href = "adminHome.html";
    } else if (username === "user" && password === "1234") {
      window.location.href = "index.html";
    } else {
      alert("Incorrect username or password.");
    }
  
    return false; // prevent default form submission
  }