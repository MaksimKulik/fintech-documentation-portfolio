document.addEventListener("DOMContentLoaded", () => {
  const closeDropdown = (dropdown) => {
    if (!dropdown.open || dropdown.classList.contains("is-closing")) {
      return;
    }

    dropdown.classList.add("is-closing");

    window.setTimeout(() => {
      dropdown.open = false;
      dropdown.classList.remove("is-closing");
    }, 140);
  };

  const dropdowns = document.querySelectorAll(".api-auth-dropdown");

  dropdowns.forEach((dropdown) => {
    const options = dropdown.querySelectorAll(".api-auth-dropdown__option");

    options.forEach((option) => {
      option.addEventListener("click", (event) => {
        event.preventDefault();
        event.stopPropagation();
        closeDropdown(dropdown);
      });
    });

    dropdown.addEventListener("toggle", () => {
      if (dropdown.open) {
        dropdown.classList.remove("is-closing");
      }
    });
  });

  document.addEventListener("click", (event) => {
    dropdowns.forEach((dropdown) => {
      if (dropdown.open && !dropdown.contains(event.target)) {
        closeDropdown(dropdown);
      }
    });
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      dropdowns.forEach(closeDropdown);
    }
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const closeDropdown = (dropdown) => {
    if (!dropdown.open || dropdown.classList.contains("is-closing")) {
      return;
    }

    dropdown.classList.add("is-closing");

    window.setTimeout(() => {
      dropdown.open = false;
      dropdown.classList.remove("is-closing");
    }, 140);
  };

  const dropdowns = document.querySelectorAll(
    ".api-auth-dropdown, .api-content-type-dropdown"
  );

  dropdowns.forEach((dropdown) => {
    const options = dropdown.querySelectorAll(
      ".api-auth-dropdown__option, .api-content-type-dropdown__option"
    );

    options.forEach((option) => {
      option.addEventListener("click", (event) => {
        event.preventDefault();
        event.stopPropagation();
        closeDropdown(dropdown);
      });
    });
  });

  document.addEventListener("click", (event) => {
    dropdowns.forEach((dropdown) => {
      if (dropdown.open && !dropdown.contains(event.target)) {
        closeDropdown(dropdown);
      }
    });
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      dropdowns.forEach(closeDropdown);
    }
  });
});

function initApiCodeTabs() {
  document.querySelectorAll(".api-code-tabs").forEach((group) => {
    if (group.dataset.apiTabsPrepared === "true") {
      return;
    }

    group.dataset.apiTabsPrepared = "true";

    const select = group.querySelector(".api-code-select");
    const summary = select?.querySelector("summary");
    const menu = select?.querySelector(".api-code-select__menu");
    const options = Array.from(group.querySelectorAll(".api-code-option"));

    if (!select || !summary || !menu || options.length === 0) {
      return;
    }

    let activeOption =
      options.find((option) => option.classList.contains("is-active")) ||
      options[0];

    const updateHeader = (option) => {
      const groupType = group.dataset.apiCodeType;

      if (groupType === "request") {
        summary.textContent = option.dataset.label || option.dataset.language || "HTTP";
      }

      if (groupType === "response") {
        const status = option.dataset.status || option.dataset.label || "200";
        const statusText = option.dataset.statusText || "";
        const contentType = option.dataset.contentType || "application/json";

        const statusBadge = group.querySelector(".api-code-status");
        const responseText = group.querySelector(".api-code-card__response-text");

        if (statusBadge) {
          statusBadge.textContent = status;
          statusBadge.classList.remove("api-code-status--success", "api-code-status--error");

          const statusNumber = Number(status);
          statusBadge.classList.add(
            statusNumber >= 200 && statusNumber < 300
              ? "api-code-status--success"
              : "api-code-status--error"
          );
        }

        if (responseText) {
          responseText.textContent = statusText;
        }

        summary.textContent = status;
      }
    };

    const setActive = (option) => {
      options.forEach((item) => {
        item.classList.toggle("is-active", item === option);
      });

      menu.querySelectorAll(".api-code-select__option").forEach((button) => {
        button.classList.toggle(
          "is-active",
          button.dataset.label === option.dataset.label
        );
      });

      updateHeader(option);
    };

    options.forEach((option) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "api-code-select__option";
      button.dataset.label = option.dataset.label;
      button.textContent = option.dataset.label || option.dataset.language || "Example";

      button.addEventListener("click", (event) => {
        event.preventDefault();
        event.stopPropagation();

        setActive(option);
        select.open = false;
      });

      menu.appendChild(button);
    });

    setActive(activeOption);
  });
}

function initApiExampleTabs() {
  document.querySelectorAll(".api-example-tabs").forEach((group) => {
    if (group.dataset.apiExampleTabsPrepared === "true") {
      return;
    }

    group.dataset.apiExampleTabsPrepared = "true";

    const nav = group.querySelector(".api-example-tabs__nav");
    const options = Array.from(group.querySelectorAll(".api-example-option"));

    if (!nav || options.length === 0) {
      return;
    }

    let activeOption =
      options.find((option) => option.classList.contains("is-active")) ||
      options[0];

    const setActive = (option) => {
      options.forEach((item) => {
        item.classList.toggle("is-active", item === option);
      });

      nav.querySelectorAll(".api-example-tabs__tab").forEach((button) => {
        const isActive = button.dataset.label === option.dataset.label;
        button.classList.toggle("is-active", isActive);
        button.setAttribute("aria-selected", isActive ? "true" : "false");
      });
    };

    options.forEach((option) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "api-example-tabs__tab";
      button.dataset.label = option.dataset.label;
      button.textContent = option.dataset.label || "Example";
      button.setAttribute("role", "tab");
      button.setAttribute("aria-selected", "false");

      button.addEventListener("click", (event) => {
        event.preventDefault();
        setActive(option);
      });

      nav.appendChild(button);
    });

    setActive(activeOption);
  });
}

