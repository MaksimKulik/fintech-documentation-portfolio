(function () {
  function enhanceTables() {
    document.querySelectorAll(".md-content table").forEach(function (table) {
      if (table.classList.contains("tw-table")) {
        return;
      }

      table.classList.add("tw-table");

      const materialWrapper = table.closest(".md-typeset__table");

      if (materialWrapper) {
        materialWrapper.classList.add("tw-table-wrap");
        return;
      }

      if (!table.closest(".tw-table-wrap")) {
        const wrapper = document.createElement("div");
        wrapper.className = "tw-table-wrap";

        table.parentNode.insertBefore(wrapper, table);
        wrapper.appendChild(table);
      }
    });
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(function () {
      enhanceTables();
    });
  } else {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", enhanceTables);
    } else {
      enhanceTables();
    }
  }
})();