function atualizaQueryString() {
  const q = document.getElementById("busca").value;

  const url = new URL(location);
  if (q) url.searchParams.set("q", q);
  else url.searchParams.delete("q");

  const tagsContainer = document.getElementById("tags-filtragem");
  tagsContainer
    .querySelectorAll("input[type=checkbox]:checked + label")
    .forEach((el) => {
      const tagParam = "tag--" + el.innerText;
      url.searchParams.set(tagParam, true);
    });
  tagsContainer
    .querySelectorAll("input[type=checkbox]:not(:checked) + label")
    .forEach((el) => {
      const tagParam = "tag--" + el.innerText;
      url.searchParams.delete(tagParam);
    });

  history.pushState({}, "", url);
}