function enableCodeLineSelectionByDefault() {
  document
    .querySelectorAll('button.md-code__button[data-md-type="select"]')
    .forEach((button) => {
      if (button.dataset.apiLineSelectionInitialized === "true") {
        return;
      }

      button.dataset.apiLineSelectionInitialized = "true";

      if (!button.classList.contains("md-code__button--active")) {
        button.click();
      }
    });
}

function scheduleCodeLineSelection() {
  window.requestAnimationFrame(enableCodeLineSelectionByDefault);

  [120, 420, 900, 1600].forEach((delay) => {
    window.setTimeout(enableCodeLineSelectionByDefault, delay);
  });
}

function observeCodeLineSelectionButtons() {
  if (
    document.documentElement.dataset.apiLineSelectionObserver === "true" ||
    typeof MutationObserver === "undefined" ||
    !document.body
  ) {
    return;
  }

  document.documentElement.dataset.apiLineSelectionObserver = "true";

  const observer = new MutationObserver((mutations) => {
    const hasNewSelectButton = mutations.some((mutation) =>
      Array.from(mutation.addedNodes).some((node) => {
        if (!(node instanceof Element)) {
          return false;
        }

        return (
          node.matches?.('button.md-code__button[data-md-type="select"]') ||
          node.querySelector?.('button.md-code__button[data-md-type="select"]')
        );
      })
    );

    if (hasNewSelectButton) {
      scheduleCodeLineSelection();
    }
  });

  observer.observe(document.body, {
    childList: true,
    subtree: true,
  });
}

let apiCodeTextSelectionPre = null;

function getCodeLineSelectionContext(event) {
  const target =
    event.target instanceof Element ? event.target : event.target?.parentElement;
  const line = target?.closest(".md-code__content > span[id]");

  if (!line) {
    return null;
  }

  const code = line.closest(".md-code__content");
  const pre = code?.closest("pre");
  const selectButton = pre?.querySelector(
    'button.md-code__button[data-md-type="select"].md-code__button--active'
  );

  if (!pre || !selectButton) {
    return null;
  }

  const lineRect = line.getBoundingClientRect();
  const anchor = line.querySelector('a[id^="__codelineno"]');
  const anchorRect = anchor?.getBoundingClientRect();
  const lineSelectionZone = anchorRect
    ? Math.max(anchorRect.right + 8, lineRect.left + 16)
    : lineRect.left + 16;

  return {
    line,
    pre,
    isTextBody: event.clientX > lineSelectionZone,
  };
}

function unwrapMaterialLineSelectionPreview(scope) {
  scope?.querySelectorAll(".hll.select").forEach((highlight) => {
    highlight.replaceWith(...Array.from(highlight.childNodes));
  });
}

function installCodeTextSelectionGuard() {
  if (document.documentElement.dataset.apiCodeSelectionGuard === "true") {
    return;
  }

  document.documentElement.dataset.apiCodeSelectionGuard = "true";

  document.addEventListener(
    "mousedown",
    (event) => {
      if (event.button !== 0) {
        return;
      }

      const context = getCodeLineSelectionContext(event);

      if (!context) {
        return;
      }

      /*
        Material handles mousedown on the whole line when line selection is
        enabled. Keep the left gutter for line selection, but let normal text
        dragging work everywhere in the code body.
      */
      if (context.isTextBody) {
        apiCodeTextSelectionPre = context.pre;
        unwrapMaterialLineSelectionPreview(context.pre);
        event.stopPropagation();
      }
    },
    true
  );

  ["mouseenter", "mouseover", "mouseleave"].forEach((eventName) => {
    document.addEventListener(
      eventName,
      (event) => {
        if (!apiCodeTextSelectionPre) {
          return;
        }

        const context = getCodeLineSelectionContext(event);

        if (!context || context.pre !== apiCodeTextSelectionPre) {
          return;
        }

        /*
          Material wraps hovered code lines with .hll.select while line
          selection is active. During a text drag, those wrappers make browser
          selection snap toward whole lines, so suppress the hover preview until
          the drag finishes.
        */
        unwrapMaterialLineSelectionPreview(context.pre);
        event.stopPropagation();
      },
      true
    );
  });

  ["mouseup", "blur", "keyup"].forEach((eventName) => {
    window.addEventListener(
      eventName,
      () => {
        if (!apiCodeTextSelectionPre) {
          return;
        }

        const pre = apiCodeTextSelectionPre;
        window.setTimeout(() => {
          unwrapMaterialLineSelectionPreview(pre);
        }, 0);
        apiCodeTextSelectionPre = null;
      },
      true
    );
  });
}

function closeApiCodeSelects(event) {
  document.querySelectorAll(".api-code-select[open]").forEach((select) => {
    if (!select.contains(event.target)) {
      select.open = false;
    }
  });
}

if (typeof document$ !== "undefined") {
  document$.subscribe(() => {
    initApiCodeTabs();
    initApiExampleTabs();
    installCodeTextSelectionGuard();
    observeCodeLineSelectionButtons();
    scheduleCodeLineSelection();
  });
} else {
  document.addEventListener("DOMContentLoaded", () => {
    initApiCodeTabs();
    initApiExampleTabs();
    installCodeTextSelectionGuard();
    observeCodeLineSelectionButtons();
    scheduleCodeLineSelection();
  });
}

document.addEventListener("click", closeApiCodeSelects);
