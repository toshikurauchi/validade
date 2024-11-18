const tagsInput = document.getElementById("tags-input");
const selectedTagsContainer = document.getElementById("selected-tags");
const selectedTagsHiddenInputsContainer = document.getElementById(
  "selected-tags-hidden-inputs"
);

function updateSelectedTagsHiddenInputs() {
  selectedTagsHiddenInputsContainer.innerHTML = selectedTags
    .map((tag, index) => {
      return `<input type="hidden" name="tag-${index}" value="${tag}">`;
    })
    .join("\n");
}

const selectedTags = [];
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
  tagElement.addEventListener("click", function () {
    selectedTags.splice(selectedTags.indexOf(tag), 1);
    updateSelectedTagsHiddenInputs();
    selectedTagsContainer.removeChild(tagElement);
  });

  selectedTagsContainer.appendChild(tagElement);
  selectedTags.push(tag);

  updateSelectedTagsHiddenInputs();

  tagsInput.value = "";
});
