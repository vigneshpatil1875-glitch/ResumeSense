// ==========================================
// ResumeSense - Main JavaScript
// ==========================================

document.addEventListener("DOMContentLoaded", function () {

    // -------------------------------
    // Mobile Menu Toggle
    // -------------------------------
    const menuButton = document.getElementById("menuButton");
    const navMenu = document.getElementById("navMenu");

    if (menuButton && navMenu) {
        menuButton.addEventListener("click", function () {
            navMenu.classList.toggle("active");
        });
    }


    // -------------------------------
    // Resume File Selection
    // -------------------------------
    const resumeInput = document.getElementById("resume");
    const fileName = document.getElementById("fileName");

    if (resumeInput) {
        resumeInput.addEventListener("change", function () {

            if (this.files.length > 0) {
                const file = this.files[0];

                if (fileName) {
                    fileName.textContent = "Selected: " + file.name;
                }

                // Allow only PDF
                if (file.type !== "application/pdf") {
                    alert("Please upload a PDF resume.");
                    this.value = "";

                    if (fileName) {
                        fileName.textContent = "No file selected";
                    }
                }

                // Maximum file size: 5 MB
                else if (file.size > 5 * 1024 * 1024) {
                    alert("File size must be less than 5 MB.");
                    this.value = "";

                    if (fileName) {
                        fileName.textContent = "No file selected";
                    }
                }
            }
        });
    }


    // -------------------------------
    // Upload Form Loading Effect
    // -------------------------------
    const uploadForm = document.getElementById("uploadForm");
    const uploadButton = document.getElementById("uploadButton");

    if (uploadForm) {
        uploadForm.addEventListener("submit", function () {

            if (uploadButton) {
                uploadButton.disabled = true;
                uploadButton.innerHTML = "⏳ Analyzing Resume...";
            }
        });
    }


    // -------------------------------
    // Drag and Drop Upload
    // -------------------------------
    const dropArea = document.getElementById("dropArea");

    if (dropArea && resumeInput) {

        ["dragenter", "dragover"].forEach(function (eventName) {

            dropArea.addEventListener(eventName, function (event) {
                event.preventDefault();
                event.stopPropagation();

                dropArea.classList.add("drag-active");
            });

        });

        ["dragleave", "drop"].forEach(function (eventName) {

            dropArea.addEventListener(eventName, function (event) {
                event.preventDefault();
                event.stopPropagation();

                dropArea.classList.remove("drag-active");
            });

        });

        dropArea.addEventListener("drop", function (event) {

            const files = event.dataTransfer.files;

            if (files.length > 0) {

                const file = files[0];

                if (file.type === "application/pdf") {

                    resumeInput.files = files;

                    if (fileName) {
                        fileName.textContent =
                            "Selected: " + file.name;
                    }

                } else {

                    alert("Please upload a PDF file.");
                }
            }
        });
    }


    // -------------------------------
    // Smooth Scrolling
    // -------------------------------
    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(function (link) {

        link.addEventListener("click", function (event) {

            const targetId = this.getAttribute("href");

            if (targetId !== "#") {

                const target = document.querySelector(targetId);

                if (target) {

                    event.preventDefault();

                    target.scrollIntoView({
                        behavior: "smooth"
                    });
                }
            }
        });
    });


    // -------------------------------
    // Animate Score Numbers
    // -------------------------------
    const scoreElements =
        document.querySelectorAll(".score-number");

    scoreElements.forEach(function (element) {

        const finalScore =
            parseFloat(element.textContent);

        if (isNaN(finalScore)) {
            return;
        }

        let currentScore = 0;

        const duration = 1200;
        const steps = 60;
        const increment = finalScore / steps;

        const interval = setInterval(function () {

            currentScore += increment;

            if (currentScore >= finalScore) {

                currentScore = finalScore;
                clearInterval(interval);
            }

            element.textContent =
                currentScore.toFixed(1);

        }, duration / steps);
    });


    // -------------------------------
    // Progress Bar Animation
    // -------------------------------
    const progressBars =
        document.querySelectorAll(".progress-bar");

    progressBars.forEach(function (bar) {

        const width =
            bar.getAttribute("data-width");

        if (width) {

            bar.style.width = "0%";

            setTimeout(function () {

                bar.style.width = width + "%";

            }, 300);
        }
    });


    // -------------------------------
    // Search Jobs
    // -------------------------------
    const searchInput =
        document.getElementById("jobSearch");

    const jobCards =
        document.querySelectorAll(".job-card");

    if (searchInput) {

        searchInput.addEventListener("input", function () {

            const searchText =
                this.value.toLowerCase().trim();

            jobCards.forEach(function (card) {

                const text =
                    card.textContent.toLowerCase();

                if (text.includes(searchText)) {
                    card.style.display = "";
                } else {
                    card.style.display = "none";
                }
            });
        });
    }


    // -------------------------------
    // Back To Top Button
    // -------------------------------
    const topButton =
        document.getElementById("backToTop");

    if (topButton) {

        window.addEventListener("scroll", function () {

            if (window.scrollY > 300) {
                topButton.classList.add("show");
            } else {
                topButton.classList.remove("show");
            }
        });

        topButton.addEventListener("click", function () {

            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });

        });
    }


    // -------------------------------
    // Password Show / Hide
    // -------------------------------
    const passwordToggle =
        document.getElementById("passwordToggle");

    const passwordInput =
        document.getElementById("password");

    if (passwordToggle && passwordInput) {

        passwordToggle.addEventListener("click", function () {

            if (passwordInput.type === "password") {

                passwordInput.type = "text";
                passwordToggle.textContent = "Hide";

            } else {

                passwordInput.type = "password";
                passwordToggle.textContent = "Show";
            }

        });
    }


    // -------------------------------
    // Alert Auto Hide
    // -------------------------------
    const alerts =
        document.querySelectorAll(".alert");

    alerts.forEach(function (alert) {

        setTimeout(function () {

            alert.style.opacity = "0";

            setTimeout(function () {
                alert.remove();
            }, 500);

        }, 5000);

    });

});
