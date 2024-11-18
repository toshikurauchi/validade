function initProductForm(container) {
  const selectedTags = [];

  const tagsInput = container.querySelector("#tags-input");
  const selectedTagsContainer = container.querySelector("#selected-tags");
  const selectedTagsHiddenInputsContainer = container.querySelector(
    "#selected-tags-hidden-inputs"
  );

  function updateSelectedTagsHiddenInputs() {
    selectedTagsHiddenInputsContainer.innerHTML = selectedTags
      .map((tag, index) => {
        return `<input type="hidden" name="tag-${index}" value="${tag}">`;
      })
      .join("\n");
  }

  function handleTagClick(event) {
    selectedTags.splice(selectedTags.indexOf(event.target.innerText), 1);
    updateSelectedTagsHiddenInputs();
    selectedTagsContainer.removeChild(event.target);
  }

  selectedTagsContainer.querySelectorAll("span").forEach((tagElement) => {
    selectedTags.push(tagElement.innerText);
    tagElement.addEventListener("click", handleTagClick);
  });

  tagsInput.addEventListener("change", function (event) {
    const tag = event.target.value;
    if (!tag || selectedTags.includes(tag)) {
      tagsInput.value = "";
      return;
    }

    const tagElement = document.createElement("span");
    tagElement.classList.add("px-2", "py-1", "rounded");
    tagElement.style.backgroundColor = COR_FUNDO[tag];
    tagElement.style.color = COR_TEXTO[tag];
    tagElement.textContent = tag;
    tagElement.addEventListener("click", handleTagClick);

    selectedTagsContainer.appendChild(tagElement);
    selectedTags.push(tag);

    updateSelectedTagsHiddenInputs();

    tagsInput.value = "";
  });
}
