const toastElList = [].slice.call(document.querySelectorAll('.toast'))
const toastList = toastElList.map(function (myToast) {
  return new bootstrap.Toast(myToast).show()
})