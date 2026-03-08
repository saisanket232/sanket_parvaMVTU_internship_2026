const form = document.getElementById("sform");
const display = document.getElementById("display");

form.addEventListener("submit", function(e){

e.preventDefault();

const name = document.getElementById("name").value.trim();
const email = document.getElementById("email").value.trim();
const phone = document.getElementById("number").value.trim();
const course = document.getElementById("course").value;
const address = document.getElementById("address").value.trim();

const genderElement = document.querySelector('input[name="gender"]:checked');
const gender = genderElement ? genderElement.value : "";

const skillNodes = document.querySelectorAll('input[name="skills"]:checked');
let skills = [];

skillNodes.forEach(function(skill){
skills.push(skill.value);
});

skills = skills.join(", ");

if(name === ""){
alert("Name cannot be empty");
return;
}

if(!email.includes("@") || !email.includes(".")){
alert("Enter a valid email");
return;
}

if(phone.length !== 10 || isNaN(phone)){
alert("Enter a valid 10 digit phone number");
return;
}

display.innerHTML = `
<div class="card p-3">
<h4>Student Details</h4>
<p><strong>Name:</strong> ${name}</p>
<p><strong>Email:</strong> ${email}</p>
<p><strong>Phone:</strong> ${phone}</p>
<p><strong>Course:</strong> ${course}</p>
<p><strong>Gender:</strong> ${gender}</p>
<p><strong>Skills:</strong> ${skills}</p>
<p><strong>Address:</strong> ${address}</p>
</div>
`;

});