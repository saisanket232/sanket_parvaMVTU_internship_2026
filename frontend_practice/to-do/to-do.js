function addtask(){

    var input = document.getElementById("task");
    var taskValue = input.value.trim();

    if(taskValue === ""){
        alert("Please enter a task");
        return;
    }

    var taskList = document.getElementById("task-list");

    var li = document.createElement("li");
    li.className = "list-group-item d-flex justify-content-between align-items-center";

    var span = document.createElement("span");
    span.innerText = taskValue;

    var completeBtn = document.createElement("button");
    completeBtn.innerText = "Complete";
    completeBtn.className = "btn btn-success btn-sm";

    completeBtn.onclick = function(){
        span.classList.toggle("completed");
    };

    var deleteBtn = document.createElement("button");
    deleteBtn.innerText = "Delete";
    deleteBtn.className = "btn btn-danger btn-sm";

    deleteBtn.onclick = function(){
        taskList.removeChild(li);
    };

    var buttonGroup = document.createElement("div");

    buttonGroup.appendChild(completeBtn);
    buttonGroup.appendChild(deleteBtn);

    li.appendChild(span);
    li.appendChild(buttonGroup);

    taskList.appendChild(li);

    input.value = "";
}

document.getElementById("task").addEventListener("keypress", function(event){

    if(event.key === "Enter"){
        addtask();
    }

});