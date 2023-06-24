
const addEventListeners = () => {
    const btnAddRevenue = document.getElementById("add-revenue");
    const btnAddExpense = document.getElementById("add-expense");

    btnAddRevenue.addEventListener("click", () => {
        $('#myModal').modal('show');
    });

    btnAddExpense.addEventListener("click", () => {
        $('#myModalDespesa').modal('show');
    });
}

window.addEventListener("load", () => {
    addEventListeners();
});