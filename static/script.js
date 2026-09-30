const activityInput = document.querySelector("#activity-input")
const addButton = document.querySelector("#add-button")
const activityList = document.querySelector("#activity-list")

const destinationInput = document.querySelector("#destination");
const startDateInput = document.querySelector("#start-date");
const endDateInput = document.querySelector("#end-date");
const saveTripButton = document.querySelector("#save-trip");


function displayActivity(activity) {
    const newActivity = document.createElement("li");
    newActivity.innerText = activity.name;

    const deleteButton = document.createElement("button");
    deleteButton.innerText = "Delete";

    newActivity.appendChild(deleteButton);
    activityList.appendChild(newActivity);

    // DELETE ACTIVITY
    deleteButton.addEventListener("click", function() {
        fetch(`/delete_activity/${activity.id}`, {
            method: "DELETE"
        })
        .then(response => {
            if (response.ok) {
                activityList.removeChild(newActivity);
            }
        });
    });
}

addButton.addEventListener("click", function() {
    const activity = activityInput.value.trim();

    if (activity !== "") {

        fetch("/add_activity", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ name: activity })
        })
        .then(response => response.json())
        .then(data => {
            displayActivity(data);
        });

        activityInput.value = "";

    } else {
        alert("Please enter an activity.");
    }
});

fetch("/activities")
    .then(response => response.json())
    .then(data => {
        data.forEach(activity => {
            displayActivity(activity);
        });
    })
    .catch(error => {
        console.error("Error fetching activities:", error);
    });

    
saveTripButton.addEventListener("click", function() {
    const destination = destinationInput.value.trim();
    const startDate = startDateInput.value;
    const endDate = endDateInput.value;

   console.log(destination, startDate, endDate);

    fetch("/save_trip", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ destination, start_date: startDate, end_date: endDate })
    })
    .then(response => {
        console.log("Flask response:", response.status);
    });
});

fetch("/trip")
    .then(response => response.json())
    .then(data => {
        if (data.destination) {
            destinationInput.value = data.destination;
            startDateInput.value = data.start_date;
            endDateInput.value = data.end_date;
        }
    });
