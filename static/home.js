function create() {
    window.location.href = "../create/";
}


function Delete(id) {
    refresh = true;
    let form = document.querySelector('.form' + id);
    let confirmation = confirm("Are you sure to delete this Post?");
    if (confirmation) {
        form.submit();
    }
    else {
        return false;
    }
}

function Edit(id) {
    window.location.href = "../edit/" + id;
}

function checkaccept() {
    location.reload();
}