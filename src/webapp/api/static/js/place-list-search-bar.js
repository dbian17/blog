window.addEventListener('load', function () {
  const searchBar = document.getElementById('search-bar'); 
  const tableRows = document.getElementsByTagName('tr');

  searchBar.addEventListener('keyup', function search(e) {
    filter = e.target.value.trim().toLowerCase();

    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < tableRows.length; i++) {
      place_list_item = tableRows[i]
      if (place_list_item.textContent.toLowerCase().indexOf(filter) > -1) {
        tableRows[i].style.display = "";
      } else {
        tableRows[i].style.display = "none";
      }
    }
  });
});
