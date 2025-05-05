document.addEventListener("DOMContentLoaded", () => {
    const rightArrows = document.querySelectorAll(".arrow-icon.right");
    const leftArrows = document.querySelectorAll(".arrow-icon.left");
    const movieLists = document.querySelectorAll(".movie-list");
    const filterSelect = document.getElementById("filterSelect"); // <-- you forgot this line

    // Arrow navigation
    rightArrows.forEach((arrow, index) => {
        arrow.addEventListener("click", () => {
            movieLists[index].scrollLeft += 270;
        });
    });

    leftArrows.forEach((arrow, index) => {
        arrow.addEventListener("click", () => {
            movieLists[index].scrollLeft -= 270;
        });
    });

    // Filtering logic
    filterSelect.addEventListener("change", () => {
        const value = filterSelect.value;

        movieLists.forEach(list => {
            const movieItems = Array.from(list.querySelectorAll(".movie-list-item"));
            let filteredItems = [...movieItems];

            if (value === "az") {
                filteredItems.sort((a, b) =>
                    a.querySelector(".movie-title").textContent.localeCompare(
                        b.querySelector(".movie-title").textContent
                    )
                );
            } else if (value === "za") {
                filteredItems.sort((a, b) =>
                    b.querySelector(".movie-title").textContent.localeCompare(
                        a.querySelector(".movie-title").textContent
                    )
                );
            } else if (value.startsWith("genre")) {
                const genre = value.split("-")[1];
                filteredItems = movieItems.filter(item =>
                    item.textContent.toLowerCase().includes(genre)
                );
            }

            // Update list
            list.innerHTML = "";
            filteredItems.forEach(item => list.appendChild(item));
        });
    });
});
