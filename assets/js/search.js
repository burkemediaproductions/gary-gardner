document.addEventListener("DOMContentLoaded", async () => {
  const params = new URLSearchParams(window.location.search);
  const query = (params.get("q") || "").trim();

  const input = document.getElementById("search-query");
  const summary = document.getElementById("search-status");
  const resultsContainer = document.getElementById("search-results");

  if (input) input.value = query;

  if (!resultsContainer) return;

  if (!query) {
    if (summary) summary.textContent = "Enter a keyword or phrase to search the site.";
    resultsContainer.innerHTML = "";
    return;
  }

  let pages = [];

  try {
    const response = await fetch("/search/search-index.json", { cache: "no-store" });
    if (!response.ok) throw new Error("Search index not found.");
    pages = await response.json();
  } catch (error) {
    console.error(error);
    if (summary) summary.textContent = "Sorry, the search index could not be loaded.";
    resultsContainer.innerHTML = "";
    return;
  }

  const q = query.toLowerCase();

  const results = pages.filter((page) => {
    const title = (page.title || "").toLowerCase();
    const content = (page.content || "").toLowerCase();
    const url = (page.url || "").toLowerCase();
    return title.includes(q) || content.includes(q) || url.includes(q);
  });

  if (summary) {
    summary.textContent =
      results.length === 1
        ? `1 result found for "${query}"`
        : `${results.length} results found for "${query}"`;
  }

  if (!results.length) {
    resultsContainer.innerHTML = `
      <div class="search-empty">
        <p>No results matched your search.</p>
        <p>Try a different keyword, shorter phrase, or broader term.</p>
      </div>
    `;
    return;
  }

  resultsContainer.innerHTML = results.map((page) => {
    const excerpt = page.content
      ? (page.content.length > 180 ? page.content.slice(0, 180) + "..." : page.content)
      : "";

    return `
      <article class="search-result">
        <h2><a href="${page.url}">${page.title}</a></h2>
        <p class="search-result-url">${page.url}</p>
        ${excerpt ? `<p>${excerpt}</p>` : ""}
      </article>
    `;
  }).join("");
});
