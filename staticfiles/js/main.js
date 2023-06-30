const addEventListeners = () => {
    const btnAddRevenue = document.getElementById("add-revenue");
    const btnAddExpense = document.getElementById("add-expense");

    btnAddRevenue.addEventListener("click", () => {
        $('#ModalRevenue').modal('show');
    });

    btnAddExpense.addEventListener("click", () => {
        $('#ModalExpense').modal('show');
    });
}

const sidebarFunctions = () => {
    const btnDashboard = document.getElementById("dashboard");
    const btnExtract = document.getElementById("extract");
    const path = window.location.pathname;

    switch (path) {
        case "/dashboard":
            btnDashboard.classList.add("active");
            btnExtract.classList.add("text-body");
            break;
        case "/extract":
            btnExtract.classList.add("active");
            btnDashboard.classList.add("text-dark");
            break;
        default:
            btnDashboard.classList.add("active");
            btnExtract.classList.add("text-dark");
            break;
    }
}

document.addEventListener('DOMContentLoaded', function () {
    addEventListeners();
    sidebarFunctions();
});