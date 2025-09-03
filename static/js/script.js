// Bootstrap modal confirm delete
const confirmDeleteModal = document.getElementById("confirmDeleteModal");

if (confirmDeleteModal) {
  confirmDeleteModal.addEventListener("show.bs.modal", (event) => {
    const button = event.relatedTarget;
    const userId = button.getAttribute("data-user-id");
    const userName = button.getAttribute("data-user-name");

    const message = confirmDeleteModal.querySelector("#deleteMessage");
    const confirmBtn = confirmDeleteModal.querySelector("#confirmDeleteBtn");

    message.textContent = `Are you sure you want to delete ${userName}?`;
    confirmBtn.href = `/users/delete/${userId}`;
  });
}
