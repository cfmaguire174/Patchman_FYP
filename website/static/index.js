function deleteComputer(computerId) {
  fetch("/delete-computer", {
    method: "POST",
    body: JSON.stringify({ computerId: computerId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function patchComputer(computerId) {
  fetch("/patch-computer", {
    method: "POST",
    body: JSON.stringify({ computerId: computerId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
