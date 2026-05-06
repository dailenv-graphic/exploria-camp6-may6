(function () {
  var root = document.getElementById("owners-testimonials");
  if (!root) return;

  var INTRO_LONG =
    "See what fellow owners and guests have to say about their unforgettable experiences at Club Exploria resorts. You’ll be able to share your story too via video testimonial as well!!";
  var INTRO_SHORT =
    "See what fellow owners and guests have to say about their unforgettable experiences at Club Exploria resorts";

  var SLIDES = [
    {
      bgLayers: [
        "public/testimonials-carousel/orlando-bg-a.png",
        "public/testimonials-carousel/orlando-bg-b.png",
      ],
      intro: INTRO_LONG,
      title: "Summer Bay Orlando",
      subtitle: "By Exploria Resorts",
      quoteSize: "18px",
      quote:
        "Love this place! We do our family reunions here each year and can't be any happier with everything they have to offer.",
      author: "– Wayne M.",
      stamp: "public/testimonials-carousel/stamp-orlando.png",
    },
    {
      bgLayers: ["public/testimonials-carousel/daytona-bg.png"],
      intro: INTRO_SHORT,
      title: "Grand Seas Resort",
      subtitle: "By Exploria Resorts",
      quoteSize: "18px",
      quote:
        "Love this place! We do our family reunions here each year and can't be any happier with everything they have to offer.",
      author: "– Wayne M.",
      stamp: "public/testimonials-carousel/stamp-daytona.png",
    },
    {
      bgLayers: ["public/testimonials-carousel/poconos-bg.png"],
      intro: INTRO_SHORT,
      title: "Mountain Villas",
      subtitle: "By Exploria Resorts",
      quoteSize: "16px",
      quote:
        "Great place to stay and unwind. I especially love the old 3 bedroom deluxe with the jacuzzi tub and sauna in the master bedroom. I was there for an event so i didnt have time to make use of the amenities but will be sure to try and make use of them next time.",
      author: "– djsimmy2025",
      stamp: "public/testimonials-carousel/stamp-poconos.png",
    },
  ];

  var paneA = root.querySelector(".owners-testimonials__bg-pane--a");
  var paneB = root.querySelector(".owners-testimonials__bg-pane--b");
  var introEl = root.querySelector("[data-owners-intro]");
  var titleEl = root.querySelector("[data-owners-title]");
  var subtitleEl = root.querySelector("[data-owners-subtitle]");
  var quoteEl = root.querySelector("[data-owners-quote]");
  var authorEl = root.querySelector("[data-owners-author]");
  var stampEl = root.querySelector("[data-owners-stamp]");
  var prevBtn = root.querySelector("[data-owners-prev]");
  var nextBtn = root.querySelector("[data-owners-next]");
  var dots = root.querySelectorAll("[data-owners-dot]");

  var FADE_MS = 480;
  var current = 0;
  var activePane = paneA;
  var inactivePane = paneB;
  var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function renderBgPane(pane, slide) {
    if (!pane) return;
    pane.innerHTML = "";
    slide.bgLayers.forEach(function (src) {
      var img = document.createElement("img");
      img.className = "owners-testimonials__bg-img";
      img.src = src;
      img.alt = "";
      pane.appendChild(img);
    });
  }

  function applyContent(slide) {
    if (introEl) introEl.textContent = slide.intro;
    if (titleEl) titleEl.textContent = slide.title;
    if (subtitleEl) subtitleEl.textContent = slide.subtitle;
    if (quoteEl) {
      quoteEl.textContent = slide.quote;
      quoteEl.style.fontSize = slide.quoteSize;
    }
    if (authorEl) authorEl.textContent = slide.author;
    if (stampEl) {
      stampEl.src = slide.stamp;
    }
  }

  function setDots(index) {
    dots.forEach(function (dot, i) {
      var on = i === index;
      dot.classList.toggle("is-active", on);
      dot.setAttribute("aria-selected", on ? "true" : "false");
      if (on) dot.setAttribute("aria-current", "true");
      else dot.removeAttribute("aria-current");
    });
  }

  function swapBgPanes(slide) {
    if (!activePane || !inactivePane) return;
    renderBgPane(inactivePane, slide);
    inactivePane.classList.add("is-active");
    activePane.classList.remove("is-active");
    var t = activePane;
    activePane = inactivePane;
    inactivePane = t;
  }

  var animated = root.querySelectorAll(".owners-testimonials__animate");

  function runFade(updateFn) {
    if (reducedMotion) {
      updateFn();
      return;
    }
    animated.forEach(function (el) {
      el.classList.add("is-hiding");
    });
    window.setTimeout(function () {
      updateFn();
      animated.forEach(function (el) {
        el.classList.remove("is-hiding");
        el.classList.add("is-showing");
      });
      window.requestAnimationFrame(function () {
        animated.forEach(function (el) {
          el.classList.remove("is-showing");
        });
      });
    }, FADE_MS);
  }

  function goTo(index, opts) {
    opts = opts || {};
    var n = SLIDES.length;
    var next = ((index % n) + n) % n;
    if (!opts.force && next === current) return;
    current = next;
    var slide = SLIDES[current];

    if (opts.initial) {
      renderBgPane(activePane, slide);
      applyContent(slide);
    } else if (reducedMotion) {
      swapBgPanes(slide);
      applyContent(slide);
    } else {
      swapBgPanes(slide);
      runFade(function () {
        applyContent(slide);
      });
    }
    setDots(current);
  }

  if (prevBtn) {
    prevBtn.addEventListener("click", function () {
      goTo(current - 1);
    });
  }
  if (nextBtn) {
    nextBtn.addEventListener("click", function () {
      goTo(current + 1);
    });
  }
  dots.forEach(function (dot) {
    dot.addEventListener("click", function () {
      var i = parseInt(dot.getAttribute("data-owners-dot"), 10);
      if (!isNaN(i)) goTo(i);
    });
  });

  root.addEventListener("keydown", function (e) {
    if (e.key === "ArrowLeft") {
      goTo(current - 1);
    } else if (e.key === "ArrowRight") {
      goTo(current + 1);
    }
  });

  if (paneA && paneB) {
    goTo(0, { initial: true, force: true });
  }
})();

