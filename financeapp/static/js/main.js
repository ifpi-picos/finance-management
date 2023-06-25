const addEventListeners = () => {
    const btnAddRevenue = document.getElementById("add-revenue");
    const btnAddExpense = document.getElementById("add-expense");
    const btnSubmitFormRevenue = document.getElementById("submit-form-revenue");
    const btnSubmitFormExpense = document.getElementById("submit-form-expense");
    const btnDeleteRevenue = document.getElementById("delete-earning-modal");
    const btnDeleteExpense = document.getElementById("delete-expense-modal");

    btnAddRevenue.addEventListener("click", () => {
        $('#ModalRevenue').modal('show');
    });

    btnAddExpense.addEventListener("click", () => {
        $('#ModalExpense').modal('show');
    });
    
    try {
        btnDeleteRevenue.addEventListener("click", () => {
            $('#deleteModalEarning').modal('show');
        });
    } catch (error) {
        console.log(error);
    }

    try {
        btnDeleteExpense.addEventListener("click", () => {
            $('#deleteModalExpense').modal('show');
        });
    } catch (error) {
        console.log(error);
    }

    btnSubmitFormRevenue.addEventListener("click", () => {
        const form = document.getElementById("form-revenue");
        form.submit();
    });

    btnSubmitFormExpense.addEventListener("click", () => {
        const form = document.getElementById("form-expense");
        form.submit();
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