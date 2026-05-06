(function () {
  var root = document.getElementById("resorts-carousel");
  var mount = document.getElementById("resorts-carousel-mount");
  if (!root || !mount) return;

  var RESORTS_DATA = {
    orlando: [
      {
        layout: "overview",
        image: "public/resorts-carousel/orlando-0.png",
        title: "Summer Bay Orlando",
        subtitle: "By Exploria Resorts",
        lead:
          "Discover the ultimate escape at Summer Bay Orlando! This luxury resort blends the excitement of Orlando's world-famous attractions with the relaxation of a premier Vacation.",
        body:
          "Spanning 400 acres of lush landscapes and featuring a stunning 64-acre spring-fed lake, Summer Bay Resort offers something for everyone—near all the area attractions.",
      },
      {
        layout: "accommodations",
        image: "public/resorts-carousel/orlando-1.png",
        kicker: "Accommodations",
        unitTitle: "One Bedroom",
        body:
          "Our 1-bedroom condo is ideal for a small family, offering both space and comfort. It features a queen bed and a sofa sleeper, a full kitchen for home-cooked meals, a washer and dryer for convenience, and a flat-screen TV for entertainment.",
        amenities: [
          "Queen Bed",
          "Capacity: 4",
          "Sofa Bed",
          "Full kitchen",
          "Flat Screen TV",
          "Washer and Dryer",
        ],
      },
      {
        layout: "bonus",
        image: "public/resorts-carousel/orlando-2.png",
        kicker: "Bonus Gift",
        sub: "Bonus $100 Resort Credit or $100 Ticket Credit",
        body:
          "Your stay includes a $100 Resort Credit or $100 Ticket Credit, your choice. Use it to extend the experience on property or explore everything Orlando has to offer. Summer Bay Orlando puts you at the center of it all, and your bonus credit makes sure every moment counts. Because the best vacations aren't just trips, they're the memories your family talks about for years.",
      },
      {
        layout: "things",
        image: "public/resorts-carousel/orlando-3.png",
        kicker: "Things To Do",
        items: [
          {
            bold: "Disney Springs –",
            text: " Shop, dine, and enjoy world-class entertainment at this lively waterfront district.",
          },
          {
            bold: "Animal Kingdom –",
            text: " Explore exotic wildlife, thrilling rides, and breathtaking landscapes.",
          },
          {
            bold: "Universal Orlando Resort –",
            text: " Experience blockbuster attractions, thrilling roller coasters, and The Wizarding World of Harry Potter™.",
          },
          {
            bold: "SeaWorld Orlando –",
            text: " Get up close with marine life, enjoy exciting shows, and ride adrenaline-pumping coasters.",
          },
        ],
      },
    ],
    daytona: [
      {
        layout: "overview",
        image: "public/resorts-carousel/daytona-0.png",
        title: "Grand Seas Resort",
        subtitle: "By Exploria Resorts",
        lead:
          "Grand Seas offers vacationers a beachfront destination resort conveniently located near the Daytona International Speedway and Ocean Walk Village.",
        body:
          "Your Florida beach getaway to Grand Seas offers an array of comfortable floor-plans to provide the backdrop for memorable and relaxing moments in your home away from home.",
      },
      {
        layout: "accommodations",
        image: "public/resorts-carousel/daytona-1.png",
        kicker: "Accommodations",
        unitTitle: "1-Bedroom Oceanfront Bahama Condo",
        body:
          "Grand Seas By Exploria Resorts 1 bedroom oceanfront condo features a private bedroom with queen bed and a queen size sleeper sofa in the living area. These accommodations are appointed with vibrant colors and feature full kitchens, air jetted tubs, and beachfront views.",
        amenities: [
          "1 Queen bed",
          "2 Twin Beds",
          "Sofa Bed",
          "Full kitchen",
          "Flat Screen TV",
          "Washer and Dryer",
        ],
      },
      {
        layout: "bonus",
        image: "public/resorts-carousel/daytona-2.png",
        kicker: "Bonus Gift",
        sub: "Bonus $100 Resort Credit or $100 Ticket Credit",
        body:
          "Your stay includes a $100 Resort Credit or $100 Ticket Credit, your choice. Put it toward resort amenities or local attractions along the coast. With Daytona's beaches and energy right outside your door, your bonus credit stretches your vacation further than you'd expect. From sunrise on the sand to evenings spent together, every detail is designed to become a memory worth keeping.",
      },
      {
        layout: "things",
        image: "public/resorts-carousel/daytona-3.png",
        kicker: "Things To Do",
        items: [
          {
            bold: "\"World's Most Famous Beach\" –",
            text: " Daytona Beach offers convenient beach access with multiple entry points.",
          },
          {
            bold: "Drinks with an Ocean View –",
            text: " Enjoy refreshing cocktails and stunning beachfront views of the Atlantic.",
          },
          {
            bold: "The Beachside Cafe –",
            text: " Experience blockbuster attractions, thrilling roller coasters, and The Wizarding World of Harry Potter™.",
          },
          {
            bold: "Daytona International –",
            text: " Daytona International Speedway is a legendary 2.5-mile racetrack famous for hosting the Daytona 500.",
          },
        ],
      },
    ],
    poconos: [
      {
        layout: "overview",
        image: "public/resorts-carousel/poconos-0.png",
        title: "Pocono Mountain Villas",
        subtitle: "By Exploria Resorts",
        lead:
          "Escape to the beauty of the Pocono Mountains at Pocono Mountain Villas by Exploria Resorts! Nestled in a breathtaking natural setting, this resort is a short drive from top regional attractions.",
        body:
          "From zipping through the mountain tree tops, experiencing the thrill of year-round tubing at lightning speeds, and tee-ing up for the par-fect golf game, enjoy new experiences every day during your stay.",
      },
      {
        layout: "accommodations",
        image: "public/resorts-carousel/poconos-1.png",
        kicker: "Accommodations",
        unitTitle: "1-Bedroom Condo with Fireplace",
        body:
          "1-bedroom units have a queen bed in the bedroom and a sofa sleeper in the living room. The units also have a full kitchen. This unit can be booked with a 'Tree Tops Studio' to lock-off into a 2-bedroom unit. All units are multi-story with interior stairs.",
        amenities: [
          "Queen Bed",
          "Washer/dryer",
          "Sofa Bed",
          "Full kitchen",
          "Cable TV/DVD",
          "Coffee/Tea maker",
        ],
      },
      {
        layout: "bonus",
        image: "public/resorts-carousel/poconos-2.png",
        kicker: "Bonus Gift",
        kickerTone: "orange",
        sub: "Bonus 4 Waterpark or Zipline Tickets",
        body:
          "Your stay includes 4 Waterpark Passes or 4 Zipline Tickets, your choice. More adventure is built right into your getaway. Nestled in the heart of the Pocono Mountains, your bonus tickets turn a great escape into an unforgettable one. Whether you're splashing through the waterpark or soaring above the treetops, these are the moments your family will never forget.",
      },
      {
        layout: "things",
        image: "public/resorts-carousel/poconos-3.png",
        kicker: "Things To Do",
        items: [
          {
            bold: "The Warehouse Tavern & Grill –",
            text: " Enjoy  gourmet burgers, steaks, seafood, artisanal pizzas, and live music!",
          },
          {
            bold: "Blue Lightning Tubing  –",
            text: " The attraction includes a Magic Carpet lift with two 400 foot tubing lanes.",
          },
          {
            bold: "The Pocono Hills Golf Course –",
            text: " The 18-hole par-71 golf course is recognized for its challenging greens and rolling fairways.",
          },
          {
            bold: "Bushkill Riding Stables –",
            text: " Take a trail ride back in time through the scenic Pocono Mountains. Open year-round, what better way to enjoy the mountain views then on the back of a horse.",
          },
        ],
      },
    ],
  };

  function starsHtml() {
    return (
      '<div class="resorts-carousel__stars">' +
      '<span class="resorts-carousel__star"><img src="public/star1.svg" alt="" /></span>' +
      '<span class="resorts-carousel__star"><img src="public/star3.svg" alt="" /></span>' +
      '<span class="resorts-carousel__star"><img src="public/star5.svg" alt="" /></span>' +
      '<span class="resorts-carousel__star"><img src="public/star7.svg" alt="" /></span>' +
      '<span class="resorts-carousel__star resorts-carousel__star--half"><img src="public/star9.svg" alt="" /></span>' +
      "</div>"
    );
  }

  function amenitiesHtml(list) {
    return (
      '<div class="resorts-carousel__amenities">' +
      list
        .map(function (a) {
          return '<span class="resorts-carousel__amenity">' + a + "</span>";
        })
        .join("") +
      "</div>"
    );
  }

  function logoHtml() {
    return (
      '<div class="resorts-carousel__brand">' +
      '<img src="public/logo0.png" alt="" class="resorts-carousel__brand-logo" width="133" height="41" />' +
      "</div>"
    );
  }

  var SLIDE_CHROME_MEDIA =
    "resorts-carousel__photo-wrap resorts-carousel__photo-wrap--framed";
  var SLIDE_CHROME_PANEL =
    "resorts-carousel__copy-panel resorts-carousel__copy-panel--cream";
  var SLIDE_CHROME_INNER =
    "resorts-carousel__copy-inner resorts-carousel__copy-inner--bordered";

  function ctaHtml() {
    return (
      '<div class="resorts-carousel__cta">' +
      '<div class="resorts-carousel__cta-inner">' +
      '<span class="resorts-carousel__cta-text">RESERVE NOW</span>' +
      "</div></div>"
    );
  }

  function renderOverview(region, d) {
    var accent = " resorts-carousel__accent-bar--orange";
    return (
      '<div class="resorts-carousel__step">' +
      '<div class="' +
      SLIDE_CHROME_MEDIA +
      '">' +
      '<img class="resorts-carousel__photo" src="' +
      d.image +
      '" alt="" />' +
      "</div>" +
      '<div class="' +
      SLIDE_CHROME_PANEL +
      '">' +
      '<div class="' +
      SLIDE_CHROME_INNER +
      '">' +
      '<div class="resorts-carousel__preview">' +
      '<div class="resorts-carousel__headline-block">' +
      '<div class="resorts-carousel__title">' +
      d.title +
      "</div>" +
      '<div class="resorts-carousel__subtitle">' +
      d.subtitle +
      "</div>" +
      "</div>" +
      starsHtml() +
      '<div class="resorts-carousel__lead-row">' +
      '<div class="resorts-carousel__accent-bar ' +
      accent +
      '"></div>' +
      '<p class="resorts-carousel__lead">' +
      d.lead +
      "</p>" +
      "</div>" +
      '<p class="resorts-carousel__body">' +
      d.body +
      "</p>" +
      "</div>" +
      ctaHtml() +
      "</div></div></div>"
    );
  }

  function renderAccommodations(region, d) {
    var kickerCls = "resorts-carousel__kicker";
    if (d.kickerTone === "orange") kickerCls += " resorts-carousel__kicker--orange";
    return (
      '<div class="resorts-carousel__step">' +
      '<div class="' +
      SLIDE_CHROME_MEDIA +
      '">' +
      '<img class="resorts-carousel__photo" src="' +
      d.image +
      '" alt="" />' +
      "</div>" +
      '<div class="' +
      SLIDE_CHROME_PANEL +
      '">' +
      '<div class="' +
      SLIDE_CHROME_INNER +
      '">' +
      '<div class="resorts-carousel__preview resorts-carousel__preview--spaced">' +
      logoHtml() +
      '<div class="' +
      kickerCls +
      '">' +
      d.kicker +
      "</div>" +
      '<div class="resorts-carousel__unit-title">' +
      d.unitTitle +
      "</div>" +
      '<p class="resorts-carousel__body resorts-carousel__body--acc">' +
      d.body +
      "</p>" +
      amenitiesHtml(d.amenities) +
      "</div>" +
      ctaHtml() +
      "</div></div></div>"
    );
  }

  function renderBonus(region, d) {
    var kickerCls = "resorts-carousel__kicker";
    if (d.kickerTone === "orange") kickerCls += " resorts-carousel__kicker--orange";
    return (
      '<div class="resorts-carousel__step">' +
      '<div class="' +
      SLIDE_CHROME_MEDIA +
      '">' +
      '<img class="resorts-carousel__photo" src="' +
      d.image +
      '" alt="" />' +
      "</div>" +
      '<div class="' +
      SLIDE_CHROME_PANEL +
      '">' +
      '<div class="' +
      SLIDE_CHROME_INNER +
      '">' +
      '<div class="resorts-carousel__preview resorts-carousel__preview--spaced">' +
      logoHtml() +
      '<div class="' +
      kickerCls +
      '">' +
      d.kicker +
      "</div>" +
      '<div class="resorts-carousel__bonus-sub">' +
      d.sub +
      "</div>" +
      '<p class="resorts-carousel__body">' +
      d.body +
      "</p>" +
      "</div>" +
      ctaHtml() +
      "</div></div></div>"
    );
  }

  function renderThings(region, d) {
    var kickerCls = "resorts-carousel__kicker";
    if (d.kickerTone === "orange") kickerCls += " resorts-carousel__kicker--orange";
    var items = d.items
      .map(function (it) {
        return (
          '<p class="resorts-carousel__thing">' +
          "<strong>" +
          it.bold +
          "</strong>" +
          it.text +
          "</p>"
        );
      })
      .join("");
    return (
      '<div class="resorts-carousel__step">' +
      '<div class="' +
      SLIDE_CHROME_MEDIA +
      '">' +
      '<img class="resorts-carousel__photo" src="' +
      d.image +
      '" alt="" />' +
      "</div>" +
      '<div class="' +
      SLIDE_CHROME_PANEL +
      '">' +
      '<div class="' +
      SLIDE_CHROME_INNER +
      '">' +
      '<div class="resorts-carousel__preview resorts-carousel__preview--spaced">' +
      logoHtml() +
      '<div class="' +
      kickerCls +
      '">' +
      d.kicker +
      "</div>" +
      '<div class="resorts-carousel__things-list">' +
      items +
      "</div>" +
      "</div>" +
      ctaHtml() +
      "</div></div></div>"
    );
  }

  function renderHtml(region, index) {
    var d = RESORTS_DATA[region][index];
    if (d.layout === "overview") return renderOverview(region, d);
    if (d.layout === "accommodations") return renderAccommodations(region, d);
    if (d.layout === "bonus") return renderBonus(region, d);
    if (d.layout === "things") return renderThings(region, d);
    return "";
  }

  function render(region, index) {
    mount.innerHTML = renderHtml(region, index);
  }

  var regionsList = ["orlando", "daytona", "poconos"];

  function measureMaxSlideHeight(widthPx) {
    var probe = document.createElement("div");
    probe.setAttribute("aria-hidden", "true");
    probe.style.cssText =
      "position:absolute;left:-99999px;top:0;visibility:hidden;width:" +
      widthPx +
      "px;pointer-events:none;box-sizing:border-box;";
    document.body.appendChild(probe);
    var maxH = 0;
    for (var r = 0; r < regionsList.length; r++) {
      for (var i = 0; i < 4; i++) {
        probe.innerHTML = renderHtml(regionsList[r], i);
        var step = probe.querySelector(".resorts-carousel__step");
        if (step) maxH = Math.max(maxH, step.offsetHeight);
      }
    }
    document.body.removeChild(probe);
    return maxH;
  }

  var mountMinHeightRaf = 0;
  function updateMountMinHeight() {
    var w = mount.offsetWidth;
    if (!w) return;
    var h = measureMaxSlideHeight(w);
    if (h > 0) mount.style.minHeight = h + "px";
  }

  function scheduleMountMinHeight() {
    if (mountMinHeightRaf) cancelAnimationFrame(mountMinHeightRaf);
    mountMinHeightRaf = requestAnimationFrame(function () {
      mountMinHeightRaf = 0;
      updateMountMinHeight();
    });
  }

  var region = "orlando";
  var index = 0;

  var tabs = root.querySelectorAll("[data-resorts-tab]");
  var prevBtn = root.querySelector("[data-resorts-prev]");
  var nextBtn = root.querySelector("[data-resorts-next]");
  var dots = root.querySelectorAll("[data-resorts-dot]");

  function syncChrome() {
    root.setAttribute("data-active-region", region);
    root.setAttribute("data-active-index", String(index));
    root.classList.remove(
      "resorts-carousel--orlando",
      "resorts-carousel--daytona",
      "resorts-carousel--poconos"
    );
    root.classList.add("resorts-carousel--" + region);

    tabs.forEach(function (tab) {
      var on = tab.getAttribute("data-resorts-tab") === region;
      tab.classList.toggle("is-active", on);
      tab.setAttribute("aria-selected", on ? "true" : "false");
    });

    dots.forEach(function (dot, i) {
      dot.classList.toggle("is-active", i === index);
      dot.setAttribute("aria-current", i === index ? "true" : "false");
    });

    render(region, index);
  }

  function go(delta) {
    index = (index + delta + 4) % 4;
    syncChrome();
  }

  function setRegion(r) {
    region = r;
    index = 0;
    syncChrome();
  }

  tabs.forEach(function (tab) {
    tab.addEventListener("click", function () {
      setRegion(tab.getAttribute("data-resorts-tab"));
    });
  });

  if (prevBtn) prevBtn.addEventListener("click", function () { go(-1); });
  if (nextBtn) nextBtn.addEventListener("click", function () { go(1); });

  dots.forEach(function (dot, i) {
    dot.addEventListener("click", function () {
      index = i;
      syncChrome();
    });
  });

  var layoutDebounce = 0;
  function debouncedScheduleMountMinHeight() {
    clearTimeout(layoutDebounce);
    layoutDebounce = setTimeout(scheduleMountMinHeight, 100);
  }

  window.addEventListener("resize", debouncedScheduleMountMinHeight);

  if (typeof ResizeObserver !== "undefined") {
    try {
      var ro = new ResizeObserver(debouncedScheduleMountMinHeight);
      ro.observe(mount);
    } catch (e) {}
  }

  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(scheduleMountMinHeight);
  }

  window.addEventListener("load", scheduleMountMinHeight);

  syncChrome();
  scheduleMountMinHeight();
})();
