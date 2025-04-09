function search() {
    var search_input = document.getElementById('place-list-search-bar');
    filter = search_input.value.toLowerCase();
    table_rows = document.getElementsByTagName('tr')
  
    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < table_rows.length; i++) {
      place_list_item = table_rows[i]
      if (place_list_item.textContent.toLowerCase().indexOf(filter) > -1) {
        table_rows[i].style.display = "";
      } else {
        table_rows[i].style.display = "none";
      }
    }
  }