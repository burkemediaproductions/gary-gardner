document.addEventListener("DOMContentLoaded", () => {
  const body = document.body;
  const menuButton = document.querySelector("[data-menu-button]");
  const nav = document.querySelector("[data-nav]");
  const navClose = document.querySelector("[data-nav-close]");
  const navBackdrop = document.querySelector("[data-nav-backdrop]");
  const navLinks = document.querySelectorAll("[data-nav-link]");
  const revealItems = document.querySelectorAll(".reveal");
  const desktopBreakpoint = 1400;

  const normalizePath = (path) => {
    if (!path) return "/";
    let normalized = path.replace(/index\.html$/, "");
    normalized = normalized.replace(/\/+$/, "");
    return normalized === "" ? "/" : normalized;
  };

  const currentPath = normalizePath(window.location.pathname);

  navLinks.forEach((link) => {
    const href = link.getAttribute("href");
    if (!href || href.startsWith("http") || href.startsWith("mailto:") || href.startsWith("#")) {
      return;
    }

    const linkPath = normalizePath(new URL(href, window.location.origin).pathname);

    link.removeAttribute("aria-current");

    if (linkPath === currentPath) {
      link.setAttribute("aria-current", "page");
    }
  });

  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    revealItems.forEach((item) => item.classList.add("is-visible"));
  } else if ("IntersectionObserver" in window) {
    const revealObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        });
      },
      {
        threshold: 0.12,
        rootMargin: "0px 0px -8% 0px"
      }
    );

    revealItems.forEach((item) => revealObserver.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add("is-visible"));
  }

  if (!menuButton || !nav || !navClose || !navBackdrop) return;

  const openMenu = () => {
    nav.classList.add("open");
    navBackdrop.classList.add("open");
    menuButton.setAttribute("aria-expanded", "true");
    body.classList.add("nav-open");
    navClose.focus();
  };

  const closeMenu = () => {
    nav.classList.remove("open");
    navBackdrop.classList.remove("open");
    menuButton.setAttribute("aria-expanded", "false");
    body.classList.remove("nav-open");
    menuButton.focus();
  };

  menuButton.addEventListener("click", () => {
    const expanded = menuButton.getAttribute("aria-expanded") === "true";
    expanded ? closeMenu() : openMenu();
  });

  navClose.addEventListener("click", closeMenu);
  navBackdrop.addEventListener("click", closeMenu);

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && nav.classList.contains("open")) {
      closeMenu();
    }
  });

  nav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      if (window.innerWidth < desktopBreakpoint) {
        closeMenu();
      }
    });
  });
});