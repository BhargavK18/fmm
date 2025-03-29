// Initialize flatpickr for check-in and check-out date fields
flatpickr("#checkin", {
    minDate: "today", // Disable past dates
    dateFormat: "Y-m-d", // Use YYYY-MM-DD format
});

flatpickr("#checkout", {
    minDate: "today", // Disable past dates
    dateFormat: "Y-m-d", // Use YYYY-MM-DD format
});

// Optional: Handle form validation or submission logic
document.querySelector("form").addEventListener("submit", function(event) {
    const checkinDate = document.querySelector("#checkin").value;
    const checkoutDate = document.querySelector("#checkout").value;

    // Ensure check-out date is after check-in date
    if (new Date(checkoutDate) <= new Date(checkinDate)) {
        event.preventDefault(); // Prevent form submission
        alert("Check-out date must be after check-in date.");
    } else {
        alert("Your booking has been submitted successfully!");
    }
});
