const topicList = document.querySelector("#topic-list");
const topicHeadings = document.querySelectorAll(".topics h2, .topics h3");

topicHeadings.forEach((heading) => {
    const item = document.createElement("li");
    item.textContent = heading.textContent;
    topicList.appendChild(item);
});