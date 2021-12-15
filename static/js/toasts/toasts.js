const toastElList = [].slice.call(document.querySelectorAll('.toast'));
const toastList = toastElList.map((myToast) => new bootstrap.Toast(myToast).show());