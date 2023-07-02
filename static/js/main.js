const addEventListeners = () => {
    const btnAddRevenue = document.getElementById("add-revenue");
    const btnAddExpense = document.getElementById("add-expense");
    const myButton = document.getElementById("dark-mode-toggle");
    const icon = document.getElementById("dl-icon")

    function toggleDarkMode() {
        const body = document.body;
        body.classList.toggle("dark-mode");
        const isDarkModeEnabled = body.classList.contains("dark-mode");
        localStorage.setItem("darkModeEnabled", isDarkModeEnabled);

        const btnDashboard = document.getElementById("dashboard");
        const btnExtract = document.getElementById("extract");
        const btnAbout = document.getElementById("about");
        const username = document.getElementById("username");
        const logout = document.getElementById("logout");
        const path = window.location.pathname;

        if (isDarkModeEnabled) {
            username.classList.add("text-white");
            logout.classList.add("text-white");
            switch (path) {
                case "/dashboard":
                    btnDashboard.classList.add("text-white");
                    btnExtract.classList.add("text-white");
                    btnAbout.classList.add("text-white");
                    break;
                case "/extract":
                    btnExtract.classList.add("text-white");
                    btnDashboard.classList.add("text-white");
                    btnAbout.classList.add("text-white");
                    break;
                case "/about":
                    btnAbout.classList.add("text-white");
                    btnDashboard.classList.add("text-white");
                    btnExtract.classList.add("text-white");
                    break;
            }
        } else {
            username.classList.remove("text-white");
            username.classList.add("text-body");

            logout.classList.remove("text-white");
            logout.classList.add("text-body");
            switch (path) {
                case "/dashboard":
                    btnExtract.classList.remove("text-white");
                    btnAbout.classList.remove("text-white");

                    btnExtract.classList.add("text-body");
                    btnAbout.classList.add("text-body");
                    break;
                case "/extract":
                    btnDashboard.classList.remove("text-white");
                    btnAbout.classList.remove("text-white");

                    btnDashboard.classList.add("text-body");
                    btnAbout.classList.add("text-body");
                    break;
                case "/about":
                    btnDashboard.classList.remove("text-white");
                    btnExtract.classList.remove("text-white");

                    btnDashboard.classList.add("text-body");
                    btnExtract.classList.add("text-body");
                    break;
            }
        }
    }

    btnAddRevenue.addEventListener("click", () => {
        $('#ModalRevenue').modal('show');
    });

    btnAddExpense.addEventListener("click", () => {
        $('#ModalExpense').modal('show');
    });

    myButton.addEventListener("click", function () {
        icon.classList.toggle('fa-moon');
        icon.classList.toggle('fa-sun');
        toggleDarkMode();
    });
}

const sidebarFunctions = () => {
    const btnDashboard = document.getElementById("dashboard");
    const btnExtract = document.getElementById("extract");
    const btnAbout = document.getElementById("about");
    const path = window.location.pathname;
    const isDarkModeEnabled = localStorage.getItem("darkModeEnabled");
    const username = document.getElementById("username");
    const logout = document.getElementById("logout");

    if (isDarkModeEnabled === "true") {
        username.classList.add("text-white");
        logout.classList.add("text-white");
    } else {
        username.classList.add("text-body");
        logout.classList.add("text-body");
    }

    switch (path) {
        case "/dashboard":
            btnDashboard.classList.add("active");
            if (isDarkModeEnabled === "true") {
                btnDashboard.classList.add("text-white");
                btnExtract.classList.add("text-white");
                btnAbout.classList.add("text-white");
            } else {
                btnExtract.classList.add("text-body");
                btnAbout.classList.add("text-body");
            }
            break;
        case "/extract":
            btnExtract.classList.add("active");
            if (isDarkModeEnabled === "true") {
                btnExtract.classList.add("text-white");
                btnDashboard.classList.add("text-white");
                btnAbout.classList.add("text-white");
            } else {
                btnDashboard.classList.add("text-body");
                btnAbout.classList.add("text-body");
            }
            break;
        case "/about":
            btnAbout.classList.add("active");
            if (isDarkModeEnabled === "true") {
                btnAbout.classList.add("text-white");
                btnDashboard.classList.add("text-white");
                btnExtract.classList.add("text-white");
            } else {
                btnDashboard.classList.add("text-body");
                btnExtract.classList.add("text-body");
            }
            break;
    }
}

document.addEventListener('DOMContentLoaded', function () {
    addEventListeners();
    sidebarFunctions();

    const isDarkModeEnabled = localStorage.getItem("darkModeEnabled");

    if (isDarkModeEnabled === "true") {
        const body = document.body;
        body.classList.add("dark-mode");
    }
});