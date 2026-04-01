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

  if (menuButton && nav && navClose && navBackdrop) {
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
  }

  const galleryLinks = Array.from(document.querySelectorAll("[data-lightbox]"));

  if (galleryLinks.length) {
    const overlay = document.createElement("div");
    overlay.className = "lightbox-overlay";
    overlay.hidden = true;
    overlay.innerHTML = `
      <div class="lightbox-dialog" role="dialog" aria-modal="true" aria-label="Image gallery">
        <button class="lightbox-close" type="button" aria-label="Close image viewer">×</button>
        <div class="lightbox-image-wrap">
          <img class="lightbox-image" src="" alt="">
        </div>
        <p class="lightbox-caption"></p>
        <div class="lightbox-nav">
          <button class="lightbox-prev" type="button" aria-label="Previous image">‹</button>
          <button class="lightbox-next" type="button" aria-label="Next image">›</button>
        </div>
      </div>
    `;
    document.body.appendChild(overlay);

    const imageEl = overlay.querySelector(".lightbox-image");
    const captionEl = overlay.querySelector(".lightbox-caption");
    const closeBtn = overlay.querySelector(".lightbox-close");
    const prevBtn = overlay.querySelector(".lightbox-prev");
    const nextBtn = overlay.querySelector(".lightbox-next");

    let currentIndex = 0;
    let activeGroup = [];

    const openLightbox = (group, index) => {
      activeGroup = group;
      currentIndex = index;

      const link = activeGroup[currentIndex];
      const img = link.querySelector("img");

      imageEl.src = link.href;
      imageEl.alt = img ? img.alt : "";
      captionEl.textContent = img ? img.alt : "";
      overlay.hidden = false;
      document.body.classList.add("nav-open");
      closeBtn.focus();
    };

    const closeLightbox = () => {
      overlay.hidden = true;
      imageEl.src = "";
      document.body.classList.remove("nav-open");
    };

    const showIndex = (index) => {
      if (!activeGroup.length) return;
      currentIndex = (index + activeGroup.length) % activeGroup.length;

      const link = activeGroup[currentIndex];
      const img = link.querySelector("img");

      imageEl.src = link.href;
      imageEl.alt = img ? img.alt : "";
      captionEl.textContent = img ? img.alt : "";
    };

    galleryLinks.forEach((link) => {
      link.addEventListener("click", (event) => {
        event.preventDefault();
        const groupName = link.getAttribute("data-lightbox");
        const group = galleryLinks.filter(
          (item) => item.getAttribute("data-lightbox") === groupName
        );
        const index = group.indexOf(link);
        openLightbox(group, index);
      });
    });

    closeBtn.addEventListener("click", closeLightbox);
    prevBtn.addEventListener("click", () => showIndex(currentIndex - 1));
    nextBtn.addEventListener("click", () => showIndex(currentIndex + 1));

    overlay.addEventListener("click", (event) => {
      if (event.target === overlay) closeLightbox();
    });

    document.addEventListener("keydown", (event) => {
      if (overlay.hidden) return;
      if (event.key === "Escape") closeLightbox();
      if (event.key === "ArrowLeft") showIndex(currentIndex - 1);
      if (event.key === "ArrowRight") showIndex(currentIndex + 1);
    });
  }

  const donationChoices = document.querySelectorAll('input[name="donation-choice"]');
  const customAmountWrap = document.getElementById("custom-amount-wrap");
  const customAmountInput = document.getElementById("donate-amount-other");
  const finalDonationAmount = document.getElementById("donation-amount-final");

  if (
    donationChoices.length &&
    customAmountWrap &&
    customAmountInput &&
    finalDonationAmount
  ) {
    const updateDonationAmount = () => {
      const selected = document.querySelector('input[name="donation-choice"]:checked');

      if (!selected) {
        customAmountWrap.hidden = true;
        customAmountInput.required = false;
        customAmountInput.value = "";
        finalDonationAmount.value = "";
        return;
      }

      if (selected.value === "other") {
        customAmountWrap.hidden = false;
        customAmountInput.required = true;
        finalDonationAmount.value = customAmountInput.value.trim();
      } else {
        customAmountWrap.hidden = true;
        customAmountInput.required = false;
        customAmountInput.value = "";
        finalDonationAmount.value = selected.value;
      }
    };

    donationChoices.forEach((choice) => {
      choice.addEventListener("change", updateDonationAmount);
    });

    customAmountInput.addEventListener("input", () => {
      finalDonationAmount.value = customAmountInput.value.trim();
    });

    updateDonationAmount();
  }

  const donateForm = document.querySelector('form[name="donate"]');

  if (donateForm) {
    donateForm.addEventListener("submit", async (e) => {
      e.preventDefault();

      const formData = new FormData(donateForm);
      const amount = String(formData.get("donation-amount") || "").trim();

      if (!amount || Number.isNaN(Number(amount)) || Number(amount) <= 0) {
        alert("Please enter a valid donation amount.");
        return;
      }

      const recaptchaEl = donateForm.querySelector('[data-netlify-recaptcha="true"]');
      if (recaptchaEl && typeof grecaptcha !== "undefined") {
        const response = grecaptcha.getResponse();
        if (!response) {
          alert("Please complete the reCAPTCHA.");
          return;
        }
      }

      const submitButton = donateForm.querySelector('button[type="submit"]');
      const originalButtonText = submitButton ? submitButton.textContent : "";

      if (submitButton) {
        submitButton.disabled = true;
        submitButton.textContent = "Redirecting to secure checkout...";
      }

      const payload = {
        firstName: formData.get("first-name"),
        lastName: formData.get("last-name"),
        occupation: formData.get("occupation"),
        phone: formData.get("phone"),
        email: formData.get("email"),
        address1: formData.get("address-line-1"),
        address2: formData.get("address-line-2"),
        city: formData.get("city"),
        state: formData.get("state-region"),
        zip: formData.get("zip-postal"),
        country: formData.get("country"),
        donationAmount: amount
      };

      try {
        const res = await fetch("/.netlify/functions/create-checkout-session", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        });

        const data = await res.json().catch(() => ({}));

        if (!res.ok) {
          throw new Error(data.error || "Unable to start Stripe checkout.");
        }

        if (data.url) {
          window.location.href = data.url;
          return;
        }

        throw new Error("Stripe checkout session URL was not returned.");
      } catch (err) {
        console.error("Stripe checkout error:", err);
        alert(err.message || "There was an error connecting to Stripe.");
      } finally {
        if (submitButton) {
          submitButton.disabled = false;
          submitButton.textContent = originalButtonText || "Submit Donation Info";
        }
      }
    });
  }
});
