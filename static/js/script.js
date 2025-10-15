document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM fully loaded and parsed");

    const showModal = (id) => {
        const el = document.getElementById(id);
        if (!el) return;
        // close any open modals first
        document.querySelectorAll(".modal.show").forEach(openModal => {
            const instance = bootstrap.Modal.getInstance(openModal);
            if (instance) instance.hide();
        });
        // then open the new one
        const modal = new bootstrap.Modal(el);
        modal.show();
        console.log(`Modal with id ${id} shown`);
    };   
});
