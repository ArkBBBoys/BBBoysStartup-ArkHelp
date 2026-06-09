(function () {
  'use strict';

  const $ = (sel, ctx) => (ctx || document).querySelector(sel);
  const $$ = (sel, ctx) => Array.from((ctx || document).querySelectorAll(sel));
  const doc = document;
  const body = doc.body;
  const html = doc.documentElement;

  let cache = {};

  function refreshCache() {
    cache = {
      navbarToggle: $('#navbarToggle'),
      messagesContainer: $('.messages-container'),
      backToTop: $('#backToTop'),
      filterForm: $('#filterForm'),
      filterPanel: $('#filterPanel'),
      filterToggle: $('#filterToggle'),
      latField: $('#filterLat'),
      lngField: $('#filterLng'),
      useLocationBtn: $('#useLocationBtn'),
      accountTypeInput: $('#accountTypeInput'),
      accountTypeField: $('#accountTypeField'),
      userTypeBtn: $('#userTypeBtn'),
      helperTypeBtn: $('#helperTypeBtn'),
      divisionSelect: $('select[name="division"]'),
      districtSelect: $('select[name="district"]'),
      upazilaSelect: $('#upazilaSelect'),
      searchInput: $('.search-input'),
      hireModal: $('#hireModal'),
      shareBtn: $('.share-btn'),
      favBtns: $$('.fav-btn'),
      starRatings: $$('.star-rating'),
      revealEls: $$('.reveal'),
      lazyImages: $$('img[data-src]'),
      skeletonWrap: $('.skeleton-wrapper'),
    };
  }

  const util = {
    debounce(fn, ms) {
      if (ms === undefined) ms = 300;
      let timer;
      return function (...args) {
        clearTimeout(timer);
        timer = setTimeout(() => fn.apply(this, args), ms);
      };
    },
    throttle(fn, ms) {
      if (ms === undefined) ms = 100;
      let last = 0;
      return function (...args) {
        const now = Date.now();
        if (now - last >= ms) { last = now; fn.apply(this, args); }
      };
    },
    getCSRF() {
      const m = doc.cookie.match(/csrftoken=([^;]+)/);
      return m ? m[1] : '';
    },
    toast(message, type, duration) {
      if (type === undefined) type = 'info';
      if (duration === undefined) duration = 4000;
      let container = $('.toast-container');
      if (!container) {
        container = doc.createElement('div');
        container.className = 'toast-container';
        body.appendChild(container);
      }
      const el = doc.createElement('div');
      el.className = 'toast toast-' + type;
      el.textContent = message;
      container.appendChild(el);
      requestAnimationFrame(() => el.classList.add('toast-visible'));
      setTimeout(() => {
        el.classList.remove('toast-visible');
        el.classList.add('toast-hiding');
        el.addEventListener('transitionend', () => el.remove(), { once: true });
      }, duration);
    },
    async copyToClipboard(text) {
      try {
        await navigator.clipboard.writeText(text);
        util.toast('কপি হয়েছে!', 'success', 2000);
      } catch (e) {
        const ta = doc.createElement('textarea');
        ta.value = text;
        ta.style.position = 'fixed'; ta.style.opacity = '0';
        body.appendChild(ta); ta.select();
        doc.execCommand('copy');
        body.removeChild(ta);
        util.toast('কপি হয়েছে!', 'success', 2000);
      }
    },
    saveToLS(key, val) {
      try { localStorage.setItem(key, JSON.stringify(val)); } catch (e) {}
    },
    loadFromLS(key, fallback) {
      if (fallback === undefined) fallback = null;
      try {
        const v = localStorage.getItem(key);
        return v ? JSON.parse(v) : fallback;
      } catch (e) { return fallback; }
    },
  };

  function initDarkMode() {
    const stored = util.loadFromLS('theme', 'light');
    if (stored === 'dark') html.setAttribute('data-theme', 'dark');
  }

  function initReveal() {
    if (!('IntersectionObserver' in window)) {
      cache.revealEls.forEach(function(el) { el.classList.add('reveal-visible'); });
      return;
    }
    const obs = new IntersectionObserver(
      function(entries) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('reveal-visible');
            obs.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
    );
    cache.revealEls.forEach(function(el) { obs.observe(el); });
  }

  function initStarRating() {
    cache.starRatings.forEach(function(container) {
      const inputs = $$('input[type="radio"]', container);
      const labels = $$('label', container);
      if (!inputs.length) return;
      const refresh = function() {
        const checked = container.querySelector('input:checked');
        const val = checked ? +checked.value : 0;
        labels.forEach(function(l, i) { l.classList.toggle('active', i < val); });
      };
      inputs.forEach(function(input) {
        input.addEventListener('change', refresh);
        input.addEventListener('mouseenter', function() {
          labels.forEach(function(l, i) {
            l.style.color = i < +this.value ? '#FF8F00' : '';
          }.bind(this));
        });
        input.addEventListener('mouseleave', function() {
          labels.forEach(function(l) { l.style.color = ''; });
          refresh();
        });
      });
      refresh();
    });
  }

  function initNotifications() {
    if (!cache.messagesContainer) return;
    cache.messagesContainer.querySelectorAll('.message').forEach(function(el) {
      setTimeout(function() {
        el.style.opacity = '0';
        el.style.transform = 'translateX(100%)';
        el.addEventListener('transitionend', function() { el.remove(); }, { once: true });
      }, 5000);
    });
  }

  function openModal(id) {
    const m = $('#' + id);
    if (!m) return;
    m.classList.add('active');
    body.style.overflow = 'hidden';
  }

  function closeModal(id) {
    const m = $('#' + id);
    if (!m) return;
    m.classList.remove('active');
    body.style.overflow = '';
  }

  function initModalDismiss() {
    doc.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        $$('.modal.active').forEach(function(m) {
          m.classList.remove('active');
          body.style.overflow = '';
        });
      }
    });
    $$('.modal').forEach(function(m) {
      m.addEventListener('click', function(e) {
        if (e.target === m) {
          m.classList.remove('active');
          body.style.overflow = '';
        }
      });
    });
  }

  function initCascadingDropdowns() {
    const divSel = cache.divisionSelect;
    const distSel = cache.districtSelect;
    if (!divSel || !distSel) return;
    divSel.addEventListener('change', function() {
      const val = divSel.value;
      distSel.innerHTML = '<option value="">জেলা নির্বাচন করুন</option>';
      const districts = getDistrictsByDivision(val);
      districts.forEach(function(d) {
        const opt = doc.createElement('option');
        opt.value = d[0]; opt.textContent = d[1];
        distSel.appendChild(opt);
      });
      if (cache.upazilaSelect) {
        cache.upazilaSelect.innerHTML = '<option value="">উপজেলা নির্বাচন করুন</option>';
      }
    });
  }

  function cascadeDistricts() {
    const division = cache.divisionSelect ? cache.divisionSelect.value : '';
    const distSel = cache.districtSelect;
    const upaSel = cache.upazilaSelect;
    if (!distSel) return;
    if (!division) {
      distSel.innerHTML = '<option value="">সব জেলা</option>';
      if (upaSel) upaSel.innerHTML = '<option value="">সব উপজেলা</option>';
      return;
    }
    fetch('/ajax/districts/?division=' + encodeURIComponent(division))
      .then(function(r) { return r.json(); })
      .then(function(data) {
        distSel.innerHTML = '<option value="">সব জেলা</option>';
        data.districts.forEach(function(d) {
          const opt = doc.createElement('option');
          opt.value = d.code; opt.textContent = d.name;
          distSel.appendChild(opt);
        });
        if (upaSel) upaSel.innerHTML = '<option value="">সব উপজেলা</option>';
      });
  }

  function cascadeUpazilas() {
    const district = cache.districtSelect ? cache.districtSelect.value : '';
    const upaSel = cache.upazilaSelect;
    if (!upaSel) return;
    if (!district) {
      upaSel.innerHTML = '<option value="">সব উপজেলা</option>';
      return;
    }
    fetch('/ajax/upazilas/?district=' + encodeURIComponent(district))
      .then(function(r) { return r.json(); })
      .then(function(data) {
        upaSel.innerHTML = '<option value="">সব উপজেলা</option>';
        data.upazilas.forEach(function(u) {
          const opt = doc.createElement('option');
          opt.value = u.code; opt.textContent = u.name;
          upaSel.appendChild(opt);
        });
      });
  }

  function removeParam(key, url) {
    const u = new URL(url, window.location.origin);
    u.searchParams.delete(key);
    u.searchParams.delete('district');
    u.searchParams.delete('upazila');
    return u.toString();
  }

  function getDistrictsByDivision(division) {
    var districts = {
      dhaka: [['dhaka','ঢাকা'],['faridpur','ফরিদপুর'],['gazipur','গাজীপুর'],['gopalganj','গোপালগঞ্জ'],['jamalpur','জামালপুর'],['kishoreganj','কিশোরগঞ্জ'],['madaripur','মাদারীপুর'],['manikganj','মানিকগঞ্জ'],['munshiganj','মুন্সিগঞ্জ'],['narayanganj','নারায়ণগঞ্জ'],['narsingdi','নরসিংদী'],['netrokona','নেত্রকোণা'],['rajbari','রাজবাড়ী'],['shariatpur','শরীয়তপুর'],['sherpur','শেরপুর'],['tangail','টাঙ্গাইল']],
      chittagong: [['bandarban','বান্দরবন'],['brahmanbaria','ব্রাহ্মণবাড়ীয়া'],['chandpur','চাঁদপুর'],['chittagong','চট্টগ্রাম'],['comilla','কুমিল্লা'],['cox_bazar','কক্সবাজার'],['feni','ফেনী'],['khagrachari','খাগড়াছড়ি'],['lakshmipur','লক্ষ্মীপুর'],['noakhali','নোয়াখালী'],['rangamati','রাঙ্গামাটি']],
      rajshahi: [['bogra','বগুড়া'],['chapainawabganj','চাঁপাইনবাবগঞ্জ'],['jaipurhat','জয়পুরহাট'],['naogaon','নওগাঁ'],['natore','নাটোর'],['pabna','পাবনা'],['rajshahi','রাজশাহী'],['sirajganj','সিরাজগঞ্জ']],
      khulna: [['bagerhat','বাগেরহাট'],['chuadanga','চুয়াডাঙ্গা'],['jessore','যশোর'],['jhenaidah','ঝিনাইদহ'],['khulna','খুলনা'],['kustia','কুষ্টিয়া'],['magura','মাগুরা'],['meherpur','মেহেরপুর'],['narail','নড়াইল'],['satkhira','সাতক্ষীরা']],
      barisal: [['barguna','বরগুনা'],['barisal','বরিশাল'],['bhola','ভোলা'],['jhalokati','ঝালকাঠী'],['patuakhali','পটুয়াখালী'],['pirojpur','পিরোজপুর']],
      sylhet: [['habiganj','হবিগঞ্জ'],['moulvibazar','মৌলভীবাজার'],['sunamganj','সুনামগঞ্জ'],['sylhet','সিলেট']],
      rangpur: [['dinajpur','দিনাজপুর'],['gaibandha','গাইবান্ধা'],['kurigram','কুড়িগ্রাম'],['lalmonirhat','লালমনিরহাট'],['nilphamari','নীলফামারী'],['panchagarh','পঞ্চগড়'],['rangpur','রংপুর'],['thakurgaon','ঠাকুরগাঁও']],
      mymensingh: [['jamalpur','জামালপুর'],['mymensingh','ময়মনসিংহ'],['netrokona','নেত্রকোণা'],['sherpur','শেরপুর']],
    };
    return districts[division] || [];
  }

  function getUpazilasByDistrict(district) {
    var upazilas = {
      dhaka:[['dhaka_sadar','ঢাকা সদর'],['savar','সাভার'],['dohar','দোহার'],['keraniganj','কেরানীগঞ্জ']],
      gazipur:[['gazipur_sadar','গাজীপুর সদর'],['tongi','টঙ্গী'],['sreepur','শ্রীপুর'],['kaliganj','কালীগঞ্জ'],['kapasia','কাপাসিয়া']],
      tangail:[['tangail_sadar','টাঙ্গাইল সদর'],['sakhipur','সখিপুর'],['basail','বাসাইল'],['dhanbari','ধানবাড়ী'],['gopalpur','গোপালপুর'],['madhupur','মধুপুর']],
      chittagong:[['chittagong_sadar','চট্টগ্রাম সদর'],['pahartali','পাহাড়তলী'],['banskali','বাঁশখালী'],['sitakunda','সীতাকুণ্ড'],['rangunia','রাঙ্গুনিয়া'],['hathazari','হাটহাজারী'],['patiya','পটিয়া'],['mirsharai','মীরসরাই']],
      comilla:[['comilla_sadar','কুমিল্লা সদর'],['chandina','চন্দিনা'],['daudkandi','দাউদকান্দি'],['laksam','লাকসাম'],['nangalkot','নাঙ্গলকোট']],
      cox_bazar:[['cox_bazar_sadar','কক্সবাজার সদর'],['ramu','রামু'],['moheshkhali','মহেশখালী'],['chakaria','চকরিয়া'],['ukhiya','উখিয়া'],['teknaf','টেকনাফ']],
      noakhali:[['noakhali_sadar','নোয়াখালী সদর'],['companiganj','কোম্পানীগঞ্জ'],['begumganj','বেগমগঞ্জ'],['hatiya','হাতিয়া']],
      feni:[['feni_sadar','ফেনী সদর'],['parshuram','পরশুরাম'],['daganbhuiyan','দাগনভূঁইয়া']],
      rajshahi:[['rajshahi_sadar','রাজশাহী সদর'],['paba','পবা'],['durgapur','দুর্গাপুর'],['bagmara','বাগমারা']],
      bogra:[['bogra_sadar','বগুড়া সদর'],['sariakandi','সারিয়াকান্দি'],['shajahanpur','শাজাহানপুর'],['gabtali','গাবতলী']],
      pabna:[['pabna_sadar','পাবনা সদর'],['ishwardi','ঈশ্বরদী'],['sujanagar','সুজানগর'],['santhiya','সাঁথিয়া']],
      khulna:[['khulna_sadar','খুলনা সদর'],['dighalia','দিঘলিয়া'],['phultala','ফুলতলা'],['rupsha','রূপসা']],
      jessore:[['jessore_sadar','যশোর সদর'],['bagherpara','বাঘেরপাড়া'],['chowgacha','চৌগাছা'],['jhikargacha','ঝিকরগাছা']],
      satkhira:[['satkhira_sadar','সাতক্ষীরা সদর'],['kalaroa','কালারোয়া'],['tala','তালা'],['assassuni','আশাশুনি']],
      sylhet:[['sylhet_sadar','সিলেট সদর'],['balaganj','বালাগঞ্জ'],['beanibazar','বিয়ানীবাজার'],['golapganj','গোলাপগঞ্জ']],
      moulvibazar:[['moulvibazar_sadar','মৌলভীবাজার সদর'],['sreemangal','শ্রীমঙ্গল'],['kamalganj','কমলগঞ্জ'],['rajnagar','রাজনগর']],
      mymensingh:[['mymensingh_sadar','ময়মনসিংহ সদর'],['fulpur','ফুলপুর'],['muktagacha','মুক্তাগাছা'],['trishal','ত্রিশাল']],
      barisal:[['barisal_sadar','বরিশাল সদর'],['bakerganj','বাকেরগঞ্জ'],['gournadi','গৌরনদী'],['babuganj','বাবুগঞ্জ']],
      bhola:[['bhola_sadar','ভোলা সদর'],['char_fassion','চরফ্যাশন'],['monpura','মনপুরা'],['lalmohan','লালমোহন']],
      rangpur:[['rangpur_sadar','রংপুর সদর'],['badarganj','বদরগঞ্জ'],['gangachara','গঙ্গাচরা'],['taraganj','তারাগঞ্জ']],
      dinajpur:[['dinajpur_sadar','দিনাজপুর সদর'],['birganj','বীরগঞ্জ'],['parbatipur','পার্বতীপুর'],['biral','বিরল']],
    };
    return upazilas[district] || [];
  }

  function initAutoFilterSubmit() {
    const isDesktop = window.innerWidth >= 768;
    if (!isDesktop) return;
    $$('.filter-select').forEach(function(sel) {
      sel.addEventListener('change', function() {
        const form = sel.closest('form');
        if (form) form.submit();
      });
    });
  }

  function onFilterChange() {
    const form = $('#filterForm');
    if (form) form.submit();
  }

  function toggleFilters() {
    if (cache.filterPanel) cache.filterPanel.classList.toggle('active');
    if (cache.filterToggle) cache.filterToggle.classList.toggle('active');
  }

  function detectLocation() {
    const btn = cache.useLocationBtn;
    if (!btn) return;
    btn.innerHTML = 'অবস্থান খোঁজা হচ্ছে...';
    btn.disabled = true;
    if (!navigator.geolocation) {
      btn.innerHTML = 'জিওলোকেশন সমর্থিত নয়';
      btn.disabled = false;
      return;
    }
    navigator.geolocation.getCurrentPosition(
      function(pos) {
        window.location.href = '/helpers/?lat=' + pos.coords.latitude + '&lng=' + pos.coords.longitude;
      },
      function() {
        btn.innerHTML = 'অবস্থান পাওয়া যায়নি';
        btn.disabled = false;
        setTimeout(function() { btn.innerHTML = 'আমার অবস্থান ব্যবহার করুন'; }, 2000);
      },
      { enableHighAccuracy: true, timeout: 8000, maximumAge: 60000 }
    );
  }

  function detectAndRedirect(url) {
    if (!navigator.geolocation) { window.location.href = url; return; }
    navigator.geolocation.getCurrentPosition(
      function(pos) {
        var sep = url.indexOf('?') > -1 ? '&' : '?';
        window.location.href = url + sep + 'lat=' + pos.coords.latitude + '&lng=' + pos.coords.longitude;
      },
      function() { window.location.href = url; },
      { enableHighAccuracy: true, timeout: 8000, maximumAge: 60000 }
    );
  }

  function initLocationDetection() {
    if (cache.latField && cache.lngField && cache.latField.value && cache.lngField.value) {
      const notice = $('.filter-notice');
      if (notice) notice.style.display = 'flex';
    }
  }

  function initFavorites() {
    const favs = util.loadFromLS('favorites', []);
    const sync = function() {
      cache.favBtns.forEach(function(btn) {
        const id = btn.dataset.helperId;
        btn.classList.toggle('active', favs.indexOf(id) > -1);
        btn.setAttribute('aria-label', favs.indexOf(id) > -1 ? 'ফেভারিট থেকে সরান' : 'ফেভারিটে যোগ করুন');
      });
    };
    cache.favBtns.forEach(function(btn) {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        const id = btn.dataset.helperId;
        if (!id) return;
        const idx = favs.indexOf(id);
        if (idx > -1) { favs.splice(idx, 1); } else { favs.push(id); }
        util.saveToLS('favorites', favs);
        sync();
      });
    });
    sync();
  }

  function initShare() {
    if (!cache.shareBtn) return;
    cache.shareBtn.addEventListener('click', async function(e) {
      e.preventDefault();
      const data = {
        title: cache.shareBtn.dataset.shareTitle || 'Khujo',
        text: cache.shareBtn.dataset.shareText || 'এই হেল্পারটি দেখুন',
        url: cache.shareBtn.dataset.shareUrl || window.location.href,
      };
      if (navigator.share) {
        try { await navigator.share(data); } catch (e) {}
      } else {
        util.copyToClipboard(data.url);
      }
    });
  }

  function initSmoothScroll() {
    doc.addEventListener('click', function(e) {
      const a = e.target.closest('a[href^="#"]');
      if (!a) return;
      const id = a.getAttribute('href').slice(1);
      if (!id) return;
      const target = doc.getElementById(id);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  }

  function initDebouncedSearch() {
    if (!cache.searchInput) return;
    const handler = util.debounce(function() {
      const form = this.closest('form');
      if (form) form.submit();
    }, 300);
    cache.searchInput.addEventListener('input', handler);
  }

  function initAdTracking() {
    $$('[data-ad-id]').forEach(function(el) {
      const id = el.dataset.adId;
      if (id && navigator.sendBeacon) {
        navigator.sendBeacon('/ads/track/impression/' + id + '/');
      }
    });
  }

  function initLazyImages() {
    if (!('IntersectionObserver' in window)) {
      cache.lazyImages.forEach(function(img) {
        if (img.dataset.src) img.src = img.dataset.src;
        if (img.dataset.srcset) img.srcset = img.dataset.srcset;
      });
      return;
    }
    const obs = new IntersectionObserver(
      function(entries) {
        entries.forEach(function(entry) {
          if (!entry.isIntersecting) return;
          const img = entry.target;
          if (img.dataset.src) { img.src = img.dataset.src; img.removeAttribute('data-src'); }
          if (img.dataset.srcset) { img.srcset = img.dataset.srcset; img.removeAttribute('data-srcset'); }
          img.classList.add('lazy-loaded');
          obs.unobserve(img);
        });
      },
      { rootMargin: '200px 0px' }
    );
    cache.lazyImages.forEach(function(img) { obs.observe(img); });
  }

  function initSkeletonLoader() {
    if (!cache.skeletonWrap) return;
    requestAnimationFrame(function() {
      cache.skeletonWrap.querySelectorAll('.skeleton').forEach(function(el) {
        el.classList.add('skeleton-loading');
      });
    });
    window.addEventListener('load', function() {
      cache.skeletonWrap.querySelectorAll('.skeleton').forEach(function(el) {
        el.classList.remove('skeleton-loading');
        el.classList.add('skeleton-loaded');
      });
    });
  }

  function initClipboardTriggers() {
    doc.addEventListener('click', function(e) {
      const trigger = e.target.closest('[data-copy]');
      if (!trigger) return;
      util.copyToClipboard(trigger.dataset.copy);
    });
  }

  function initBackToTop() {
    if (!cache.backToTop) return;
    const handler = util.throttle(function() {
      cache.backToTop.classList.toggle('visible', window.scrollY > 400);
    }, 100);
    window.addEventListener('scroll', handler, { passive: true });
    cache.backToTop.addEventListener('click', function(e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  function init() {
    refreshCache();
    initDarkMode();
    initReveal();
    initStarRating();
    initNotifications();
    initModalDismiss();
    initCascadingDropdowns();
    initAutoFilterSubmit();
    initLocationDetection();
    initFavorites();
    initShare();
    initSmoothScroll();
    initDebouncedSearch();
    initAdTracking();
    initLazyImages();
    initSkeletonLoader();
    initClipboardTriggers();
    initBackToTop();

    var divSel = cache.divisionSelect;
    var distSel = cache.districtSelect;
    if (divSel) { divSel.addEventListener('change', cascadeDistricts); }
    if (distSel) { distSel.addEventListener('change', cascadeUpazilas); }
  }

  if (doc.readyState === 'loading') {
    doc.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  window.openModal = openModal;
  window.closeModal = closeModal;
  window.trackAdClick = function trackAdClick(id) {
    fetch('/ads/track/click/' + id + '/', {
      method: 'POST',
      headers: { 'X-CSRFToken': util.getCSRF() },
    })
      .then(function(r) { return r.json(); })
      .then(function(data) { if (data.redirect) window.location.href = data.redirect; });
  };
  window.closeAd = function closeAd(id) {
    var p = $('#adPopup' + id);
    if (p) {
      p.style.animation = 'adFadeOut 0.3s ease forwards';
      p.addEventListener('animationend', function() { p.style.display = 'none'; }, { once: true });
    }
  };
  window.detectLocation = detectLocation;
  window.detectAndRedirect = detectAndRedirect;
  window.setAccountType = function setAccountType(type) {
    if (cache.accountTypeInput) cache.accountTypeInput.value = type;
    if (cache.accountTypeField) cache.accountTypeField.value = type;
    if (cache.userTypeBtn) cache.userTypeBtn.classList.toggle('active', type === 'user');
    if (cache.helperTypeBtn) cache.helperTypeBtn.classList.toggle('active', type === 'helper');
  };
  window.toggleFilters = toggleFilters;
  window.onFilterChange = onFilterChange;
  window.cascadeDistricts = cascadeDistricts;
  window.cascadeUpazilas = cascadeUpazilas;
  window.removeParam = removeParam;
  window.getDistrictsByDivision = getDistrictsByDivision;
  window.getUpazilasByDistrict = getUpazilasByDistrict;
  window.toast = util.toast;
  window.copyToClipboard = util.copyToClipboard;

})();