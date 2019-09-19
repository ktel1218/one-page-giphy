$(document).ready(function() {
  console.log("ready!");


  // on form submission ...
  $('form').on('submit', function() {

    console.log("the form has beeen submitted");

    // grab values
    searchTerm = $('input[name="search_term"]').val();
    console.log(searchTerm)

    $.ajax({
      type: "POST",
      url: "/",
      data : { 'search_term': searchTerm},
      success: function(results) {
        // $('input').hide();
        // var randNum = Math.floor(Math.random() * Object.keys(results.items).length)
        console.log(results);
        $('#results').html('<img src="'+results+'">');
        // $('input').val('')
      },
      error: function(error) {
        console.log(error)
      }
    });

  });
});