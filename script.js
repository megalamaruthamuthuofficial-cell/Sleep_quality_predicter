// ===========================
// Form Validation
// ===========================

function validateForm() {

    const age = document.getElementById("age").value;
    const sleep = document.getElementById("sleep_duration").value;

    if (age <= 0 || age > 100) {

        alert("Please enter a valid age.");

        return false;
    }

    if (sleep <= 0 || sleep > 24) {

        alert("Sleep duration must be between 1 and 24 hours.");

        return false;
    }

    return true;
}


// ===========================
// Show Loader
// ===========================

function showLoader() {

    if (validateForm()) {

        document.getElementById("loader").style.display = "flex";

    }

}