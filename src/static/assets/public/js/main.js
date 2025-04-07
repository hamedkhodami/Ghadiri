


document.addEventListener('DOMContentLoaded', () => {
    const categoryButtons = document.querySelectorAll('.btn-category');

    // انتخاب دکمه اول و فعال کردن آن
    const firstButton = categoryButtons[0];
    firstButton.classList.add('active');

    // نمایش تصاویر مربوط به دسته اول
    const firstCategoryId = firstButton.getAttribute('category-id');
    displayImages(firstCategoryId);

    categoryButtons.forEach(button => {
        button.addEventListener('click', () => {
            // حذف کلاس‌های فعال از تمامی دکمه‌ها
            categoryButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            const categoryId = button.getAttribute('category-id');
            displayImages(categoryId);
        });
    });

    function displayImages(categoryId) {
        const gridItems = document.querySelectorAll(".course-card");
        const gridContainer = document.querySelector('.grid-container');

        // ابتدا تمام تصاویر را مخفی می‌کنیم
        gridItems.forEach(image => image.classList.add('hidden'));

        // فقط تصاویری که مربوط به دسته انتخابی هستند را نشان می‌دهیم
        gridItems.forEach((item) => {
            if (item.getAttribute("category-img-id") === categoryId) {
                item.classList.remove('hidden');
            }
        });
    }
});




document.addEventListener("DOMContentLoaded", function () {
    const accordions = document.querySelectorAll('.accordion-button');
  
    accordions.forEach((button, index) => {
      button.addEventListener('click', function () {
        // انتخاب محتوای مربوط به دکمه
        const content = button.nextElementSibling;
  
        // اگر محتوا مخفی است، آن را نمایش دهیم
        if (content.classList.contains('hidden')) {
          // مخفی کردن تمام محتواها
          document.querySelectorAll('.accordion-content').forEach(item => item.classList.add('hidden'));
  
          // نمایش محتوای مربوطه
          content.classList.remove('hidden');
        } else {
          // اگر محتوای فعلی نمایش داده شده، آن را مخفی کنیم
          content.classList.add('hidden');
        }
      });
    });
  });
  
  
  
document.addEventListener("DOMContentLoaded", () => {
  const btnsShowModal = document.querySelector(".btn-modal-1");
  const btnsCloseModal = document.querySelector(".close-modal-adamtaeid");
  const btnsSendModal = document.querySelector(".btn-send-modal");
  const contentModals = document.querySelector(".modal-ticket");

  // نمایش مدال
  if (btnsShowModal) {
    btnsShowModal.addEventListener("click", () => {
      contentModals.classList.remove("hidden");
    });
  }

  // بستن مدال
  if (btnsCloseModal) {
    btnsCloseModal.addEventListener("click", () => {
      contentModals.classList.add("hidden");
    });
  }

  if (btnsSendModal) {
    btnsSendModal.addEventListener("click", () => {
      contentModals.classList.add("hidden");
    });
  }


  if (contentModals) {
    contentModals.addEventListener("click", (e) => {

      if (e.target === contentModals) {
        contentModals.classList.add("hidden");
      }
    });
  }
});


