var females = [1, 2, 4, 5];
var males = [3, 6];

var gender = document.getElementById("student-gender").innerText;

if (gender === "M") {
  random = males[Math.floor(Math.random() * males.length)];
} else if (gender === "F") {
  random = females[Math.floor(Math.random() * females.length)];
} else {
  random = 3;
}

document
  .getElementById("student-avatar")
  .setAttribute(
    "src",
    "https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava" +
      random +
      ".webp"
  );

var supgender = document.getElementById("supervisor-gender").innerText;

if (supgender === "M") {
  suprandom = males[Math.floor(Math.random() * males.length)];
} else if (supgender === "F") {
  suprandom = females[Math.floor(Math.random() * females.length)];
} else {
  suprandom = 3;
}

document
  .getElementById("supervisor-avatar")
  .setAttribute(
    "src",
    "https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava" +
      suprandom +
      ".webp"
  );

// Figure out how to change the avatar url to static directory
